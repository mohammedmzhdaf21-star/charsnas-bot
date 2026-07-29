"""Undergraduate pharmacy study content by specialty and difficulty."""
from __future__ import annotations

import random

from quiz_bank import DIFFICULTIES, DIFFICULTY_LABELS, LABEL_TO_DIFFICULTY

SPECIALTY_ORDER = ['pharmacology', 'clinical_pharmacy', 'pharmaceutics', 'pharmacokinetics', 'medicinal_chemistry', 'pharmacognosy', 'pharmacy_practice', 'hospital_pharmacy', 'toxicology', 'pharm_microbiology']

SPECIALTIES: dict[str, dict] = {'pharmacology': {'label': 'Pharmacology',
                  'books': ["Rang and Dale's Pharmacology",
                            'Katzung Basic & Clinical Pharmacology',
                            "Goodman & Gilman's"],
                  'pdf_notes': ['Agonist activates; antagonist blocks receptors.',
                                'First-pass metabolism can reduce oral bioavailability.',
                                'Narrow therapeutic index drugs need monitoring.',
                                'Know major CYP inducers/inhibitors.',
                                'ACEI cough; beta-blockers caution in asthma.'],
                  'questions': {'easy': [{'question': 'Agonist means a drug that?',
                                          'options': ['A) Activates a receptor',
                                                      'B) Only blocks a receptor',
                                                      'C) Only inhibits an enzyme always',
                                                      'D) Only is a vitamin'],
                                          'answer': 'A) Activates a receptor',
                                          'explanation': 'Agonists activate receptors; antagonists '
                                                         'block.'},
                                         {'question': 'First-pass metabolism mainly occurs after?',
                                          'options': ['A) Oral absorption via liver',
                                                      'B) IV bolus only',
                                                      'C) Intramuscular only always',
                                                      'D) Topical cream only'],
                                          'answer': 'A) Oral absorption via liver',
                                          'explanation': 'Oral drugs may undergo extensive hepatic '
                                                         'first-pass.'},
                                         {'question': 'Therapeutic index relates to?',
                                          'options': ['A) Safety margin between effective and '
                                                      'toxic doses',
                                                      'B) Only tablet color',
                                                      'C) Only brand name',
                                                      'D) Only price'],
                                          'answer': 'A) Safety margin between effective and toxic '
                                                    'doses',
                                          'explanation': 'Narrow TI drugs need careful '
                                                         'monitoring.'}],
                                'medium': [{'question': 'Beta-blocker caution is highest in?',
                                            'options': ['A) Asthma (nonselective agents)',
                                                        'B) Only mild acne',
                                                        'C) Only myopia',
                                                        'D) Only caries'],
                                            'answer': 'A) Asthma (nonselective agents)',
                                            'explanation': 'Bronchoconstriction risk.'},
                                           {'question': 'ACE inhibitor common side effect?',
                                            'options': ['A) Dry cough',
                                                        'B) Only orange urine always',
                                                        'C) Only gingival hyperplasia classic for '
                                                        'this class',
                                                        'D) Only ototoxicity classic'],
                                            'answer': 'A) Dry cough',
                                            'explanation': 'Bradykinin-related; ARB alternative '
                                                           'often.'},
                                           {'question': 'Zero-order elimination example theme?',
                                            'options': ['A) Phenytoin / ethanol at higher levels',
                                                        'B) Always all antibiotics',
                                                        'C) Always all vitamins',
                                                        'D) Always saline'],
                                            'answer': 'A) Phenytoin / ethanol at higher levels',
                                            'explanation': 'Saturable kinetics.'}],
                                'hard': [{'question': 'A junior colleague asks for the single best '
                                                      'answer. Competitive antagonist effect on '
                                                      'agonist curve? Beware of near-miss '
                                                      'distractors.',
                                          'options': ['A) Right shift; same maximal response if '
                                                      'surmountable',
                                                      'B) Always lowers Vmax of enzyme only',
                                                      'C) Always irreversible covalent binding '
                                                      'only',
                                                      'D) No change ever'],
                                          'answer': 'A) Right shift; same maximal response if '
                                                    'surmountable',
                                          'explanation': 'Noncompetitive often depresses max '
                                                         'response.'},
                                         {'question': 'A junior colleague asks for the single best '
                                                      'answer. CYP3A4 induction may? Beware of '
                                                      'near-miss distractors.',
                                          'options': ['A) Reduce substrate drug levels',
                                                      'B) Always increase all drug levels',
                                                      'C) Only change tablet shape',
                                                      'D) Only affect topical drugs'],
                                          'answer': 'A) Reduce substrate drug levels',
                                          'explanation': 'Clinically important interactions.'},
                                         {'question': 'A junior colleague asks for the single best '
                                                      'answer. Loading dose mainly depends on? '
                                                      'Beware of near-miss distractors.',
                                          'options': ['A) Volume of distribution and target '
                                                      'concentration',
                                                      'B) Only clearance',
                                                      'C) Only half-life alone forever',
                                                      'D) Only taste'],
                                          'answer': 'A) Volume of distribution and target '
                                                    'concentration',
                                          'explanation': 'Maintenance relates more to clearance.'}],
                                'extreme': [{'question': 'In a high-stakes pharmacy scenario with '
                                                         'incomplete data, which statement is MOST '
                                                         'correct? Torsades risk rises with? Avoid '
                                                         'actions that could harm if a critical '
                                                         'risk remains open.',
                                             'options': ['A) QT-prolonging drugs + electrolyte '
                                                         'imbalance',
                                                         'B) Only paracetamol at therapeutic dose '
                                                         'always',
                                                         'C) Only topical emollients',
                                                         'D) Only vitamins C/D always'],
                                             'answer': 'A) QT-prolonging drugs + electrolyte '
                                                       'imbalance',
                                             'explanation': 'Check interactions and K/Mg.'},
                                            {'question': 'In a high-stakes pharmacy scenario with '
                                                         'incomplete data, which statement is MOST '
                                                         'correct? Serotonin syndrome risk '
                                                         'combination theme? Avoid actions that '
                                                         'could harm if a critical risk remains '
                                                         'open.',
                                             'options': ['A) MAOI + SSRI / certain serotonergic '
                                                         'combos',
                                                         'B) Only two topical steroids',
                                                         'C) Only antacids together',
                                                         'D) Only fluoride + calcium always'],
                                             'answer': 'A) MAOI + SSRI / certain serotonergic '
                                                       'combos',
                                             'explanation': 'Potentially life-threatening.'},
                                            {'question': 'In a high-stakes pharmacy scenario with '
                                                         'incomplete data, which statement is MOST '
                                                         'correct? Narrow therapeutic index '
                                                         'warfarin interaction? Avoid actions that '
                                                         'could harm if a critical risk remains '
                                                         'open.',
                                             'options': ['A) CYP2C9 inhibitors can raise INR/bleed '
                                                         'risk',
                                                         'B) Never interacts',
                                                         'C) Only with toothpaste',
                                                         'D) Only with sunlight'],
                                             'answer': 'A) CYP2C9 inhibitors can raise INR/bleed '
                                                       'risk',
                                             'explanation': 'Monitor INR closely.'}]},
                  'cases': {'easy': [{'title': 'New Oral Drug Discussion',
                                      'stem': 'A student asks why an oral dose is much higher than '
                                              'the IV dose for the same drug.',
                                      'question': 'Key concept?',
                                      'answer': 'First-pass hepatic metabolism reducing oral '
                                                'bioavailability.',
                                      'discussion': 'Compare bioavailability and route selection.',
                                      'book_hint': "Rang and Dale's Pharmacology / Katzung"}],
                            'medium': [{'title': 'Cough on Antihypertensive',
                                        'stem': 'A patient develops dry cough after starting '
                                                'enalapril.',
                                        'question': 'Likely cause?',
                                        'answer': 'ACE inhibitor–related cough.',
                                        'discussion': 'Consider switching to an ARB if '
                                                      'appropriate.',
                                        'book_hint': "Rang and Dale's Pharmacology / Katzung"}],
                            'hard': [{'title': 'Seizure Drug Levels Fall',
                                      'stem': 'A patient on carbamazepine starts a strong CYP '
                                              'inducer; seizures return. Choose the safest '
                                              'high-yield next concept before definitive results.',
                                      'question': 'Mechanism theme?',
                                      'answer': 'Induction lowering carbamazepine concentration.',
                                      'discussion': 'Monitor levels and adjust.',
                                      'book_hint': "Rang and Dale's Pharmacology / Katzung"}],
                            'extreme': [{'title': 'Polypharmacy Syncope',
                                         'stem': 'An elderly patient on multiple QT-prolonging '
                                                 'drugs has syncope and polymorphic VT. Avoid '
                                                 'harmful premature treatment while catastrophic '
                                                 'differentials remain open.',
                                         'question': 'Concern?',
                                         'answer': 'Drug-induced TdP — stop offenders, correct '
                                                   'electrolytes, specialist care.',
                                         'discussion': 'Review all QT drugs and interactions.',
                                         'book_hint': "Rang and Dale's Pharmacology / Katzung"}]}},
 'clinical_pharmacy': {'label': 'Clinical Pharmacy',
                       'books': ['Clinical Pharmacy and Therapeutics — Walker',
                                 'Applied Therapeutics',
                                 'Pharmacotherapy — DiPiro'],
                       'pdf_notes': ['Medication reconciliation prevents omission/duplication.',
                                     'Renal/hepatic function drives many dose adjustments.',
                                     'Beers/STOPP themes for older adults.',
                                     'High-alert medicines need extra safeguards.',
                                     'Counsel on ADRs and when to seek help.'],
                       'questions': {'easy': [{'question': 'Medication reconciliation aims to?',
                                               'options': ['A) Ensure accurate medication lists '
                                                           'across transitions',
                                                           'B) Only count tablets in a bottle for '
                                                           'fun',
                                                           'C) Only change brands randomly',
                                                           'D) Only remove all drugs always'],
                                               'answer': 'A) Ensure accurate medication lists '
                                                         'across transitions',
                                               'explanation': 'Reduce errors at '
                                                              'admission/discharge.'},
                                              {'question': 'ADR means?',
                                               'options': ['A) Adverse drug reaction',
                                                           'B) Average daily rate only',
                                                           'C) Antibiotic dose range only',
                                                           'D) Absolute drug resistance only'],
                                               'answer': 'A) Adverse drug reaction',
                                               'explanation': 'Detect, report, manage.'},
                                              {'question': 'Counseling on antibiotics should '
                                                           'include?',
                                               'options': ['A) Complete course as directed / '
                                                           'stewardship themes',
                                                           'B) Stop when feeling better always '
                                                           'without advice',
                                                           'C) Share with family always',
                                                           'D) Double dose if missed three times '
                                                           'always'],
                                               'answer': 'A) Complete course as directed / '
                                                         'stewardship themes',
                                               'explanation': 'Local guidance matters.'}],
                                     'medium': [{'question': 'Beers Criteria help identify?',
                                                 'options': ['A) Potentially inappropriate meds in '
                                                             'older adults',
                                                             'B) Only pediatric syrup flavors',
                                                             'C) Only IV compatibility forever',
                                                             'D) Only tablet imprint codes'],
                                                 'answer': 'A) Potentially inappropriate meds in '
                                                           'older adults',
                                                 'explanation': 'Deprescribing support.'},
                                                {'question': 'Renal dose adjustment needed when?',
                                                 'options': ['A) Drug cleared renally and GFR '
                                                             'reduced',
                                                             'B) Only for topical creams always',
                                                             'C) Only for eye drops always',
                                                             'D) Never for antibiotics'],
                                                 'answer': 'A) Drug cleared renally and GFR '
                                                           'reduced',
                                                 'explanation': 'Avoid accumulation/toxicity.'},
                                                {'question': 'Anticoagulant counseling key point?',
                                                 'options': ['A) Bleeding signs and interaction '
                                                             'awareness',
                                                             'B) Stop for headaches without advice '
                                                             'always',
                                                             'C) Take only when eating spinach '
                                                             'exclusively',
                                                             'D) Never tell dentist'],
                                                 'answer': 'A) Bleeding signs and interaction '
                                                           'awareness',
                                                 'explanation': 'Safety netting.'}],
                                     'hard': [{'question': 'A junior colleague asks for the single '
                                                           'best answer. Vancomycin dosing '
                                                           'commonly uses? Beware of near-miss '
                                                           'distractors.',
                                               'options': ['A) Weight and renal function ± levels',
                                                           'B) Only age in months forever',
                                                           'C) Only tablet color',
                                                           'D) Fixed infant dose for all adults'],
                                               'answer': 'A) Weight and renal function ± levels',
                                               'explanation': 'TDM in many protocols.'},
                                              {'question': 'A junior colleague asks for the single '
                                                           'best answer. Hyperkalemia risk with? '
                                                           'Beware of near-miss distractors.',
                                               'options': ['A) ACEI + spironolactone combinations',
                                                           'B) Only topical NSAID gel always',
                                                           'C) Only lactulose',
                                                           'D) Only artificial tears'],
                                               'answer': 'A) ACEI + spironolactone combinations',
                                               'explanation': 'Monitor K+.'},
                                              {'question': 'A junior colleague asks for the single '
                                                           'best answer. Steroid sick-day rules '
                                                           'teach? Beware of near-miss '
                                                           'distractors.',
                                               'options': ['A) Increase dose during significant '
                                                           'illness per plan',
                                                           'B) Stop suddenly when ill always',
                                                           'C) Never tell anyone about steroids',
                                                           'D) Only take every other month'],
                                               'answer': 'A) Increase dose during significant '
                                                         'illness per plan',
                                               'explanation': 'Prevent adrenal crisis.'}],
                                     'extreme': [{'question': 'In a high-stakes pharmacy scenario '
                                                              'with incomplete data, which '
                                                              'statement is MOST correct? '
                                                              'Chemotherapy extravasation '
                                                              'priority? Avoid actions that could '
                                                              'harm if a critical risk remains '
                                                              'open.',
                                                  'options': ['A) Stop infusion and follow '
                                                              'protocol antidote/pathway',
                                                              'B) Speed up infusion',
                                                              'C) Ignore swelling',
                                                              'D) Give IM antibiotic into same '
                                                              'site'],
                                                  'answer': 'A) Stop infusion and follow protocol '
                                                            'antidote/pathway',
                                                  'explanation': 'Tissue injury risk.'},
                                                 {'question': 'In a high-stakes pharmacy scenario '
                                                              'with incomplete data, which '
                                                              'statement is MOST correct? '
                                                              'Clozapine pharmacy monitoring '
                                                              'theme? Avoid actions that could '
                                                              'harm if a critical risk remains '
                                                              'open.',
                                                  'options': ['A) Mandatory blood counts for '
                                                              'agranulocytosis risk',
                                                              'B) No labs ever needed',
                                                              'C) Only ask about taste',
                                                              'D) Only dental check'],
                                                  'answer': 'A) Mandatory blood counts for '
                                                            'agranulocytosis risk',
                                                  'explanation': 'Registry/protocol driven.'},
                                                 {'question': 'In a high-stakes pharmacy scenario '
                                                              'with incomplete data, which '
                                                              'statement is MOST correct? Opioid '
                                                              'stewardship in hospital includes? '
                                                              'Avoid actions that could harm if a '
                                                              'critical risk remains open.',
                                                  'options': ['A) Appropriate indication, dose, '
                                                              'naloxone awareness, constipation '
                                                              'prophylaxis',
                                                              'B) Unlimited PRN without review',
                                                              'C) Hide naloxone',
                                                              'D) Avoid documenting'],
                                                  'answer': 'A) Appropriate indication, dose, '
                                                            'naloxone awareness, constipation '
                                                            'prophylaxis',
                                                  'explanation': 'Safety + efficacy.'}]},
                       'cases': {'easy': [{'title': 'Discharge Med List Mismatch',
                                           'stem': "Discharge list misses the patient's home "
                                                   'anticoagulant.',
                                           'question': 'Risk?',
                                           'answer': 'Omission error — reconcile and correct '
                                                     'before discharge.',
                                           'discussion': 'High-risk meds need extra checks.',
                                           'book_hint': 'Clinical Pharmacy and Therapeutics — '
                                                        'Walker/Whittlesea'}],
                                 'medium': [{'title': 'Elderly Fall on Sedatives',
                                             'stem': 'An older adult on multiple sedating drugs '
                                                     'has recurrent falls.',
                                             'question': 'Pharmacy action theme?',
                                             'answer': 'Review sedatives; consider deprescribing '
                                                       'per Beers/STOPP themes.',
                                             'discussion': 'Falls are a major ADR outcome.',
                                             'book_hint': 'Clinical Pharmacy and Therapeutics — '
                                                          'Walker/Whittlesea'}],
                                 'hard': [{'title': 'Rising Creatinine on Dual Blockade',
                                           'stem': 'Patient on ACEI + NSAID + diuretic has rising '
                                                   'creatinine. Choose the safest high-yield next '
                                                   'concept before definitive results.',
                                           'question': 'Triple whammy concept?',
                                           'answer': 'Hemodynamically mediated AKI risk — review '
                                                     'and modify regimen.',
                                           'discussion': 'Hydration and follow-up labs matter.',
                                           'book_hint': 'Clinical Pharmacy and Therapeutics — '
                                                        'Walker/Whittlesea'}],
                                 'extreme': [{'title': 'Neutropenic Fever Post Chemo',
                                              'stem': 'A patient on myelosuppressive chemo '
                                                      'presents febrile and unwell. Avoid harmful '
                                                      'premature treatment while catastrophic '
                                                      'differentials remain open.',
                                              'question': 'Pharmacy/clinical priority concept?',
                                              'answer': 'Urgent sepsis pathway and protocol '
                                                        'antibiotics; review chemo timing/growth '
                                                        'factors per oncology plan.',
                                              'discussion': 'Do not delay for outpatient review.',
                                              'book_hint': 'Clinical Pharmacy and Therapeutics — '
                                                           'Walker/Whittlesea'}]}},
 'pharmaceutics': {'label': 'Pharmaceutics',
                   'books': ["Aulton's Pharmaceutics",
                             "Ansel's Pharmaceutical Dosage Forms",
                             'Remington'],
                   'pdf_notes': ['Excipients have functions (binder, disintegrant, etc.).',
                                 'Do not crush MR/enteric products without checking.',
                                 'BCS class guides absorption limitations.',
                                 'Sterile manufacture for injectables.',
                                 'Compatibility matters in IV admixtures.'],
                   'questions': {'easy': [{'question': 'Tablet binder helps?',
                                           'options': ['A) Hold powder particles together',
                                                       'B) Only color the coat',
                                                       'C) Only kill microbes always',
                                                       'D) Only add flavor always'],
                                           'answer': 'A) Hold powder particles together',
                                           'explanation': 'Excipient function.'},
                                          {'question': 'Bioavailability compares?',
                                           'options': ['A) Rate and extent of absorption to '
                                                       'systemic circulation',
                                                       'B) Only tablet hardness',
                                                       'C) Only bottle size',
                                                       'D) Only label font'],
                                           'answer': 'A) Rate and extent of absorption to systemic '
                                                     'circulation',
                                           'explanation': 'AUC themes.'},
                                          {'question': 'Sterile products must be?',
                                           'options': ['A) Free from viable microorganisms',
                                                       'B) Only sweet tasting',
                                                       'C) Only scored tablets',
                                                       'D) Only sugar-coated'],
                                           'answer': 'A) Free from viable microorganisms',
                                           'explanation': 'Aseptic manufacture critical.'}],
                                 'medium': [{'question': 'BCS Class II drugs are?',
                                             'options': ['A) Low solubility, high permeability',
                                                         'B) High solubility high permeability',
                                                         'C) Low solubility low permeability',
                                                         'D) High solubility low permeability'],
                                             'answer': 'A) Low solubility, high permeability',
                                             'explanation': 'Dissolution often rate-limiting.'},
                                            {'question': 'Lyophilization is?',
                                             'options': ['A) Freeze-drying',
                                                         'B) Only wet granulation',
                                                         'C) Only sugar coating',
                                                         'D) Only blister packing'],
                                             'answer': 'A) Freeze-drying',
                                             'explanation': 'Stability of injectables/biologics.'},
                                            {'question': 'Osmotic pump tablets provide?',
                                             'options': ['A) Controlled release via osmotic '
                                                         'pressure',
                                                         'B) Instant buccal only',
                                                         'C) Only topical action',
                                                         'D) No release control'],
                                             'answer': 'A) Controlled release via osmotic pressure',
                                             'explanation': 'Do not crush.'}],
                                 'hard': [{'question': 'A junior colleague asks for the single '
                                                       'best answer. Noyes–Whitney relates to? '
                                                       'Beware of near-miss distractors.',
                                           'options': ['A) Dissolution rate',
                                                       'B) Only receptor affinity',
                                                       'C) Only half-life formula alone',
                                                       'D) Only pKa of acids only without '
                                                       'dissolution'],
                                           'answer': 'A) Dissolution rate',
                                           'explanation': 'Surface area, diffusion, concentration '
                                                          'gradient.'},
                                          {'question': 'A junior colleague asks for the single '
                                                       'best answer. Partition coefficient (log P) '
                                                       'indicates? Beware of near-miss '
                                                       'distractors.',
                                           'options': ['A) Lipophilicity',
                                                       'B) Only tablet friability',
                                                       'C) Only microbial limit',
                                                       'D) Only osmolarity of NS'],
                                           'answer': 'A) Lipophilicity',
                                           'explanation': 'Affects absorption/distribution.'},
                                          {'question': 'A junior colleague asks for the single '
                                                       'best answer. HLB system helps select? '
                                                       'Beware of near-miss distractors.',
                                           'options': ['A) Emulsifying agents',
                                                       'B) Only capsule sizes',
                                                       'C) Only needle gauges',
                                                       'D) Only fridge brands'],
                                           'answer': 'A) Emulsifying agents',
                                           'explanation': 'Hydrophilic–lipophilic balance.'}],
                                 'extreme': [{'question': 'In a high-stakes pharmacy scenario with '
                                                          'incomplete data, which statement is '
                                                          'MOST correct? NANOPARTICLE carriers aim '
                                                          'to? Avoid actions that could harm if a '
                                                          'critical risk remains open.',
                                              'options': ['A) Modify '
                                                          'distribution/targeting/solubility '
                                                          'profiles',
                                                          'B) Only change bottle labels',
                                                          'C) Eliminate need for sterile technique '
                                                          'always',
                                                          'D) Remove all ADRs forever'],
                                              'answer': 'A) Modify '
                                                        'distribution/targeting/solubility '
                                                        'profiles',
                                              'explanation': 'Formulation science of advanced '
                                                             'delivery.'},
                                             {'question': 'In a high-stakes pharmacy scenario with '
                                                          'incomplete data, which statement is '
                                                          'MOST correct? Glass transition (Tg) '
                                                          'matters for? Avoid actions that could '
                                                          'harm if a critical risk remains open.',
                                              'options': ['A) Amorphous solid stability',
                                                          'B) Only metal implants',
                                                          'C) Only ECG paper',
                                                          'D) Only suture color'],
                                              'answer': 'A) Amorphous solid stability',
                                              'explanation': 'Physical stability of amorphous '
                                                             'drugs.'},
                                             {'question': 'In a high-stakes pharmacy scenario with '
                                                          'incomplete data, which statement is '
                                                          'MOST correct? Extractables/leachables '
                                                          'concern in? Avoid actions that could '
                                                          'harm if a critical risk remains open.',
                                              'options': ['A) Container–closure systems for '
                                                          'injectables',
                                                          'B) Only paper leaflets',
                                                          'C) Only cardboard shippers without '
                                                          'contact',
                                                          'D) Only pharmacy uniforms'],
                                              'answer': 'A) Container–closure systems for '
                                                        'injectables',
                                              'explanation': 'Patient safety in packaging.'}]},
                   'cases': {'easy': [{'title': 'Why Not Crush This Tablet?',
                                       'stem': 'A nurse asks to crush an enteric-coated tablet for '
                                               'a tube feed.',
                                       'question': 'Problem?',
                                       'answer': 'Coating protects drug/stomach; crushing may '
                                                 'destroy intended release/stability.',
                                       'discussion': 'Find suitable alternative formulation.',
                                       'book_hint': "Aulton's Pharmaceutics"}],
                             'medium': [{'title': 'Extended-Release Crush Request',
                                         'stem': 'Ward wants XR opioid crushed for dysphagia.',
                                         'question': 'Risk?',
                                         'answer': 'Dose dumping — potentially fatal; use '
                                                   'appropriate formulation.',
                                         'discussion': 'Never crush XR opioids.',
                                         'book_hint': "Aulton's Pharmaceutics"}],
                             'hard': [{'title': 'Cloudy IV Admixture',
                                       'stem': 'Two IV drugs mixed; solution becomes cloudy. '
                                               'Choose the safest high-yield next concept before '
                                               'definitive results.',
                                       'question': 'Concern?',
                                       'answer': 'Incompatibility/precipitation — do not infuse; '
                                                 'check compatibility resources.',
                                       'discussion': 'Line flushing/separation strategies.',
                                       'book_hint': "Aulton's Pharmaceutics"}],
                             'extreme': [{'title': 'Biologic Aggregation After Shaking',
                                          'stem': 'A nurse vigorously shakes a protein biologic; '
                                                  'product foams. Avoid harmful premature '
                                                  'treatment while catastrophic differentials '
                                                  'remain open.',
                                          'question': 'Issue?',
                                          'answer': 'Possible denaturation/aggregation — follow '
                                                    'handling IFU; may need to discard per '
                                                    'protocol.',
                                          'discussion': 'Educate on gentle handling.',
                                          'book_hint': "Aulton's Pharmaceutics"}]}},
 'pharmacokinetics': {'label': 'Pharmacokinetics',
                      'books': ['Applied Biopharmaceutics & Pharmacokinetics — Shargel',
                                'Rowland and Tozer',
                                'Clinical Pharmacokinetics concepts texts'],
                      'pdf_notes': ['Half-life guides dosing interval.',
                                    'Clearance determines maintenance dose.',
                                    'Steady state ~4–5 half-lives.',
                                    'TDM timing is critical.',
                                    'Nonlinear kinetics (phenytoin) need careful titration.'],
                      'questions': {'easy': [{'question': 'Half-life is time for?',
                                              'options': ['A) Plasma concentration to fall by 50%',
                                                          'B) Drug to be ordered',
                                                          'C) Tablet to be coated',
                                                          'D) Prescription to expire only'],
                                              'answer': 'A) Plasma concentration to fall by 50%',
                                              'explanation': 'Dosing interval planning.'},
                                             {'question': 'Clearance reflects?',
                                              'options': ['A) Volume of plasma cleared of drug per '
                                                          'time',
                                                          'B) Only stomach emptying',
                                                          'C) Only tablet diameter',
                                                          'D) Only urine color'],
                                              'answer': 'A) Volume of plasma cleared of drug per '
                                                        'time',
                                              'explanation': 'Determines maintenance dose.'},
                                             {'question': 'Steady state roughly after?',
                                              'options': ['A) ~4–5 half-lives with regular dosing',
                                                          'B) 1 minute always',
                                                          'C) 1 year always',
                                                          'D) Never'],
                                              'answer': 'A) ~4–5 half-lives with regular dosing',
                                              'explanation': 'Loading dose can reach faster.'}],
                                    'medium': [{'question': 'AUC represents?',
                                                'options': ['A) Overall exposure',
                                                            'B) Only peak only',
                                                            'C) Only trough only',
                                                            'D) Only tablet weight'],
                                                'answer': 'A) Overall exposure',
                                                'explanation': 'Key in '
                                                               'bioavailability/bioequivalence.'},
                                               {'question': 'Nonlinear PK means?',
                                                'options': ['A) Parameters change with dose (e.g., '
                                                            'saturation)',
                                                            'B) Always linear forever at all doses',
                                                            'C) Only applies to placebos',
                                                            'D) Only topical creams'],
                                                'answer': 'A) Parameters change with dose (e.g., '
                                                          'saturation)',
                                                'explanation': 'Phenytoin classic.'},
                                               {'question': 'Protein binding displacement may?',
                                                'options': ['A) Transiently raise free fraction '
                                                            'for highly bound drugs',
                                                            'B) Never matter',
                                                            'C) Only change pill color',
                                                            'D) Only affect IV bags labels'],
                                                'answer': 'A) Transiently raise free fraction for '
                                                          'highly bound drugs',
                                                'explanation': 'Clinically nuanced; clearance '
                                                               'often adjusts.'}],
                                    'hard': [{'question': 'A junior colleague asks for the single '
                                                          'best answer. Hepatic clearance for high '
                                                          'extraction drugs depends strongly on? '
                                                          'Beware of near-miss distractors.',
                                              'options': ['A) Liver blood flow',
                                                          'B) Only plasma protein binding always '
                                                          'solely',
                                                          'C) Only tablet shape',
                                                          'D) Only gut motility solely'],
                                              'answer': 'A) Liver blood flow',
                                              'explanation': 'Extraction ratio concepts.'},
                                             {'question': 'A junior colleague asks for the single '
                                                          'best answer. Renal clearance includes? '
                                                          'Beware of near-miss distractors.',
                                              'options': ['A) Filtration − reabsorption + '
                                                          'secretion',
                                                          'B) Only secretion forever',
                                                          'C) Only reabsorption forever',
                                                          'D) Only bile'],
                                              'answer': 'A) Filtration − reabsorption + secretion',
                                              'explanation': 'pH/ion trapping can matter.'},
                                             {'question': 'A junior colleague asks for the single '
                                                          'best answer. Two-compartment model '
                                                          'early phase is? Beware of near-miss '
                                                          'distractors.',
                                              'options': ['A) Distribution phase',
                                                          'B) Only elimination phase always from '
                                                          't=0',
                                                          'C) Only absorption for IV bolus',
                                                          'D) Only metabolism in gut only'],
                                              'answer': 'A) Distribution phase',
                                              'explanation': 'Multi-compartment kinetics.'}],
                                    'extreme': [{'question': 'In a high-stakes pharmacy scenario '
                                                             'with incomplete data, which '
                                                             'statement is MOST correct? TDM for '
                                                             'digoxin timing? Avoid actions that '
                                                             'could harm if a critical risk '
                                                             'remains open.',
                                                 'options': ['A) Avoid sampling in distribution '
                                                             'phase; sample at steady state '
                                                             'appropriately',
                                                             'B) Sample 5 minutes after IV push '
                                                             'always as trough',
                                                             'C) Any random time is identical',
                                                             'D) Never sample'],
                                                 'answer': 'A) Avoid sampling in distribution '
                                                           'phase; sample at steady state '
                                                           'appropriately',
                                                 'explanation': 'Mis-timed levels cause wrong dose '
                                                                'changes.'},
                                                {'question': 'In a high-stakes pharmacy scenario '
                                                             'with incomplete data, which '
                                                             'statement is MOST correct? '
                                                             'Bioequivalence typically compares? '
                                                             'Avoid actions that could harm if a '
                                                             'critical risk remains open.',
                                                 'options': ['A) AUC and Cmax within regulatory '
                                                             'limits',
                                                             'B) Only taste panels',
                                                             'C) Only bottle shape',
                                                             'D) Only price'],
                                                 'answer': 'A) AUC and Cmax within regulatory '
                                                           'limits',
                                                 'explanation': 'Generic substitution science.'},
                                                {'question': 'In a high-stakes pharmacy scenario '
                                                             'with incomplete data, which '
                                                             'statement is MOST correct? Nonlinear '
                                                             'binding + saturable clearance '
                                                             'together can cause? Avoid actions '
                                                             'that could harm if a critical risk '
                                                             'remains open.',
                                                 'options': ['A) Complex dose–concentration '
                                                             'relationships',
                                                             'B) Perfect proportionality always',
                                                             'C) No clinical relevance ever',
                                                             'D) Only affects ointments'],
                                                 'answer': 'A) Complex dose–concentration '
                                                           'relationships',
                                                 'explanation': 'Expert dosing required.'}]},
                      'cases': {'easy': [{'title': 'Why Wait for Steady State?',
                                          'stem': 'Team wants a level 2 hours after first '
                                                  "gentamicin dose as 'trough steady state'.",
                                          'question': 'Teaching point?',
                                          'answer': 'Steady state needs multiple half-lives unless '
                                                    'loading used; interpret timing correctly.',
                                          'discussion': 'Wrong timing misleads TDM.',
                                          'book_hint': 'Applied Biopharmaceutics & '
                                                       'Pharmacokinetics — Shargel'}],
                                'medium': [{'title': 'Phenytoin Dose Doubled',
                                            'stem': 'Phenytoin dose doubled because level was '
                                                    'slightly low; patient becomes toxic.',
                                            'question': 'Why?',
                                            'answer': 'Saturable metabolism — small dose hikes can '
                                                      'cause large level jumps.',
                                            'discussion': 'Titrate carefully.',
                                            'book_hint': 'Applied Biopharmaceutics & '
                                                         'Pharmacokinetics — Shargel'}],
                                'hard': [{'title': 'Aminoglycoside Once-Daily',
                                          'stem': 'Protocol uses extended-interval aminoglycoside '
                                                  'dosing. Choose the safest high-yield next '
                                                  'concept before definitive results.',
                                          'question': 'PK/PD rationale theme?',
                                          'answer': 'Concentration-dependent killing + adaptive '
                                                    'resistance considerations; monitor '
                                                    'levels/renal function per protocol.',
                                          'discussion': 'Not the same as old multiple-daily '
                                                        'empiric habits.',
                                          'book_hint': 'Applied Biopharmaceutics & '
                                                       'Pharmacokinetics — Shargel'}],
                                'extreme': [{'title': 'Transplant Tacrolimus Interaction',
                                             'stem': 'Tacrolimus levels soar after starting a '
                                                     'strong CYP3A4/P-gp inhibitor. Avoid harmful '
                                                     'premature treatment while catastrophic '
                                                     'differentials remain open.',
                                             'question': 'Action concept?',
                                             'answer': 'Recognize interaction, hold/adjust per '
                                                       'protocol, repeat levels, coordinate '
                                                       'transplant team.',
                                             'discussion': 'Narrow TI immunosuppressants are '
                                                           'high-alert.',
                                             'book_hint': 'Applied Biopharmaceutics & '
                                                          'Pharmacokinetics — Shargel'}]}},
 'medicinal_chemistry': {'label': 'Medicinal Chemistry',
                         'books': ["Foye's Principles of Medicinal Chemistry",
                                   'Wilson and Gisvold',
                                   'The Organic Chemistry of Drug Design'],
                         'pdf_notes': ['SAR links structure to activity.',
                                       'Prodrugs improve delivery then activate.',
                                       'pKa affects ionization and absorption.',
                                       'Chirality can change effect/toxicity.',
                                       'Beta-lactam ring is central to many antibiotics.'],
                         'questions': {'easy': [{'question': 'SAR means?',
                                                 'options': ['A) Structure–activity relationship',
                                                             'B) Serum antibiotic rate',
                                                             'C) Syringe aspiration rule',
                                                             'D) Sterile air ratio'],
                                                 'answer': 'A) Structure–activity relationship',
                                                 'explanation': 'How structure changes activity.'},
                                                {'question': 'Prodrug is?',
                                                 'options': ['A) Inactive form converted in vivo '
                                                             'to active drug',
                                                             'B) Always more toxic forever',
                                                             'C) Never absorbed',
                                                             'D) Only a placebo'],
                                                 'answer': 'A) Inactive form converted in vivo to '
                                                           'active drug',
                                                 'explanation': 'Improve properties/delivery.'},
                                                {'question': 'pKa helps predict?',
                                                 'options': ['A) Ionization at a given pH',
                                                             'B) Only tablet hardness',
                                                             'C) Only microbial purity',
                                                             'D) Only label glue'],
                                                 'answer': 'A) Ionization at a given pH',
                                                 'explanation': 'Affects solubility/absorption.'}],
                                       'medium': [{'question': 'Beta-lactam ring is essential for?',
                                                   'options': ['A) Many penicillins/cephalosporins '
                                                               'antibacterial action',
                                                               'B) Only opioid analgesia',
                                                               'C) Only statin lipid effect',
                                                               'D) Only SSRI action'],
                                                   'answer': 'A) Many penicillins/cephalosporins '
                                                             'antibacterial action',
                                                   'explanation': 'Hydrolysis by beta-lactamases '
                                                                  'resists.'},
                                                  {'question': 'Chirality matters because?',
                                                   'options': ['A) Enantiomers can differ in '
                                                               'activity/toxicity',
                                                               'B) Mirror images always identical '
                                                               'clinically always',
                                                               'C) Only affects bottle color',
                                                               'D) Only affects shipping weight'],
                                                   'answer': 'A) Enantiomers can differ in '
                                                             'activity/toxicity',
                                                   'explanation': 'Stereoselective pharmacology.'},
                                                  {'question': 'Bioisostere replacement aims to?',
                                                   'options': ['A) Retain activity while improving '
                                                               'properties',
                                                               'B) Always destroy all activity',
                                                               'C) Only change trademark',
                                                               'D) Only add sugar'],
                                                   'answer': 'A) Retain activity while improving '
                                                             'properties',
                                                   'explanation': 'Classic medicinal chemistry '
                                                                  'tactic.'}],
                                       'hard': [{'question': 'A junior colleague asks for the '
                                                             'single best answer. Log D differs '
                                                             'from log P by? Beware of near-miss '
                                                             'distractors.',
                                                 'options': ['A) Accounting for ionization at a pH',
                                                             'B) Being unrelated to lipophilicity',
                                                             'C) Only measuring melting point',
                                                             'D) Only counting carbons'],
                                                 'answer': 'A) Accounting for ionization at a pH',
                                                 'explanation': 'More physiologically relevant '
                                                                'sometimes.'},
                                                {'question': 'A junior colleague asks for the '
                                                             'single best answer. Suicide '
                                                             'substrate / mechanism-based '
                                                             'inhibitor? Beware of near-miss '
                                                             'distractors.',
                                                 'options': ['A) Requires enzyme activation then '
                                                             'inactivates enzyme',
                                                             'B) Only competitive reversible '
                                                             'always',
                                                             'C) Only binds albumin',
                                                             'D) Only chelates calcium in bone '
                                                             'forever'],
                                                 'answer': 'A) Requires enzyme activation then '
                                                           'inactivates enzyme',
                                                 'explanation': 'E.g., some enzyme inactivators.'},
                                                {'question': 'A junior colleague asks for the '
                                                             'single best answer. Hansch analysis '
                                                             'relates? Beware of near-miss '
                                                             'distractors.',
                                                 'options': ['A) Physicochemical parameters to '
                                                             'biological activity',
                                                             'B) Only hospital bed counts',
                                                             'C) Only nurse staffing',
                                                             'D) Only fridge temperature logs'],
                                                 'answer': 'A) Physicochemical parameters to '
                                                           'biological activity',
                                                 'explanation': 'QSAR foundations.'}],
                                       'extreme': [{'question': 'In a high-stakes pharmacy '
                                                                'scenario with incomplete data, '
                                                                'which statement is MOST correct? '
                                                                'Hard drug vs soft drug concepts? '
                                                                'Avoid actions that could harm if '
                                                                'a critical risk remains open.',
                                                    'options': ['A) Soft drugs designed for '
                                                                'predictable metabolism to '
                                                                'inactive metabolites',
                                                                'B) Soft drugs never metabolized',
                                                                'C) Hard drugs always topical only',
                                                                'D) Terms mean tablet hardness '
                                                                'only'],
                                                    'answer': 'A) Soft drugs designed for '
                                                              'predictable metabolism to inactive '
                                                              'metabolites',
                                                    'explanation': 'Safety-by-design metabolism.'},
                                                   {'question': 'In a high-stakes pharmacy '
                                                                'scenario with incomplete data, '
                                                                'which statement is MOST correct? '
                                                                'Covalent warheads in targeted '
                                                                'covalent inhibitors need? Avoid '
                                                                'actions that could harm if a '
                                                                'critical risk remains open.',
                                                    'options': ['A) Careful selectivity to limit '
                                                                'off-target binding',
                                                                'B) No selectivity concerns',
                                                                'C) Only flavoring agents',
                                                                'D) Only colorants'],
                                                    'answer': 'A) Careful selectivity to limit '
                                                              'off-target binding',
                                                    'explanation': 'Modern covalent drug design.'},
                                                   {'question': 'In a high-stakes pharmacy '
                                                                'scenario with incomplete data, '
                                                                'which statement is MOST correct? '
                                                                'PROTACs act by? Avoid actions '
                                                                'that could harm if a critical '
                                                                'risk remains open.',
                                                    'options': ['A) Hijacking degradation '
                                                                'machinery to degrade target '
                                                                'proteins',
                                                                'B) Only inhibiting kinases '
                                                                'reversibly always',
                                                                'C) Only neutralizing stomach acid',
                                                                'D) Only blocking sodium channels '
                                                                'always'],
                                                    'answer': 'A) Hijacking degradation machinery '
                                                              'to degrade target proteins',
                                                    'explanation': 'Emerging modality.'}]},
                         'cases': {'easy': [{'title': 'Why Make a Prodrug?',
                                             'stem': 'A poorly soluble drug is redesigned as an '
                                                     'ester prodrug.',
                                             'question': 'Goal theme?',
                                             'answer': 'Improve absorption/stability then release '
                                                       'active drug.',
                                             'discussion': 'Metabolic activation required.',
                                             'book_hint': "Foye's Principles of Medicinal "
                                                          'Chemistry'}],
                                   'medium': [{'title': 'Single Enantiomer Switch',
                                               'stem': 'A racemic drug is replaced by a single '
                                                       'active enantiomer product.',
                                               'question': 'Rationale?',
                                               'answer': 'Potentially more selective/predictable '
                                                         'response.',
                                               'discussion': 'Still monitor ADRs.',
                                               'book_hint': "Foye's Principles of Medicinal "
                                                            'Chemistry'}],
                                   'hard': [{'title': 'Beta-Lactamase Resistant Design',
                                             'stem': 'Chemists add bulky side chains to a '
                                                     'penicillin. Choose the safest high-yield '
                                                     'next concept before definitive results.',
                                             'question': 'Intent?',
                                             'answer': 'Steric hindrance to beta-lactamase '
                                                       'hydrolysis / spectrum modulation.',
                                             'discussion': 'Resistance still evolves.',
                                             'book_hint': "Foye's Principles of Medicinal "
                                                          'Chemistry'}],
                                   'extreme': [{'title': 'Unexpected Off-Target Toxicity',
                                                'stem': 'A covalent kinase inhibitor causes '
                                                        'unexpected organ toxicity. Avoid harmful '
                                                        'premature treatment while catastrophic '
                                                        'differentials remain open.',
                                                'question': 'Medchem concept?',
                                                'answer': 'Off-target covalent binding — redesign '
                                                          'warhead/selectivity and reassess '
                                                          'safety.',
                                                'discussion': 'Structure drives safety.',
                                                'book_hint': "Foye's Principles of Medicinal "
                                                             'Chemistry'}]}},
 'pharmacognosy': {'label': 'Pharmacognosy',
                   'books': ['Trease and Evans Pharmacognosy',
                             'Pharmacognosy texts',
                             'WHO quality control herbal themes'],
                   'pdf_notes': ['Natural ≠ always safe.',
                                 "St John's wort induces CYP enzymes.",
                                 'Standardize herbals for quality.',
                                 'Watch adulteration with undeclared drugs.',
                                 'Report suspected herbal ADRs.'],
                   'questions': {'easy': [{'question': 'Pharmacognosy studies?',
                                           'options': ['A) Medicines from natural sources',
                                                       'B) Only synthetic polymers forever',
                                                       'C) Only hospital billing',
                                                       'D) Only IV pump brands'],
                                           'answer': 'A) Medicines from natural sources',
                                           'explanation': 'Plants/microbes/marine etc.'},
                                          {'question': 'Digitalis historically relates to?',
                                           'options': ['A) Cardiac glycosides',
                                                       'B) Only antibiotics',
                                                       'C) Only local anesthetics',
                                                       'D) Only vitamins'],
                                           'answer': 'A) Cardiac glycosides',
                                           'explanation': 'Classic natural product.'},
                                          {'question': 'Alkaloids are typically?',
                                           'options': ['A) Nitrogen-containing natural bases',
                                                       'B) Only sugars',
                                                       'C) Only fats',
                                                       'D) Only inorganic salts'],
                                           'answer': 'A) Nitrogen-containing natural bases',
                                           'explanation': 'Many bioactive plant compounds.'}],
                                 'medium': [{'question': "St John's wort interaction theme?",
                                             'options': ['A) CYP induction reducing many drug '
                                                         'levels',
                                                         'B) No interactions ever',
                                                         'C) Only increases all drug levels always',
                                                         'D) Only affects tooth shade'],
                                             'answer': 'A) CYP induction reducing many drug levels',
                                             'explanation': 'Notably oral '
                                                            'contraceptives/transplant drugs '
                                                            'themes.'},
                                            {'question': 'Secondary metabolites serve plants often '
                                                         'as?',
                                             'options': ['A) Defense/attraction chemicals; humans '
                                                         'use as drugs',
                                                         'B) Only structural cellulose identical '
                                                         'always',
                                                         'C) Only water storage',
                                                         'D) Only chlorophyll always'],
                                             'answer': 'A) Defense/attraction chemicals; humans '
                                                       'use as drugs',
                                             'explanation': 'Alkaloids, terpenoids, phenolics.'},
                                            {'question': 'Standardization of herbal drugs aims to?',
                                             'options': ['A) Consistent content of marker/active '
                                                         'constituents',
                                                         'B) Random batch variability as a goal',
                                                         'C) Remove all labeling',
                                                         'D) Avoid quality tests'],
                                             'answer': 'A) Consistent content of marker/active '
                                                       'constituents',
                                             'explanation': 'Quality assurance.'}],
                                 'hard': [{'question': 'A junior colleague asks for the single '
                                                       'best answer. Microbial natural products '
                                                       'gave us many? Beware of near-miss '
                                                       'distractors.',
                                           'options': ['A) Antibiotics',
                                                       'B) Only toothpastes',
                                                       'C) Only sutures',
                                                       'D) Only gloves'],
                                           'answer': 'A) Antibiotics',
                                           'explanation': 'Penicillin onward.'},
                                          {'question': 'A junior colleague asks for the single '
                                                       'best answer. Adulteration of herbal '
                                                       'products may involve? Beware of near-miss '
                                                       'distractors.',
                                           'options': ['A) Wrong species / heavy metals / '
                                                       'undeclared drugs',
                                                       'B) Only better purity always',
                                                       'C) Only extra water always safe',
                                                       'D) Only nicer bottles'],
                                           'answer': 'A) Wrong species / heavy metals / undeclared '
                                                     'drugs',
                                           'explanation': 'Patient harm risk.'},
                                          {'question': 'A junior colleague asks for the single '
                                                       'best answer. Phytochemical screening tests '
                                                       'detect classes like? Beware of near-miss '
                                                       'distractors.',
                                           'options': ['A) Alkaloids, flavonoids, saponins, etc.',
                                                       'B) Only blood type',
                                                       'C) Only HLA',
                                                       'D) Only INR'],
                                           'answer': 'A) Alkaloids, flavonoids, saponins, etc.',
                                           'explanation': 'Preliminary characterization.'}],
                                 'extreme': [{'question': 'In a high-stakes pharmacy scenario with '
                                                          'incomplete data, which statement is '
                                                          'MOST correct? Aristolochic acid '
                                                          'concern? Avoid actions that could harm '
                                                          'if a critical risk remains open.',
                                              'options': ['A) Nephrotoxicity/carcinogenicity in '
                                                          'some botanicals',
                                                          'B) Completely harmless vitamin',
                                                          'C) Only a binder excipient always safe',
                                                          'D) Only a flavor'],
                                              'answer': 'A) Nephrotoxicity/carcinogenicity in some '
                                                        'botanicals',
                                              'explanation': 'Regulatory bans/warnings.'},
                                             {'question': 'In a high-stakes pharmacy scenario with '
                                                          'incomplete data, which statement is '
                                                          'MOST correct? Aflatoxins in crude drugs '
                                                          'are? Avoid actions that could harm if a '
                                                          'critical risk remains open.',
                                              'options': ['A) Fungal toxins; contamination risk',
                                                          'B) Desired active alkaloids always',
                                                          'C) Only pigments',
                                                          'D) Only sugars'],
                                              'answer': 'A) Fungal toxins; contamination risk',
                                              'explanation': 'Quality control critical.'},
                                             {'question': 'In a high-stakes pharmacy scenario with '
                                                          'incomplete data, which statement is '
                                                          'MOST correct? Ethnopharmacology '
                                                          'contributes by? Avoid actions that '
                                                          'could harm if a critical risk remains '
                                                          'open.',
                                              'options': ['A) Studying traditional use to guide '
                                                          'discovery',
                                                          'B) Ignoring traditional knowledge '
                                                          'always',
                                                          'C) Only renaming brands',
                                                          'D) Only counting prescriptions'],
                                              'answer': 'A) Studying traditional use to guide '
                                                        'discovery',
                                              'explanation': 'Still needs scientific '
                                                             'validation.'}]},
                   'cases': {'easy': [{'title': 'Herbal Product Question',
                                       'stem': "A patient asks if 'natural' means always safe.",
                                       'question': 'Answer theme?',
                                       'answer': 'Natural ≠ harmless; interactions and variability '
                                                 'exist.',
                                       'discussion': 'Counsel evidence and quality.',
                                       'book_hint': 'Trease and Evans Pharmacognosy'}],
                             'medium': [{'title': 'Transplant Patient on Herbals',
                                         'stem': "A transplant patient starts St John's wort; "
                                                 'tacrolimus levels drop.',
                                         'question': 'Mechanism?',
                                         'answer': 'Induction interaction — stop herbal and manage '
                                                   'levels.',
                                         'discussion': 'Ask about OTCs/herbals always.',
                                         'book_hint': 'Trease and Evans Pharmacognosy'}],
                             'hard': [{'title': "Undeclared Sildenafil in 'Herbal' Capsule",
                                       'stem': 'A man develops severe hypotension after an '
                                               "'herbal' sexual enhancer with nitrate therapy. "
                                               'Choose the safest high-yield next concept before '
                                               'definitive results.',
                                       'question': 'Issue?',
                                       'answer': 'Adulteration with PDE5 inhibitor — dangerous '
                                                 'interaction.',
                                       'discussion': 'Report and counsel.',
                                       'book_hint': 'Trease and Evans Pharmacognosy'}],
                             'extreme': [{'title': 'Herbal Nephropathy Outbreak',
                                          'stem': 'Several patients using a weight-loss herb '
                                                  'develop renal failure; aristolochic acid '
                                                  'detected. Avoid harmful premature treatment '
                                                  'while catastrophic differentials remain open.',
                                          'question': 'Pharmacy role?',
                                          'answer': 'Identify product, stop exposure, report to '
                                                    'authorities, support clinical care.',
                                          'discussion': 'Pharmacovigilance for naturals.',
                                          'book_hint': 'Trease and Evans Pharmacognosy'}]}},
 'pharmacy_practice': {'label': 'Pharmacy Practice',
                       'books': ['Community Pharmacy — Rutter',
                                 'Pharmacy Practice texts',
                                 'Local professional standards/guidance'],
                       'pdf_notes': ['Check legal and clinical validity of prescriptions.',
                                     'OTC: know referral red flags.',
                                     'Protect confidentiality.',
                                     'Report near misses to improve systems.',
                                     'Controlled drugs have extra legal duties.'],
                       'questions': {'easy': [{'question': 'Prescription validity checks include?',
                                               'options': ['A) Patient, drug, dose, route, '
                                                           'frequency, prescriber details',
                                                           'B) Only paper color',
                                                           'C) Only stamp ink brand',
                                                           'D) Only font size'],
                                               'answer': 'A) Patient, drug, dose, route, '
                                                         'frequency, prescriber details',
                                               'explanation': 'Legal/clinical screen.'},
                                              {'question': 'OTC counseling should cover?',
                                               'options': ['A) Indication limits, dose, warnings, '
                                                           'when to refer',
                                                           'B) Sell anything without questions '
                                                           'always',
                                                           'C) Never ask about other meds',
                                                           'D) Hide side effects always'],
                                               'answer': 'A) Indication limits, dose, warnings, '
                                                         'when to refer',
                                               'explanation': 'Responsible self-care.'},
                                              {'question': 'Controlled drugs require?',
                                               'options': ['A) Extra legal storage/record controls '
                                                           'per law',
                                                           'B) No special rules ever',
                                                           'C) Open shelf always',
                                                           'D) Patient self-dispense from back'],
                                               'answer': 'A) Extra legal storage/record controls '
                                                         'per law',
                                               'explanation': 'Follow local law.'}],
                                     'medium': [{'question': 'Near miss reporting helps?',
                                                 'options': ['A) System learning without waiting '
                                                             'for harm',
                                                             'B) Punish staff only',
                                                             'C) Hide errors',
                                                             'D) Increase sales only'],
                                                 'answer': 'A) System learning without waiting for '
                                                           'harm',
                                                 'explanation': 'Safety culture.'},
                                                {'question': 'Generic substitution depends on?',
                                                 'options': ['A) Local law/formulary and clinical '
                                                             'appropriateness',
                                                             'B) Always automatic for all narrow '
                                                             'TI drugs blindly',
                                                             'C) Never allowed anywhere',
                                                             'D) Only patient hair color'],
                                                 'answer': 'A) Local law/formulary and clinical '
                                                           'appropriateness',
                                                 'explanation': 'Caution with critical-dose '
                                                                'drugs.'},
                                                {'question': 'Privacy in pharmacy means?',
                                                 'options': ['A) Protect patient confidential '
                                                             'information',
                                                             'B) Discuss therapy loudly in aisle '
                                                             'always',
                                                             'C) Post prescriptions online',
                                                             'D) Share with friends'],
                                                 'answer': 'A) Protect patient confidential '
                                                           'information',
                                                 'explanation': 'Ethics + law.'}],
                                     'hard': [{'question': 'A junior colleague asks for the single '
                                                           'best answer. Emergency supply '
                                                           'frameworks (where legal) require? '
                                                           'Beware of near-miss distractors.',
                                               'options': ['A) Professional judgment + legal '
                                                           'criteria + documentation',
                                                           'B) Unlimited controlled drugs always',
                                                           'C) No records',
                                                           'D) Ignoring care continuity'],
                                               'answer': 'A) Professional judgment + legal '
                                                         'criteria + documentation',
                                               'explanation': 'Jurisdiction-specific.'},
                                              {'question': 'A junior colleague asks for the single '
                                                           'best answer. Antimicrobial stewardship '
                                                           'in community includes? Beware of '
                                                           'near-miss distractors.',
                                               'options': ['A) Avoid unnecessary antibiotics; '
                                                           'counsel adherence; refer appropriately',
                                                           'B) Always give leftover antibiotics',
                                                           'C) Encourage sharing antibiotics',
                                                           'D) Ignore allergy history'],
                                               'answer': 'A) Avoid unnecessary antibiotics; '
                                                         'counsel adherence; refer appropriately',
                                               'explanation': 'Resistance threat.'},
                                              {'question': 'A junior colleague asks for the single '
                                                           'best answer. Health promotion role '
                                                           'example? Beware of near-miss '
                                                           'distractors.',
                                               'options': ['A) Smoking cessation support',
                                                           'B) Only selling candy at checkout as '
                                                           'clinical care',
                                                           'C) Avoiding all public health talk',
                                                           'D) Only counting tablets silently'],
                                               'answer': 'A) Smoking cessation support',
                                               'explanation': 'Public health pharmacy.'}],
                                     'extreme': [{'question': 'In a high-stakes pharmacy scenario '
                                                              'with incomplete data, which '
                                                              'statement is MOST correct? '
                                                              'Suspected forged CD prescription? '
                                                              'Avoid actions that could harm if a '
                                                              'critical risk remains open.',
                                                  'options': ['A) Do not dispense; verify/report '
                                                              'per legal pathway',
                                                              'B) Dispense quickly to avoid '
                                                              'conflict',
                                                              'C) Ignore discrepancies',
                                                              'D) Alter the prescription yourself'],
                                                  'answer': 'A) Do not dispense; verify/report per '
                                                            'legal pathway',
                                                  'explanation': 'Controlled drug diversion risk.'},
                                                 {'question': 'In a high-stakes pharmacy scenario '
                                                              'with incomplete data, which '
                                                              'statement is MOST correct? Child '
                                                              'dosing error risk mitigation? Avoid '
                                                              'actions that could harm if a '
                                                              'critical risk remains open.',
                                                  'options': ['A) mg/kg checks, max dose caps, '
                                                              'independent double check when '
                                                              'required',
                                                              'B) Estimate by age appearance only',
                                                              'C) Use adult dose halved always',
                                                              'D) Avoid weighing'],
                                                  'answer': 'A) mg/kg checks, max dose caps, '
                                                            'independent double check when '
                                                            'required',
                                                  'explanation': 'Pediatrics is high-risk.'},
                                                 {'question': 'In a high-stakes pharmacy scenario '
                                                              'with incomplete data, which '
                                                              'statement is MOST correct? Vaccine '
                                                              'fridge excursion requires? Avoid '
                                                              'actions that could harm if a '
                                                              'critical risk remains open.',
                                                  'options': ['A) Quarantine stock and follow '
                                                              'cold-chain protocol before use',
                                                              'B) Use anyway silently',
                                                              'C) Freeze then thaw repeatedly',
                                                              'D) Discard documentation'],
                                                  'answer': 'A) Quarantine stock and follow '
                                                            'cold-chain protocol before use',
                                                  'explanation': 'Potency/safety.'}]},
                       'cases': {'easy': [{'title': 'OTC Request for Persistent Cough',
                                           'stem': 'Adult wants cough syrup for 4 weeks of cough '
                                                   'with weight loss.',
                                           'question': 'Action?',
                                           'answer': 'Refer — red flags, not simple OTC.',
                                           'discussion': 'Do not mask serious disease.',
                                           'book_hint': 'Community Pharmacy Practice texts / RPS '
                                                        'guidance themes'}],
                                 'medium': [{'title': 'Wrong Strength Almost Dispensed',
                                             'stem': 'Technician selects 100 mg instead of 10 mg; '
                                                     'pharmacist catches it.',
                                             'question': 'Next?',
                                             'answer': 'Correct, document near miss, review '
                                                       'look-alike storage.',
                                             'discussion': 'High-alert drugs need safeguards.',
                                             'book_hint': 'Community Pharmacy Practice texts / RPS '
                                                          'guidance themes'}],
                                 'hard': [{'title': "Request for Neighbor's Antibiotic",
                                           'stem': 'Someone asks for amoxicillin for a neighbor '
                                                   'without prescription. Choose the safest '
                                                   'high-yield next concept before definitive '
                                                   'results.',
                                           'question': 'Correct approach?',
                                           'answer': 'Do not supply illegally; explain and advise '
                                                     'appropriate care pathway.',
                                           'discussion': 'Legal + ethical boundary.',
                                           'book_hint': 'Community Pharmacy Practice texts / RPS '
                                                        'guidance themes'}],
                                 'extreme': [{'title': 'Opioid Prescription Red Flags',
                                              'stem': 'A cash-paying out-of-area patient presents '
                                                      'multiple early opioid requests with '
                                                      'inconsistent stories. Avoid harmful '
                                                      'premature treatment while catastrophic '
                                                      'differentials remain open.',
                                              'question': 'Response concept?',
                                              'answer': 'Professional vigilance for '
                                                        'diversion/misuse — verify, refuse when '
                                                        'appropriate, follow controlled-drug and '
                                                        'safeguarding pathways.',
                                              'discussion': 'Patient care + legal duties.',
                                              'book_hint': 'Community Pharmacy Practice texts / '
                                                           'RPS guidance themes'}]}},
 'hospital_pharmacy': {'label': 'Hospital Pharmacy',
                       'books': ['Hospital Pharmacy practice handbooks',
                                 'ASHP guidelines themes',
                                 'Injectable Drug Information references'],
                       'pdf_notes': ['Aseptic compounding and validation.',
                                     'Formulary + stewardship improve use.',
                                     'High-alert storage and labeling.',
                                     'Recalls need rapid quarantine/trace.',
                                     'Never-event barriers for intrathecal risks.'],
                       'questions': {'easy': [{'question': 'Unit dose systems aim to?',
                                               'options': ['A) Reduce medication errors and waste',
                                                           'B) Increase unlabeled bulk always',
                                                           'C) Remove pharmacist review',
                                                           'D) Hide drug names'],
                                               'answer': 'A) Reduce medication errors and waste',
                                               'explanation': 'Safer distribution.'},
                                              {'question': 'IV admixture service focuses on?',
                                               'options': ['A) Aseptic compounding of injectables',
                                                           'B) Only counting oral tablets',
                                                           'C) Only shelf dusting',
                                                           'D) Only outpatient retail candy'],
                                               'answer': 'A) Aseptic compounding of injectables',
                                               'explanation': 'Contamination prevention.'},
                                              {'question': 'Formulary manages?',
                                               'options': ['A) Which medicines are '
                                                           'stocked/approved for use',
                                                           'B) Only staff rotas',
                                                           'C) Only parking permits',
                                                           'D) Only cafeteria menus'],
                                               'answer': 'A) Which medicines are stocked/approved '
                                                         'for use',
                                               'explanation': 'Evidence + cost + safety.'}],
                                     'medium': [{'question': 'TPN compounding requires?',
                                                 'options': ['A) Aseptic technique + '
                                                             'stability/compatibility checks',
                                                             'B) Open-bench mixing without asepsis',
                                                             'C) No labeling',
                                                             'D) Patient self-mix at bedside '
                                                             'without training'],
                                                 'answer': 'A) Aseptic technique + '
                                                           'stability/compatibility checks',
                                                 'explanation': 'Complex admixtures.'},
                                                {'question': 'Antimicrobial stewardship rounds '
                                                             'include pharmacists to?',
                                                 'options': ['A) Optimize choice/dose/duration',
                                                             'B) Prolong all courses indefinitely',
                                                             'C) Ignore cultures',
                                                             'D) Avoid de-escalation always'],
                                                 'answer': 'A) Optimize choice/dose/duration',
                                                 'explanation': 'Better outcomes + less '
                                                                'resistance.'},
                                                {'question': 'Medication error disclosure ethics?',
                                                 'options': ['A) Be honest with patient/team per '
                                                             'policy',
                                                             'B) Hide always',
                                                             'C) Blame only juniors publicly',
                                                             'D) Alter charts secretly'],
                                                 'answer': 'A) Be honest with patient/team per '
                                                           'policy',
                                                 'explanation': 'Safety culture.'}],
                                     'hard': [{'question': 'A junior colleague asks for the single '
                                                           'best answer. Clean room grades/air '
                                                           'quality matter for? Beware of '
                                                           'near-miss distractors.',
                                               'options': ['A) Aseptic preparation risk control',
                                                           'B) Only office printing',
                                                           'C) Only waiting room TV',
                                                           'D) Only outpatient counseling desks'],
                                               'answer': 'A) Aseptic preparation risk control',
                                               'explanation': 'GMP concepts.'},
                                              {'question': 'A junior colleague asks for the single '
                                                           'best answer. Smart pump libraries '
                                                           'reduce? Beware of near-miss '
                                                           'distractors.',
                                               'options': ['A) Infusion programming errors',
                                                           'B) Need for any training ever',
                                                           'C) All ADRs magically',
                                                           'D) Labeling requirements'],
                                               'answer': 'A) Infusion programming errors',
                                               'explanation': 'Technology + processes.'},
                                              {'question': 'A junior colleague asks for the single '
                                                           'best answer. Recall management '
                                                           'requires? Beware of near-miss '
                                                           'distractors.',
                                               'options': ['A) Quarantine affected batches and '
                                                           'trace patients if needed',
                                                           'B) Continue using recalled lot',
                                                           'C) Delete records',
                                                           'D) Ignore notices'],
                                               'answer': 'A) Quarantine affected batches and trace '
                                                         'patients if needed',
                                               'explanation': 'Pharmacovigilance operations.'}],
                                     'extreme': [{'question': 'In a high-stakes pharmacy scenario '
                                                              'with incomplete data, which '
                                                              'statement is MOST correct? '
                                                              'Intrathecal vincristine error '
                                                              'prevention? Avoid actions that '
                                                              'could harm if a critical risk '
                                                              'remains open.',
                                                  'options': ['A) Never dispense IV vinca in same '
                                                              'way as IT meds; systemic safeguards',
                                                              'B) Store vincristine with IT sets',
                                                              'C) Allow syringe interchange freely',
                                                              'D) No special warnings needed'],
                                                  'answer': 'A) Never dispense IV vinca in same '
                                                            'way as IT meds; systemic safeguards',
                                                  'explanation': 'Never event.'},
                                                 {'question': 'In a high-stakes pharmacy scenario '
                                                              'with incomplete data, which '
                                                              'statement is MOST correct? Disaster '
                                                              'formulary planning includes? Avoid '
                                                              'actions that could harm if a '
                                                              'critical risk remains open.',
                                                  'options': ['A) Critical meds continuity and '
                                                              'cold chain contingency',
                                                              'B) Only elective cosmetics',
                                                              'C) Stopping all chronic meds '
                                                              'abruptly without plan',
                                                              'D) No documentation'],
                                                  'answer': 'A) Critical meds continuity and cold '
                                                            'chain contingency',
                                                  'explanation': 'Resilience.'},
                                                 {'question': 'In a high-stakes pharmacy scenario '
                                                              'with incomplete data, which '
                                                              'statement is MOST correct? '
                                                              'Cytotoxic spill response? Avoid '
                                                              'actions that could harm if a '
                                                              'critical risk remains open.',
                                                  'options': ['A) Evacuate/protect, use spill kit, '
                                                              'report, follow hazardous drug '
                                                              'protocol',
                                                              'B) Wipe with bare hands',
                                                              'C) Ignore',
                                                              'D) Pour more chemo on floor'],
                                                  'answer': 'A) Evacuate/protect, use spill kit, '
                                                            'report, follow hazardous drug '
                                                            'protocol',
                                                  'explanation': 'Occupational safety.'}]},
                       'cases': {'easy': [{'title': 'Ward Stock Look-Alike',
                                           'stem': 'Two vials look similar; wrong concentrated '
                                                   'electrolyte almost selected.',
                                           'question': 'System fix theme?',
                                           'answer': 'Separate storage, warnings, '
                                                     'ready-to-administer formats, independent '
                                                     'checks.',
                                           'discussion': 'High-alert meds.',
                                           'book_hint': 'Hospital Pharmacy practice / ASHP '
                                                        'themes'}],
                                 'medium': [{'title': 'Culture Results Ignore Broad Therapy',
                                             'stem': 'Patient remains on broad IV antibiotics '
                                                     'despite sensitivities allowing narrow agent.',
                                             'question': 'Pharmacy action?',
                                             'answer': 'Recommend de-escalation with team.',
                                             'discussion': 'Stewardship in action.',
                                             'book_hint': 'Hospital Pharmacy practice / ASHP '
                                                          'themes'}],
                                 'hard': [{'title': 'Batch Recall Mid-Shift',
                                           'stem': 'Urgent recall for a contaminated injectable '
                                                   'batch currently on wards. Choose the safest '
                                                   'high-yield next concept before definitive '
                                                   'results.',
                                           'question': 'Steps?',
                                           'answer': 'Stop use, quarantine, identify exposed '
                                                     'patients, coordinate clinical follow-up, '
                                                     'document.',
                                           'discussion': 'Speed + traceability.',
                                           'book_hint': 'Hospital Pharmacy practice / ASHP '
                                                        'themes'}],
                                 'extreme': [{'title': 'Vinca Near Intrathecal Tray',
                                              'stem': 'A vinca alkaloid syringe is found placed '
                                                      'with intrathecal medications. Avoid harmful '
                                                      'premature treatment while catastrophic '
                                                      'differentials remain open.',
                                              'question': 'Immediate actions?',
                                              'answer': 'Do not administer; quarantine; '
                                                        'root-cause; enforce never-event barriers '
                                                        '(different delivery '
                                                        'systems/times/places).',
                                              'discussion': 'Fatal if given IT.',
                                              'book_hint': 'Hospital Pharmacy practice / ASHP '
                                                           'themes'}]}},
 'toxicology': {'label': 'Toxicology',
                'books': ["Goldfrank's Toxicologic Emergencies",
                          "Casarett & Doull's Toxicology",
                          'Local poison center protocols'],
                'pdf_notes': ['ABCs before antidotes.',
                              'Naloxone for opioids; NAC for paracetamol.',
                              'Charcoal only if appropriate and airway safe.',
                              'TCA toxicity: wide QRS — bicarbonate themes.',
                              'Call poison information services early.'],
                'questions': {'easy': [{'question': 'Antidote concept example: naloxone for?',
                                        'options': ['A) Opioid toxicity',
                                                    'B) Only benzodiazepines always',
                                                    'C) Only beta-blocker only',
                                                    'D) Only cyanide only'],
                                        'answer': 'A) Opioid toxicity',
                                        'explanation': 'Supportive care still primary.'},
                                       {'question': 'Activated charcoal useful when?',
                                        'options': ['A) Selected recent ingestions if airway '
                                                    'protected',
                                                    'B) Always in all poisonings including metals '
                                                    'always best',
                                                    'C) Corrosives as first choice always',
                                                    'D) Unconscious without airway always safe'],
                                        'answer': 'A) Selected recent ingestions if airway '
                                                  'protected',
                                        'explanation': 'Contraindications exist.'},
                                       {'question': 'ABC approach in poisoning means?',
                                        'options': ['A) Airway Breathing Circulation first',
                                                    'B) Always give antidote before ABCs',
                                                    'C) Only call family first',
                                                    'D) Only wait for labs forever'],
                                        'answer': 'A) Airway Breathing Circulation first',
                                        'explanation': 'Resuscitation priority.'}],
                              'medium': [{'question': 'Paracetamol toxicity antidote?',
                                          'options': ['A) N-acetylcysteine',
                                                      'B) Naloxone',
                                                      'C) Flumazenil routinely first',
                                                      'D) Digoxin Fab always'],
                                          'answer': 'A) N-acetylcysteine',
                                          'explanation': 'Time-critical after significant '
                                                         'overdose.'},
                                         {'question': 'Methanol toxicity visual threat treated '
                                                      'with?',
                                          'options': ['A) Fomepizole/ethanol ± dialysis pathways',
                                                      'B) Only vitamin C',
                                                      'C) Only charcoal always curative',
                                                      'D) Only antibiotics'],
                                          'answer': 'A) Fomepizole/ethanol ± dialysis pathways',
                                          'explanation': 'Block alcohol dehydrogenase.'},
                                         {'question': 'Tricyclic antidepressant overdose ECG clue?',
                                          'options': ['A) Wide QRS / sodium channel block themes',
                                                      'B) Only short PR always benign',
                                                      'C) Only peaked T of hyperK always only '
                                                      'cause',
                                                      'D) Normal ECG excludes severe toxicity '
                                                      'always'],
                                          'answer': 'A) Wide QRS / sodium channel block themes',
                                          'explanation': 'Sodium bicarbonate therapy themes.'}],
                              'hard': [{'question': 'A junior colleague asks for the single best '
                                                    'answer. Physostigmine sometimes considered '
                                                    'in? Beware of near-miss distractors.',
                                        'options': ['A) Severe anticholinergic delirium (selected '
                                                    'cases)',
                                                    'B) All overdoses blindly',
                                                    'C) Opioid coma first-line',
                                                    'D) Cyanide as sole antidote'],
                                        'answer': 'A) Severe anticholinergic delirium (selected '
                                                  'cases)',
                                        'explanation': 'Expert use only.'},
                                       {'question': 'A junior colleague asks for the single best '
                                                    'answer. Hydrofluoric acid burn systemic risk? '
                                                    'Beware of near-miss distractors.',
                                        'options': ['A) Hypocalcemia',
                                                    'B) Only hypernatremia always',
                                                    'C) Only hyperglycemia only',
                                                    'D) Only polycythemia'],
                                        'answer': 'A) Hypocalcemia',
                                        'explanation': 'Calcium therapy important.'},
                                       {'question': 'A junior colleague asks for the single best '
                                                    'answer. Body packer rupture risk management? '
                                                    'Beware of near-miss distractors.',
                                        'options': ['A) Urgent surgical/toxicology pathways; avoid '
                                                    'unsafe endoscopy themes',
                                                    'B) Discharge immediately',
                                                    'C) Give charcoal only and send home',
                                                    'D) Ignore packets'],
                                        'answer': 'A) Urgent surgical/toxicology pathways; avoid '
                                                  'unsafe endoscopy themes',
                                        'explanation': 'Life-threatening.'}],
                              'extreme': [{'question': 'In a high-stakes pharmacy scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Cyanide antidote kits may '
                                                       'include? Avoid actions that could harm if '
                                                       'a critical risk remains open.',
                                           'options': ['A) Hydroxocobalamin (and other protocol '
                                                       'options)',
                                                       'B) Only naloxone',
                                                       'C) Only charcoal',
                                                       'D) Only insulin always'],
                                           'answer': 'A) Hydroxocobalamin (and other protocol '
                                                     'options)',
                                           'explanation': 'Smoke inhalation contexts.'},
                                          {'question': 'In a high-stakes pharmacy scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Serotonin syndrome vs NMS '
                                                       'distinction matters because? Avoid actions '
                                                       'that could harm if a critical risk remains '
                                                       'open.',
                                           'options': ['A) Different triggers and management '
                                                       'nuances',
                                                       'B) Identical always in cause and drugs',
                                                       'C) Neither is dangerous',
                                                       'D) Only skin color differs'],
                                           'answer': 'A) Different triggers and management nuances',
                                           'explanation': 'Tox vs neuroleptic pathways.'},
                                          {'question': 'In a high-stakes pharmacy scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Extracorporeal removal considered '
                                                       'for? Avoid actions that could harm if a '
                                                       'critical risk remains open.',
                                           'options': ['A) Selected dialyzable toxins with severe '
                                                       'toxicity',
                                                       'B) All poisonings always',
                                                       'C) Only topical exposures',
                                                       'D) Never useful'],
                                           'answer': 'A) Selected dialyzable toxins with severe '
                                                     'toxicity',
                                           'explanation': 'EXTRIP guidance themes.'}]},
                'cases': {'easy': [{'title': 'Pinpoint Pupils + Bradypnea',
                                    'stem': 'Unresponsive patient with pinpoint pupils and slow '
                                            'breathing; empty opioid bottles nearby.',
                                    'question': 'First steps + antidote theme?',
                                    'answer': 'Support ventilation and give naloxone per protocol.',
                                    'discussion': 'Watch for renarcotization.',
                                    'book_hint': "Goldfrank's Toxicologic Emergencies themes / "
                                                 'Casarett & Doull'}],
                          'medium': [{'title': 'Paracetamol Overdose 8 Hours Ago',
                                      'stem': 'Staggered paracetamol overdose; levels timing '
                                              'complex.',
                                      'question': 'Concept?',
                                      'answer': 'Do not delay NAC when significant risk; follow '
                                                'toxicology protocol.',
                                      'discussion': 'Staggered ingestions are tricky.',
                                      'book_hint': "Goldfrank's Toxicologic Emergencies themes / "
                                                   'Casarett & Doull'}],
                          'hard': [{'title': 'Wide-Complex Tachycardia After TCA',
                                    'stem': 'Overdose patient has wide QRS and hypotension. Choose '
                                            'the safest high-yield next concept before definitive '
                                            'results.',
                                    'question': 'Therapy theme?',
                                    'answer': 'Sodium bicarbonate for TCA sodium-channel toxicity '
                                              'per ACLS/tox guidance.',
                                    'discussion': 'Avoid class Ia/Ic empiric habits.',
                                    'book_hint': "Goldfrank's Toxicologic Emergencies themes / "
                                                 'Casarett & Doull'}],
                          'extreme': [{'title': 'Smoke Inhalation Collapse',
                                       'stem': 'Fire victim with soot, lactic acidosis, and coma; '
                                               'CO treated but remains severely acidotic. Avoid '
                                               'harmful premature treatment while catastrophic '
                                               'differentials remain open.',
                                       'question': 'Consider?',
                                       'answer': 'Cyanide toxicity — protocol antidotes + '
                                                 'supportive care.',
                                       'discussion': 'Do not miss dual toxicity.',
                                       'book_hint': "Goldfrank's Toxicologic Emergencies themes / "
                                                    'Casarett & Doull'}]}},
 'pharm_microbiology': {'label': 'Pharmaceutical Microbiology',
                        'books': ["Hugo and Russell's Pharmaceutical Microbiology",
                                  'Pharmaceutical Microbiology texts',
                                  'GMP microbiology guidance'],
                        'pdf_notes': ['Sterility vs disinfection vs sanitation.',
                                      'Endotoxin from Gram-negatives — pyrogen risk.',
                                      'Autoclave validation with biological indicators.',
                                      'Cleanroom environmental monitoring.',
                                      'Media fills test aseptic process capability.'],
                        'questions': {'easy': [{'question': 'Sterilization means?',
                                                'options': ['A) Killing/removal of all viable '
                                                            'microorganisms including spores '
                                                            '(process dependent)',
                                                            'B) Only reducing dust',
                                                            'C) Only washing with water',
                                                            'D) Only cooling a fridge'],
                                                'answer': 'A) Killing/removal of all viable '
                                                          'microorganisms including spores '
                                                          '(process dependent)',
                                                'explanation': 'Critical for injectables.'},
                                               {'question': 'Gram-positive bacteria stain?',
                                                'options': ['A) Purple/blue in Gram stain',
                                                            'B) Always red only',
                                                            'C) Always invisible',
                                                            'D) Always acid-fast only'],
                                                'answer': 'A) Purple/blue in Gram stain',
                                                'explanation': 'Cell wall differences.'},
                                               {'question': 'Disinfection differs from '
                                                            'sterilization by?',
                                                'options': ['A) Reducing microbes on '
                                                            'surfaces/objects but not necessarily '
                                                            'sterilizing',
                                                            'B) Being identical always',
                                                            'C) Only applying to air fragrance',
                                                            'D) Only tablet coating'],
                                                'answer': 'A) Reducing microbes on '
                                                          'surfaces/objects but not necessarily '
                                                          'sterilizing',
                                                'explanation': 'Choose agent appropriately.'}],
                                      'medium': [{'question': 'Endotoxin (LPS) risk is mainly '
                                                              'from?',
                                                  'options': ['A) Gram-negative bacteria',
                                                              'B) Only viruses',
                                                              'C) Only fungi always',
                                                              'D) Only prions only'],
                                                  'answer': 'A) Gram-negative bacteria',
                                                  'explanation': 'Pyrogen tests/LAL themes.'},
                                                 {'question': 'Autoclaving typical condition '
                                                              'theme?',
                                                  'options': ['A) Moist heat under pressure (e.g., '
                                                              '121°C themes)',
                                                              'B) Only dry room temperature '
                                                              'overnight',
                                                              'C) Only UV phone lights',
                                                              'D) Only alcohol wipe of closed '
                                                              'vials always sterilizes insides'],
                                                  'answer': 'A) Moist heat under pressure (e.g., '
                                                            '121°C themes)',
                                                  'explanation': 'Validated cycles.'},
                                                 {'question': 'Preservatives in multi-dose vials '
                                                              'help?',
                                                  'options': ['A) Inhibit microbial growth after '
                                                              'opening',
                                                              'B) Sterilize terminal spores always '
                                                              'alone',
                                                              'C) Replace need for aseptic '
                                                              'technique',
                                                              'D) Make drugs sweeter only'],
                                                  'answer': 'A) Inhibit microbial growth after '
                                                            'opening',
                                                  'explanation': 'Still use aseptic handling.'}],
                                      'hard': [{'question': 'A junior colleague asks for the '
                                                            'single best answer. HEPA filters in '
                                                            'cleanrooms remove? Beware of '
                                                            'near-miss distractors.',
                                                'options': ['A) Airborne particles/microbes to '
                                                            'specified efficiency',
                                                            'B) Only odors forever',
                                                            'C) Only CO2',
                                                            'D) Only humidity'],
                                                'answer': 'A) Airborne particles/microbes to '
                                                          'specified efficiency',
                                                'explanation': 'Environmental control.'},
                                               {'question': 'A junior colleague asks for the '
                                                            'single best answer. Biological '
                                                            'indicator for autoclave often uses? '
                                                            'Beware of near-miss distractors.',
                                                'options': ['A) Geobacillus stearothermophilus '
                                                            'spores',
                                                            'B) Only E. coli always',
                                                            'C) Only influenza',
                                                            'D) Only Candida only'],
                                                'answer': 'A) Geobacillus stearothermophilus '
                                                          'spores',
                                                'explanation': 'Validate sterilization.'},
                                               {'question': 'A junior colleague asks for the '
                                                            'single best answer. Biofilm on '
                                                            'equipment causes? Beware of near-miss '
                                                            'distractors.',
                                                'options': ['A) Persistent contamination hard to '
                                                            'eradicate',
                                                            'B) Better sterility always',
                                                            'C) No cleaning needed',
                                                            'D) Only nicer smell'],
                                                'answer': 'A) Persistent contamination hard to '
                                                          'eradicate',
                                                'explanation': 'Cleaning validation matters.'}],
                                      'extreme': [{'question': 'In a high-stakes pharmacy scenario '
                                                               'with incomplete data, which '
                                                               'statement is MOST correct? Aseptic '
                                                               'process simulation (media fill) '
                                                               'demonstrates? Avoid actions that '
                                                               'could harm if a critical risk '
                                                               'remains open.',
                                                   'options': ['A) Operator/process capability to '
                                                               'maintain sterility',
                                                               'B) Only tablet hardness',
                                                               'C) Only marketing claims',
                                                               'D) Only shipping speed'],
                                                   'answer': 'A) Operator/process capability to '
                                                             'maintain sterility',
                                                   'explanation': 'GMP expectation.'},
                                                  {'question': 'In a high-stakes pharmacy scenario '
                                                               'with incomplete data, which '
                                                               'statement is MOST correct? '
                                                               'Mycoplasma contamination is '
                                                               'problematic in? Avoid actions that '
                                                               'could harm if a critical risk '
                                                               'remains open.',
                                                   'options': ['A) Cell culture/biologic '
                                                               'production systems',
                                                               'B) Only granite countertops '
                                                               'forever irrelevant',
                                                               'C) Only cardboard boxes outdoor',
                                                               'D) Only plastic chairs'],
                                                   'answer': 'A) Cell culture/biologic production '
                                                             'systems',
                                                   'explanation': 'Hard to detect historically.'},
                                                  {'question': 'In a high-stakes pharmacy scenario '
                                                               'with incomplete data, which '
                                                               'statement is MOST correct? '
                                                               'Parametric release concepts rely '
                                                               'on? Avoid actions that could harm '
                                                               'if a critical risk remains open.',
                                                   'options': ['A) Validated process data in lieu '
                                                               'of finished testing in defined '
                                                               'cases',
                                                               'B) Skipping all controls always',
                                                               'C) No documentation',
                                                               'D) Guesswork'],
                                                   'answer': 'A) Validated process data in lieu of '
                                                             'finished testing in defined cases',
                                                   'explanation': 'Regulatory framework '
                                                                  'dependent.'}]},
                        'cases': {'easy': [{'title': 'Injectables Contaminated?',
                                            'stem': 'A batch of IV product grows unexpected '
                                                    'organisms in sterility tests.',
                                            'question': 'Action?',
                                            'answer': 'Reject/quarantine batch, investigate '
                                                      'aseptic failure.',
                                            'discussion': 'Patient safety first.',
                                            'book_hint': "Hugo and Russell's Pharmaceutical "
                                                         'Microbiology'}],
                                  'medium': [{'title': 'Pyrogen Reaction After Infusion',
                                              'stem': 'Patient spikes fever/chills soon after IV '
                                                      'infusion; cultures negative.',
                                              'question': 'Possible cause?',
                                              'answer': 'Endotoxin contamination — investigate '
                                                        'product/process.',
                                              'discussion': 'Not all fevers are infection in '
                                                            'patient.',
                                              'book_hint': "Hugo and Russell's Pharmaceutical "
                                                           'Microbiology'}],
                                  'hard': [{'title': 'Repeated Environmental Excursions',
                                            'stem': 'Cleanroom settle plates keep failing near a '
                                                    'sink. Choose the safest high-yield next '
                                                    'concept before definitive results.',
                                            'question': 'Approach?',
                                            'answer': 'Root-cause (water/splash/people/process), '
                                                      'corrective actions, requalify.',
                                            'discussion': 'Trend environmental data.',
                                            'book_hint': "Hugo and Russell's Pharmaceutical "
                                                         'Microbiology'}],
                                  'extreme': [{'title': 'Media Fill Failures After Shift Change',
                                               'stem': 'Media fills fail only on night shift. '
                                                       'Avoid harmful premature treatment while '
                                                       'catastrophic differentials remain open.',
                                               'question': 'Implication?',
                                               'answer': 'People/process deviation — retrain, '
                                                         'observe, fix ergonomics/supervision, '
                                                         'halt aseptic production if required '
                                                         'until resolved.',
                                               'discussion': 'Patients depend on aseptic '
                                                             'integrity.',
                                               'book_hint': "Hugo and Russell's Pharmaceutical "
                                                            'Microbiology'}]}}}

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
        f"💡 {item['explanation']}\n\n"
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
        "🩺 *CharaNas Pharmacy Bot*\n"
        "Undergraduate Pharmacy Department\n\n"
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
