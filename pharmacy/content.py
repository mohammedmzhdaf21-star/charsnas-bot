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
                                          'options': ['A) Activates a receptor and increases '
                                                      'signaling',
                                                      'B) Occupies a receptor without activating '
                                                      'it',
                                                      'C) Irreversibly destroys the receptor '
                                                      'protein',
                                                      'D) Only inhibits an enzyme at all doses'],
                                          'answer': 'A) Activates a receptor and increases '
                                                    'signaling',
                                          'explanation': 'An agonist binds a receptor and '
                                                         'stabilizes an active conformation, '
                                                         'thereby increasing receptor signaling '
                                                         'relative to basal tone. Full agonists '
                                                         "can elicit the system's maximal "
                                                         'response, whereas partial agonists '
                                                         'produce a submaximal effect even at full '
                                                         'occupancy. Antagonists occupy the same '
                                                         'or related sites without activating the '
                                                         'receptor and therefore reduce agonist '
                                                         'effect.'},
                                         {'question': 'First-pass metabolism mainly occurs after?',
                                          'options': ['A) Intravenous bolus administration',
                                                      'B) Oral absorption with hepatic portal '
                                                      'passage',
                                                      'C) Intramuscular injection into deltoid '
                                                      'muscle',
                                                      'D) Topical application to intact skin'],
                                          'answer': 'B) Oral absorption with hepatic portal '
                                                    'passage',
                                          'explanation': 'After oral absorption, drug in the '
                                                         'portal circulation passes through the '
                                                         'liver before reaching the systemic '
                                                         'arterial blood. Extensive hepatic '
                                                         'extraction or gut-wall metabolism during '
                                                         'this first pass can substantially reduce '
                                                         'bioavailability. Intravenous '
                                                         'administration bypasses first-pass '
                                                         'metabolism, which is why oral and IV '
                                                         'doses often differ for high-extraction '
                                                         'drugs.'},
                                         {'question': 'Therapeutic index relates to?',
                                          'options': ['A) Tablet dissolution rate in gastric fluid',
                                                      'B) Plasma protein-binding percentage alone',
                                                      'C) Safety margin between effective and '
                                                      'toxic doses',
                                                      'D) Time to reach peak plasma concentration'],
                                          'answer': 'C) Safety margin between effective and toxic '
                                                    'doses',
                                          'explanation': 'The therapeutic index compares a toxic '
                                                         'dose measure (for example TD50) with an '
                                                         'effective dose measure (for example '
                                                         'ED50), reflecting the margin between '
                                                         'efficacy and harm. Drugs with a narrow '
                                                         'therapeutic index have overlapping '
                                                         'effective and toxic concentration '
                                                         'ranges. Such agents typically require '
                                                         'careful dose titration and, when '
                                                         'appropriate, therapeutic drug '
                                                         'monitoring.'}],
                                'medium': [{'question': 'Beta-blocker caution is highest in?',
                                            'options': ['A) Mild seasonal allergic rhinitis only',
                                                        'B) Stable hypothyroidism on levothyroxine',
                                                        'C) Osteoarthritis treated with NSAIDs',
                                                        'D) Asthma when using nonselective agents'],
                                            'answer': 'D) Asthma when using nonselective agents',
                                            'explanation': 'Nonselective β-blockers antagonize '
                                                           'β2-adrenergic receptors that mediate '
                                                           'bronchial smooth-muscle relaxation. '
                                                           'Loss of β2 tone can precipitate '
                                                           'bronchoconstriction in patients with '
                                                           'asthma or reactive airway disease. '
                                                           'Cardioselective β1-blockers reduce but '
                                                           'do not abolish this risk at higher '
                                                           'doses.'},
                                           {'question': 'ACE inhibitor common side effect?',
                                            'options': ['A) Dry cough from bradykinin accumulation',
                                                        'B) Gingival hyperplasia as the class '
                                                        'hallmark',
                                                        'C) Orange urine discoloration in most '
                                                        'users',
                                                        'D) Ototoxicity at standard '
                                                        'antihypertensive doses'],
                                            'answer': 'A) Dry cough from bradykinin accumulation',
                                            'explanation': 'ACE inhibitors block '
                                                           'angiotensin-converting enzyme, which '
                                                           'also degrades bradykinin in the lungs '
                                                           'and vasculature. Accumulated '
                                                           'bradykinin and related peptides '
                                                           'stimulate sensory nerves and are the '
                                                           'principal mechanism of '
                                                           'ACE-inhibitor–associated dry cough. '
                                                           'Angiotensin-receptor blockers spare '
                                                           'ACE and therefore rarely cause this '
                                                           'cough, making them a common '
                                                           'alternative.'},
                                           {'question': 'Zero-order elimination example theme?',
                                            'options': ['A) Most beta-lactam antibiotics at usual '
                                                        'doses',
                                                        'B) Phenytoin and ethanol at higher levels',
                                                        'C) All water-soluble vitamins without '
                                                        'exception',
                                                        'D) Isotonic saline infused as maintenance '
                                                        'fluid'],
                                            'answer': 'B) Phenytoin and ethanol at higher levels',
                                            'explanation': 'Zero-order (saturation) elimination '
                                                           'occurs when metabolizing enzymes '
                                                           'operate near Vmax, so a constant '
                                                           'amount of drug is removed per unit '
                                                           'time. Phenytoin and ethanol '
                                                           'classically show this nonlinear '
                                                           'behavior at clinically relevant '
                                                           'concentrations. Small dose increases '
                                                           'can then produce disproportionately '
                                                           'large rises in plasma concentration '
                                                           'and toxicity risk.'}],
                                'hard': [{'question': 'Competitive antagonist effect on agonist '
                                                      'curve?',
                                          'options': ['A) Depresses Emax with no change in EC50',
                                                      'B) Left-shifts the curve and raises Emax',
                                                      'C) Right shift with same maximal response '
                                                      'if surmountable',
                                                      'D) Converts the agonist into an '
                                                      'irreversible binder'],
                                          'answer': 'C) Right shift with same maximal response if '
                                                    'surmountable',
                                          'explanation': 'A surmountable competitive antagonist '
                                                         'and agonist compete for the same '
                                                         'receptor site, so higher agonist '
                                                         'concentrations restore receptor '
                                                         'occupancy. On a concentration–response '
                                                         'curve this produces a parallel rightward '
                                                         'shift with preserved maximal response '
                                                         '(Emax). Noncompetitive or irreversible '
                                                         'antagonism more typically depresses Emax '
                                                         'when receptor reserve is limited.'},
                                         {'question': 'CYP3A4 induction may?',
                                          'options': ['A) Block first-pass metabolism completely',
                                                      'B) Increase oral bioavailability of all '
                                                      'substrates',
                                                      'C) Prolong half-life of every CYP3A4 '
                                                      'substrate',
                                                      'D) Reduce plasma levels of sensitive '
                                                      'substrate drugs'],
                                          'answer': 'D) Reduce plasma levels of sensitive '
                                                    'substrate drugs',
                                          'explanation': 'CYP3A4 induction increases transcription '
                                                         'and amount of active enzyme, '
                                                         'accelerating oxidative metabolism of '
                                                         'many substrates. Faster clearance lowers '
                                                         'steady-state plasma concentrations and '
                                                         'can cause loss of therapeutic effect for '
                                                         'inducer-sensitive drugs. The interaction '
                                                         'magnitude depends on inducer potency, '
                                                         'substrate fraction metabolized by '
                                                         'CYP3A4, and dosing time course.'},
                                         {'question': 'Loading dose mainly depends on?',
                                          'options': ['A) Volume of distribution and target '
                                                      'concentration',
                                                      'B) Clearance alone without considering Vd',
                                                      'C) Elimination half-life as the sole '
                                                      'determinant',
                                                      'D) Dosing interval chosen for maintenance '
                                                      'therapy'],
                                          'answer': 'A) Volume of distribution and target '
                                                    'concentration',
                                          'explanation': 'Loading dose is chosen to rapidly '
                                                         'achieve a target concentration in the '
                                                         'apparent volume of distribution: LD ≈ '
                                                         'Css × Vd (adjusted for bioavailability). '
                                                         'It fills the distributive space rather '
                                                         'than matching elimination rate. '
                                                         'Maintenance dose, by contrast, replaces '
                                                         'drug lost through clearance and is '
                                                         'therefore governed mainly by CL and '
                                                         'dosing interval.'}],
                                'extreme': [{'question': 'Torsades risk rises with?',
                                             'options': ['A) Therapeutic-dose paracetamol used '
                                                         'alone',
                                                         'B) QT-prolonging drugs plus electrolyte '
                                                         'imbalance',
                                                         'C) Topical emollients applied to dry '
                                                         'skin',
                                                         'D) Routine vitamin C and D '
                                                         'supplementation'],
                                             'answer': 'B) QT-prolonging drugs plus electrolyte '
                                                       'imbalance',
                                             'explanation': 'Torsades de pointes is a polymorphic '
                                                            'ventricular tachycardia linked to '
                                                            'delayed ventricular repolarization '
                                                            'and QT interval prolongation. Many '
                                                            'drugs block cardiac IKr (hERG) '
                                                            'potassium channels, and hypokalemia '
                                                            'or hypomagnesemia further destabilize '
                                                            'repolarization. Concurrent '
                                                            'QT-prolonging drugs plus electrolyte '
                                                            'imbalance therefore synergistically '
                                                            'elevate torsades risk.'},
                                            {'question': 'Serotonin syndrome risk combination '
                                                         'theme?',
                                             'options': ['A) Two low-potency topical '
                                                         'corticosteroids together',
                                                         'B) Antacid plus alginate taken after '
                                                         'meals',
                                                         'C) MAOI combined with SSRI or other '
                                                         'strong serotonergics',
                                                         'D) Fluoride toothpaste used with calcium '
                                                         'supplements'],
                                             'answer': 'C) MAOI combined with SSRI or other strong '
                                                       'serotonergics',
                                             'explanation': 'Serotonin syndrome reflects excess '
                                                            'serotonergic tone at central 5-HT '
                                                            'receptors, especially 5-HT2A. '
                                                            'Combining monoamine oxidase '
                                                            'inhibitors with SSRIs, or other '
                                                            'strongly serotonergic pairs, can '
                                                            'produce hyperthermia, autonomic '
                                                            'instability, clonus, and altered '
                                                            'mentation. The interaction is '
                                                            'pharmacodynamic amplification of '
                                                            'synaptic serotonin rather than a '
                                                            'simple additive sedative effect.'},
                                            {'question': 'Narrow therapeutic index warfarin '
                                                         'interaction?',
                                             'options': ['A) Warfarin never has clinically '
                                                         'relevant CYP interactions',
                                                         'B) CYP2C9 induction always lowers '
                                                         'bleeding risk only',
                                                         'C) Toothpaste fluoride is the main INR '
                                                         'determinant',
                                                         'D) CYP2C9 inhibitors can raise INR and '
                                                         'bleed risk'],
                                             'answer': 'D) CYP2C9 inhibitors can raise INR and '
                                                       'bleed risk',
                                             'explanation': 'S-warfarin, the more potent '
                                                            'enantiomer, is cleared largely by '
                                                            'CYP2C9. CYP2C9 inhibitors reduce '
                                                            'S-warfarin clearance, raising plasma '
                                                            'levels and vitamin K epoxide '
                                                            'reductase inhibition. The resulting '
                                                            'increase in INR prolongs coagulation '
                                                            'and elevates bleeding risk, which is '
                                                            'clinically important because '
                                                            "warfarin's therapeutic index is "
                                                            'narrow.'}]},
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
                                               'options': ['A) Replace all brand products with the '
                                                           'cheapest generic',
                                                           'B) Ensure accurate medication lists '
                                                           'across care transitions',
                                                           'C) Stop therapeutic drug monitoring '
                                                           'for all inpatients',
                                                           'D) Limit counseling to discharge '
                                                           'antibiotics only'],
                                               'answer': 'B) Ensure accurate medication lists '
                                                         'across care transitions',
                                               'explanation': 'Medication reconciliation '
                                                              'systematically compares medication '
                                                              'lists across care transitions such '
                                                              'as admission, transfer, and '
                                                              'discharge. The process identifies '
                                                              'omissions, duplications, dosing '
                                                              'errors, and unintended '
                                                              'discrepancies between what the '
                                                              'patient takes and what is ordered. '
                                                              'Accurate lists reduce preventable '
                                                              'adverse drug events at interfaces '
                                                              'of care.'},
                                              {'question': 'ADR means?',
                                               'options': ['A) Average daily requirement for '
                                                           'vitamins',
                                                           'B) Authorized dispensing record in '
                                                           'hospital',
                                                           'C) Adverse drug reaction',
                                                           'D) Absolute dose reduction applied '
                                                           'annually'],
                                               'answer': 'C) Adverse drug reaction',
                                               'explanation': 'An adverse drug reaction is a '
                                                              'noxious, unintended response to a '
                                                              'medicine at doses used for '
                                                              'prophylaxis, diagnosis, or therapy. '
                                                              'ADRs include augmented (type A) '
                                                              'dose-related effects and bizarre '
                                                              '(type B) idiosyncratic or '
                                                              'immune-mediated reactions. '
                                                              'Detection, causality assessment, '
                                                              'management, and spontaneous '
                                                              'reporting are core '
                                                              'pharmacovigilance tasks.'},
                                              {'question': 'Counseling on antibiotics should '
                                                           'include?',
                                               'options': ['A) Stopping as soon as symptoms '
                                                           'improve by 24 hours',
                                                           'B) Sharing leftover tablets with '
                                                           'household contacts',
                                                           'C) Doubling the dose if a dose was '
                                                           'missed yesterday',
                                                           'D) Completing the course as directed '
                                                           'and stewardship themes'],
                                               'answer': 'D) Completing the course as directed and '
                                                         'stewardship themes',
                                               'explanation': 'Completing an antibiotic course as '
                                                              'prescribed helps eradicate '
                                                              'susceptible pathogens when the '
                                                              'indication, agent, and duration are '
                                                              'appropriate. Unnecessary '
                                                              'prolongation or use without '
                                                              'infection, however, selects for '
                                                              'resistant organisms and harms '
                                                              'stewardship goals. Counseling '
                                                              'therefore balances adherence with '
                                                              'clear advice on indication, '
                                                              'duration, and when to seek '
                                                              'review.'}],
                                     'medium': [{'question': 'Beers Criteria help identify?',
                                                 'options': ['A) Potentially inappropriate '
                                                             'medicines in older adults',
                                                             'B) IV compatibility charts for '
                                                             'pediatric TPN only',
                                                             'C) Bioequivalence limits for generic '
                                                             'antibiotics',
                                                             'D) WHO essential medicines for '
                                                             'tropical infections'],
                                                 'answer': 'A) Potentially inappropriate medicines '
                                                           'in older adults',
                                                 'explanation': 'Beers Criteria catalog medicines '
                                                                'that are often potentially '
                                                                'inappropriate in older adults '
                                                                'because of altered '
                                                                'pharmacokinetics, '
                                                                'pharmacodynamics, and higher '
                                                                'adverse-effect burden. Examples '
                                                                'include strong anticholinergics '
                                                                'and long-acting benzodiazepines. '
                                                                'The lists support deprescribing '
                                                                'discussions but must be '
                                                                'individualized to comorbidity, '
                                                                'goals of care, and safer '
                                                                'alternatives.'},
                                                {'question': 'Renal dose adjustment needed when?',
                                                 'options': ['A) The drug is cleared only by '
                                                             'hepatic CYP3A4',
                                                             'B) Drug is cleared renally and GFR '
                                                             'is reduced',
                                                             'C) The patient has mild seasonal '
                                                             'allergic rhinitis',
                                                             'D) Plasma albumin is high without '
                                                             'renal impairment'],
                                                 'answer': 'B) Drug is cleared renally and GFR is '
                                                           'reduced',
                                                 'explanation': 'When glomerular filtration rate '
                                                                'falls, renally cleared drugs and '
                                                                'active metabolites accumulate '
                                                                'unless the dose or interval is '
                                                                'adjusted. Accumulation increases '
                                                                'exposure and toxicity risk for '
                                                                'agents such as many '
                                                                'aminoglycosides, gabapentinoids, '
                                                                'and renally excreted '
                                                                'anticoagulants. Dose adjustment '
                                                                'uses estimated kidney function '
                                                                'and drug-specific renal dosing '
                                                                'guidance.'},
                                                {'question': 'Anticoagulant counseling key point?',
                                                 'options': ['A) Ignore dietary vitamin K '
                                                             'fluctuations entirely',
                                                             'B) Crush all tablets to improve '
                                                             'absorption always',
                                                             'C) Recognize bleeding signs and '
                                                             'interaction awareness',
                                                             'D) Stop therapy whenever a headache '
                                                             'occurs once'],
                                                 'answer': 'C) Recognize bleeding signs and '
                                                           'interaction awareness',
                                                 'explanation': 'Therapeutic anticoagulation '
                                                                'intentionally impairs hemostasis, '
                                                                'so patients must recognize '
                                                                'bleeding warning signs such as '
                                                                'melena, hematuria, or '
                                                                'uncontrolled bruising. Drug–drug '
                                                                'and drug–food interactions can '
                                                                'raise or lower anticoagulant '
                                                                'effect, especially with warfarin '
                                                                'and some DOAC pathways. '
                                                                'Counseling links efficacy to '
                                                                'safety-net actions when bleeding '
                                                                'or interacting medicines '
                                                                'appear.'}],
                                     'hard': [{'question': 'Vancomycin dosing commonly uses?',
                                               'options': ['A) Ideal body weight only, ignoring '
                                                           'renal function',
                                                           'B) Fixed 1 g for every adult '
                                                           'regardless of levels',
                                                           'C) Hepatic Child–Pugh score as the '
                                                           'primary guide',
                                                           'D) Weight and renal function, often '
                                                           'with level monitoring'],
                                               'answer': 'D) Weight and renal function, often with '
                                                         'level monitoring',
                                               'explanation': 'Vancomycin is a large glycopeptide '
                                                              'cleared predominantly by glomerular '
                                                              'filtration, so dosing is guided by '
                                                              'actual body weight and renal '
                                                              'function. AUC- or trough-based '
                                                              'therapeutic drug monitoring is used '
                                                              'in many protocols to balance '
                                                              'bactericidal exposure against '
                                                              'nephrotoxicity. Loading strategies '
                                                              'and subsequent adjustment reflect '
                                                              'distribution volume and changing '
                                                              'clearance.'},
                                              {'question': 'Hyperkalemia risk with?',
                                               'options': ['A) ACE inhibitor plus spironolactone '
                                                           'combinations',
                                                           'B) Loop diuretic plus thiazide used '
                                                           'together only',
                                                           'C) Short-acting insulin given before '
                                                           'meals',
                                                           'D) Inhaled salbutamol used for acute '
                                                           'asthma'],
                                               'answer': 'A) ACE inhibitor plus spironolactone '
                                                         'combinations',
                                               'explanation': 'ACE inhibitors reduce angiotensin '
                                                              'II–mediated aldosterone secretion, '
                                                              'decreasing renal potassium '
                                                              'excretion. '
                                                              'Mineralocorticoid-receptor '
                                                              'antagonists such as spironolactone '
                                                              'further block aldosterone effect in '
                                                              'the collecting duct. Combined use '
                                                              'therefore markedly increases '
                                                              'hyperkalemia risk, especially in '
                                                              'chronic kidney disease or with '
                                                              'potassium supplements.'},
                                              {'question': 'Steroid sick-day rules teach?',
                                               'options': ['A) Stop glucocorticoids abruptly '
                                                           'during fever',
                                                           'B) Increase dose during significant '
                                                           'illness per plan',
                                                           'C) Replace oral steroids with topical '
                                                           'cream only',
                                                           'D) Halve the dose whenever appetite '
                                                           'decreases'],
                                               'answer': 'B) Increase dose during significant '
                                                         'illness per plan',
                                               'explanation': 'Long-term exogenous glucocorticoids '
                                                              'suppress the '
                                                              'hypothalamic–pituitary–adrenal '
                                                              'axis, so endogenous cortisol may be '
                                                              'inadequate during physiologic '
                                                              'stress. Sick-day rules instruct '
                                                              'temporary dose increases during '
                                                              'significant illness, fever, or '
                                                              'vomiting according to an '
                                                              'individualized plan. The goal is to '
                                                              'prevent adrenal crisis from '
                                                              'relative cortisol deficiency.'}],
                                     'extreme': [{'question': 'Chemotherapy extravasation '
                                                              'priority?',
                                                  'options': ['A) Increase infusion rate to clear '
                                                              'the line faster',
                                                              'B) Apply heat to all vesicants '
                                                              'without identifying the drug',
                                                              'C) Stop infusion and follow '
                                                              'protocol antidote pathway',
                                                              'D) Flush vigorously with large '
                                                              'volumes of undiluted drug'],
                                                  'answer': 'C) Stop infusion and follow protocol '
                                                            'antidote pathway',
                                                  'explanation': 'Vesicant chemotherapy '
                                                                 'extravasated into soft tissue '
                                                                 'can cause severe local necrosis '
                                                                 'through direct cytotoxicity and '
                                                                 'inflammation. Immediate '
                                                                 'priorities are to stop the '
                                                                 'infusion, leave or aspirate via '
                                                                 'the cannula as protocol directs, '
                                                                 'and mark the site while '
                                                                 'arranging antidote or surgical '
                                                                 'pathways. Agent-specific '
                                                                 'measures (for example '
                                                                 'dexrazoxane for anthracyclines) '
                                                                 'follow institutional '
                                                                 'extravasation protocols.'},
                                                 {'question': 'Clozapine pharmacy monitoring '
                                                              'theme?',
                                                  'options': ['A) Only liver enzymes every five '
                                                              'years',
                                                              'B) Only fasting lipids on day one '
                                                              'of therapy',
                                                              'C) Only blood pressure after each '
                                                              'dose forever',
                                                              'D) Mandatory blood counts for '
                                                              'agranulocytosis risk'],
                                                  'answer': 'D) Mandatory blood counts for '
                                                            'agranulocytosis risk',
                                                  'explanation': 'Clozapine can cause '
                                                                 'idiosyncratic agranulocytosis '
                                                                 'through toxic or immune-mediated '
                                                                 'injury to neutrophils. Mandatory '
                                                                 'scheduled full blood counts '
                                                                 'detect falling absolute '
                                                                 'neutrophil counts before '
                                                                 'life-threatening infection '
                                                                 'develops. Dispensing is '
                                                                 'typically linked to registry or '
                                                                 'protocol confirmation that '
                                                                 'hematologic monitoring remains '
                                                                 'within acceptable limits.'},
                                                 {'question': 'Opioid stewardship in hospital '
                                                              'includes?',
                                                  'options': ['A) Appropriate indication, dose, '
                                                              'naloxone awareness, constipation '
                                                              'prophylaxis',
                                                              'B) Automatic escalation to '
                                                              'long-acting opioids for all acute '
                                                              'pain',
                                                              'C) Avoiding laxatives to prevent '
                                                              'opioid withdrawal',
                                                              'D) Discharging all patients with '
                                                              'unlimited PRN refills'],
                                                  'answer': 'A) Appropriate indication, dose, '
                                                            'naloxone awareness, constipation '
                                                            'prophylaxis',
                                                  'explanation': 'Hospital opioid stewardship '
                                                                 'matches opioid choice and dose '
                                                                 'to verified pain indication '
                                                                 'while minimizing respiratory '
                                                                 'depression and misuse risk. '
                                                                 'Naloxone availability and '
                                                                 'education address μ-opioid '
                                                                 'receptor overdose reversibility. '
                                                                 'Because opioids slow gut '
                                                                 'motility via enteric '
                                                                 'μ-receptors, prophylactic '
                                                                 'laxatives are routine to prevent '
                                                                 'opioid-induced constipation.'}]},
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
                                           'options': ['A) Increase disintegration speed only',
                                                       'B) Mask bitter taste without affecting '
                                                       'strength',
                                                       'C) Hold powder particles together in the '
                                                       'compact',
                                                       'D) Sterilize the blend during compression'],
                                           'answer': 'C) Hold powder particles together in the '
                                                     'compact',
                                           'explanation': 'Binders are tablet excipients that '
                                                          'adhesively link powder particles during '
                                                          'granulation or compression, imparting '
                                                          'mechanical strength to the compact. '
                                                          'Adequate binding reduces friability and '
                                                          'capping, while excess binder can slow '
                                                          'disintegration and dissolution. Common '
                                                          'examples include povidone, starch '
                                                          'paste, and cellulose derivatives.'},
                                          {'question': 'Bioavailability compares?',
                                           'options': ['A) Tablet hardness and friability scores '
                                                       'only',
                                                       'B) Shelf-life under accelerated humidity '
                                                       'stress',
                                                       'C) Cost per milligram across brand '
                                                       'products',
                                                       'D) Rate and extent of drug reaching '
                                                       'systemic circulation'],
                                           'answer': 'D) Rate and extent of drug reaching systemic '
                                                     'circulation',
                                           'explanation': 'Bioavailability is the rate and extent '
                                                          'to which unchanged drug reaches the '
                                                          'systemic circulation. Extent is '
                                                          'commonly quantified by area under the '
                                                          'plasma concentration–time curve (AUC) '
                                                          'relative to an intravenous reference '
                                                          'for absolute bioavailability. Rate is '
                                                          'reflected in parameters such as Cmax '
                                                          'and tmax, which matter for onset and '
                                                          'peak effect.'},
                                          {'question': 'Sterile products must be?',
                                           'options': ['A) Free from viable microorganisms per '
                                                       'specifications',
                                                       'B) Colored red to indicate parenteral use',
                                                       'C) Stored only in amber glass regardless '
                                                       'of light sensitivity',
                                                       'D) Isotonic with plasma even for oral '
                                                       'liquids'],
                                           'answer': 'A) Free from viable microorganisms per '
                                                     'specifications',
                                           'explanation': 'Sterility means the absence of viable '
                                                          'contaminating microorganisms in the '
                                                          'finished product within the sensitivity '
                                                          'of validated sterility assurance '
                                                          'processes. Injectable and ophthalmic '
                                                          'preparations require sterilization or '
                                                          'aseptic manufacture because parenteral '
                                                          'routes bypass skin and mucosal '
                                                          'barriers. Failure of sterility can '
                                                          'cause severe infection including '
                                                          'sepsis.'}],
                                 'medium': [{'question': 'BCS Class II drugs are?',
                                             'options': ['A) High solubility and low permeability',
                                                         'B) Low solubility and high permeability',
                                                         'C) High solubility and high permeability',
                                                         'D) Low solubility and low permeability'],
                                             'answer': 'B) Low solubility and high permeability',
                                             'explanation': 'The Biopharmaceutics Classification '
                                                            'System places Class II drugs in the '
                                                            'low aqueous solubility, high '
                                                            'intestinal permeability quadrant. For '
                                                            'these compounds, dissolution in '
                                                            'gastrointestinal fluid is frequently '
                                                            'rate-limiting for absorption. '
                                                            'Formulation strategies that increase '
                                                            'dissolution rate (particle size '
                                                            'reduction, salts, solid dispersions) '
                                                            'therefore often improve oral '
                                                            'bioavailability.'},
                                            {'question': 'Lyophilization is?',
                                             'options': ['A) Spray-drying of oils into soft '
                                                         'gelatin capsules',
                                                         'B) Wet granulation with alcoholic '
                                                         'binders',
                                                         'C) Freeze-drying by sublimation under '
                                                         'vacuum',
                                                         'D) Hot-melt extrusion of crystalline '
                                                         'APIs only'],
                                             'answer': 'C) Freeze-drying by sublimation under '
                                                       'vacuum',
                                             'explanation': 'Lyophilization (freeze-drying) '
                                                            'removes water by sublimation from a '
                                                            'frozen product under vacuum, yielding '
                                                            'a dry solid cake. Lower residual '
                                                            'moisture slows hydrolysis and many '
                                                            'other degradation pathways, improving '
                                                            'stability of injectables and '
                                                            'biologics. The process also enables '
                                                            'reconstitution to a solution at the '
                                                            'point of use.'},
                                            {'question': 'Osmotic pump tablets provide?',
                                             'options': ['A) Immediate burst release triggered by '
                                                         'chewing',
                                                         'B) pH-independent taste masking only',
                                                         'C) Zero gastric emptying for all meal '
                                                         'states',
                                                         'D) Controlled release driven by osmotic '
                                                         'pressure'],
                                             'answer': 'D) Controlled release driven by osmotic '
                                                       'pressure',
                                             'explanation': 'Osmotic pump tablets admit water '
                                                            'through a semipermeable membrane; '
                                                            'osmotic pressure then drives drug '
                                                            'solution out through a laser-drilled '
                                                            'orifice at a controlled rate. Release '
                                                            'is relatively independent of '
                                                            'gastrointestinal pH and motility '
                                                            'within design limits. Crushing '
                                                            'destroys the membrane system and can '
                                                            'cause dose dumping.'}],
                                 'hard': [{'question': 'Noyes–Whitney relates to?',
                                           'options': ['A) Dissolution rate of solid drugs',
                                                       'B) Protein binding equilibrium constants',
                                                       'C) Renal tubular secretion capacity',
                                                       'D) Tablet punch pressure calibration only'],
                                           'answer': 'A) Dissolution rate of solid drugs',
                                           'explanation': 'The Noyes–Whitney equation states that '
                                                          'dissolution rate is proportional to '
                                                          'surface area and to the concentration '
                                                          "gradient between the drug's saturation "
                                                          'solubility at the particle surface and '
                                                          'the bulk solution. A diffusion layer '
                                                          'thickness term and diffusion '
                                                          'coefficient also govern mass transport. '
                                                          'Particle-size reduction increases '
                                                          'surface area and thus often accelerates '
                                                          'dissolution.'},
                                          {'question': 'Partition coefficient (log P) indicates?',
                                           'options': ['A) Aqueous solubility at every pH equally',
                                                       'B) Lipophilicity of the unionized species',
                                                       'C) Melting point of polymorphic forms',
                                                       'D) Tablet disintegration time in vivo'],
                                           'answer': 'B) Lipophilicity of the unionized species',
                                           'explanation': 'The partition coefficient P is the '
                                                          'equilibrium concentration ratio of '
                                                          'unionized solute between octanol and '
                                                          'water, usually expressed as log P. '
                                                          'Higher log P indicates greater '
                                                          'lipophilicity, favoring membrane '
                                                          'permeation but often reducing aqueous '
                                                          'solubility. Log P therefore helps '
                                                          'predict absorption, distribution, and '
                                                          'formulation challenges.'},
                                          {'question': 'HLB system helps select?',
                                           'options': ['A) Capsule shell gelatin bloom strength',
                                                       'B) Autoclave cycle hold times for vials',
                                                       'C) Emulsifying agents for oil–water '
                                                       'systems',
                                                       'D) Sieve sizes for powder blending only'],
                                           'answer': 'C) Emulsifying agents for oil–water systems',
                                           'explanation': 'The hydrophilic–lipophilic balance '
                                                          '(HLB) scale ranks surfactants by their '
                                                          'relative affinity for water versus oil. '
                                                          'Low-HLB agents tend to stabilize '
                                                          'water-in-oil emulsions, whereas '
                                                          'higher-HLB agents favor oil-in-water '
                                                          'systems. Formulators select emulsifiers '
                                                          '(or blends) whose HLB matches the '
                                                          'required emulsion type and oil phase.'}],
                                 'extreme': [{'question': 'Nanoparticle carriers aim to?',
                                              'options': ['A) Eliminate the need for any '
                                                          'excipients forever',
                                                          'B) Convert all drugs into '
                                                          'immediate-release syrups',
                                                          'C) Guarantee 100% oral bioavailability '
                                                          'always',
                                                          'D) Modify distribution, targeting, or '
                                                          'solubility profiles'],
                                              'answer': 'D) Modify distribution, targeting, or '
                                                        'solubility profiles',
                                              'explanation': 'Nanoparticle carriers such as '
                                                             'liposomes, polymeric nanoparticles, '
                                                             'and lipid nanoparticles alter a '
                                                             "drug's effective solubility, "
                                                             'circulation time, and tissue '
                                                             'distribution. Surface properties and '
                                                             'size can promote passive '
                                                             'accumulation or ligand-mediated '
                                                             'targeting while protecting labile '
                                                             'actives. These systems are '
                                                             'formulation tools to optimize '
                                                             'pharmacokinetics and local exposure '
                                                             "rather than changing the drug's "
                                                             'intrinsic receptor pharmacology '
                                                             'alone.'},
                                             {'question': 'Glass transition (Tg) matters for?',
                                              'options': ['A) Amorphous solid physical stability '
                                                          'and mobility',
                                                          'B) Only crystalline melting point '
                                                          'determination',
                                                          'C) Only capsule locking ring dimensions',
                                                          'D) Only syringe needle gauge selection'],
                                              'answer': 'A) Amorphous solid physical stability and '
                                                        'mobility',
                                              'explanation': 'The glass transition temperature '
                                                             '(Tg) is the temperature region where '
                                                             'an amorphous solid softens from a '
                                                             'glassy to a rubbery state with '
                                                             'increased molecular mobility. Above '
                                                             'Tg, crystallization and chemical '
                                                             'degradation of amorphous drugs or '
                                                             'dispersions accelerate. Storage well '
                                                             'below Tg, with controlled moisture '
                                                             'plasticization, is therefore '
                                                             'critical for amorphous physical '
                                                             'stability.'},
                                             {'question': 'Extractables/leachables concern in?',
                                              'options': ['A) Oral sugar-coated tablets '
                                                          'exclusively',
                                                          'B) Container–closure systems for '
                                                          'injectables',
                                                          'C) Hardness testing of chewable '
                                                          'vitamins',
                                                          'D) Color lake selection for film coats '
                                                          'only'],
                                              'answer': 'B) Container–closure systems for '
                                                        'injectables',
                                              'explanation': 'Extractables are compounds that can '
                                                             'be pulled from packaging under '
                                                             'aggressive laboratory conditions; '
                                                             'leachables migrate into the product '
                                                             'under real storage. For injectables, '
                                                             'container–closure systems '
                                                             '(elastomers, plastics, glass) are '
                                                             'primary sources of such impurities. '
                                                             'Leachables may cause toxicity, '
                                                             'particulate issues, or drug '
                                                             'degradation, so materials are '
                                                             'qualified with extractable/leachable '
                                                             'studies.'}]},
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
                                              'options': ['A) Complete elimination of all drug '
                                                          'from the body',
                                                          'B) Absorption of 50% of an oral dose',
                                                          'C) Distribution equilibrium with every '
                                                          'tissue',
                                                          'D) Plasma concentration to fall by 50%'],
                                              'answer': 'D) Plasma concentration to fall by 50%',
                                              'explanation': 'Elimination half-life (t½) is the '
                                                             'time required for plasma drug '
                                                             'concentration to decrease by 50% '
                                                             'during the terminal elimination '
                                                             'phase in linear kinetics. It is '
                                                             'determined by both clearance and '
                                                             'volume of distribution (t½ ≈ 0.693 × '
                                                             'Vd/CL). Half-life informs dosing '
                                                             'interval selection and the time '
                                                             'needed to approach steady state.'},
                                             {'question': 'Clearance reflects?',
                                              'options': ['A) Volume of plasma cleared of drug per '
                                                          'unit time',
                                                          'B) Fraction unbound in tissues at '
                                                          'steady state',
                                                          'C) Time from dosing to maximum effect '
                                                          'only',
                                                          'D) Tablet surface area available for '
                                                          'dissolution'],
                                              'answer': 'A) Volume of plasma cleared of drug per '
                                                        'unit time',
                                              'explanation': 'Clearance is the theoretical volume '
                                                             'of plasma completely cleared of drug '
                                                             'per unit time and equals the sum of '
                                                             'organ clearances (notably hepatic '
                                                             'and renal). At steady state, dosing '
                                                             'rate equals clearance times '
                                                             'steady-state concentration. '
                                                             'Maintenance dose design therefore '
                                                             'depends primarily on clearance and '
                                                             'bioavailability.'},
                                             {'question': 'Steady state roughly after?',
                                              'options': ['A) One half-life with any intermittent '
                                                          'regimen',
                                                          'B) About 4–5 half-lives with regular '
                                                          'dosing',
                                                          'C) Thirty minutes regardless of drug '
                                                          'half-life',
                                                          'D) Two dosing intervals for every '
                                                          'medicine'],
                                              'answer': 'B) About 4–5 half-lives with regular '
                                                        'dosing',
                                              'explanation': 'With regular fixed dosing and linear '
                                                             'kinetics, plasma concentrations '
                                                             'accumulate until input equals '
                                                             'elimination at steady state. About '
                                                             '4–5 elimination half-lives are '
                                                             'required to reach approximately '
                                                             '94–97% of steady-state exposure. A '
                                                             'loading dose can achieve target '
                                                             'concentrations sooner, but '
                                                             'steady-state timing still follows '
                                                             'half-life for subsequent '
                                                             'accumulation.'}],
                                    'medium': [{'question': 'AUC represents?',
                                                'options': ['A) Peak-to-trough fluctuation ratio '
                                                            'only',
                                                            'B) Volume of distribution at steady '
                                                            'state',
                                                            'C) Overall systemic drug exposure',
                                                            'D) Absorption lag time after oral '
                                                            'dosing'],
                                                'answer': 'C) Overall systemic drug exposure',
                                                'explanation': 'Area under the plasma '
                                                               'concentration–time curve (AUC) '
                                                               'integrates concentration over time '
                                                               'and quantifies total systemic '
                                                               'exposure. For linear kinetics, AUC '
                                                               'is proportional to dose and '
                                                               'inversely related to clearance '
                                                               '(AUC = F·Dose/CL). Bioavailability '
                                                               'and bioequivalence assessments '
                                                               'rely heavily on AUC comparisons '
                                                               'between formulations.'},
                                               {'question': 'Nonlinear PK means?',
                                                'options': ['A) Half-life is identical at all '
                                                            'doses forever',
                                                            'B) Clearance is constant across the '
                                                            'dose range',
                                                            'C) AUC always rises exactly '
                                                            'proportional to dose',
                                                            'D) Parameters change with dose, e.g. '
                                                            'saturation'],
                                                'answer': 'D) Parameters change with dose, e.g. '
                                                          'saturation',
                                                'explanation': 'Nonlinear (dose-dependent) '
                                                               'pharmacokinetics occur when '
                                                               'absorption, distribution, binding, '
                                                               'or elimination processes saturate '
                                                               'within the clinical dose range. '
                                                               'Michaelis–Menten metabolism of '
                                                               'phenytoin is a classic example: '
                                                               'clearance falls as concentration '
                                                               'rises. Consequently, steady-state '
                                                               'concentration is no longer '
                                                               'proportional to dose.'},
                                               {'question': 'Protein binding displacement may?',
                                                'options': ['A) Transiently raise free fraction '
                                                            'for highly bound drugs',
                                                            'B) Always double total plasma '
                                                            'concentration permanently',
                                                            'C) Eliminate renal clearance of '
                                                            'unbound drug',
                                                            'D) Convert first-order kinetics into '
                                                            'zero-order always'],
                                                'answer': 'A) Transiently raise free fraction for '
                                                          'highly bound drugs',
                                                'explanation': 'For highly protein-bound drugs, '
                                                               'displacement can transiently '
                                                               'increase unbound fraction and free '
                                                               'concentration. Increased free drug '
                                                               'is often also more available for '
                                                               'clearance and distribution, so '
                                                               'total concentration may fall while '
                                                               'free levels partly re-equilibrate. '
                                                               'Clinically important displacement '
                                                               'interactions are therefore less '
                                                               'common than total-level changes '
                                                               'alone might suggest, but remain '
                                                               'relevant for narrow-index, highly '
                                                               'bound drugs.'}],
                                    'hard': [{'question': 'Hepatic clearance for high extraction '
                                                          'drugs depends strongly on?',
                                              'options': ['A) Plasma protein binding as the sole '
                                                          'driver',
                                                          'B) Liver blood flow',
                                                          'C) Fraction unbound in the gut lumen '
                                                          'only',
                                                          'D) Gastric pH at the time of dosing'],
                                              'answer': 'B) Liver blood flow',
                                              'explanation': 'For high hepatic extraction-ratio '
                                                             'drugs, the liver removes most drug '
                                                             'from afferent blood in a single '
                                                             'pass, so clearance approximates '
                                                             'liver blood flow. Changes in hepatic '
                                                             'perfusion (heart failure, shock, '
                                                             'vasoactive drugs) therefore strongly '
                                                             'alter clearance of flow-limited '
                                                             'compounds. Low-extraction drugs are '
                                                             'instead more sensitive to intrinsic '
                                                             'metabolizing capacity and unbound '
                                                             'fraction.'},
                                             {'question': 'Renal clearance includes?',
                                              'options': ['A) Only glomerular filtration with no '
                                                          'other processes',
                                                          'B) Only tubular secretion without '
                                                          'filtration',
                                                          'C) Filtration minus reabsorption plus '
                                                          'secretion',
                                                          'D) Only hepatic conjugative metabolism'],
                                              'answer': 'C) Filtration minus reabsorption plus '
                                                        'secretion',
                                              'explanation': 'Renal clearance is the net result of '
                                                             'glomerular filtration of unbound '
                                                             'drug, tubular secretion into urine, '
                                                             'and tubular reabsorption back into '
                                                             'blood. Thus CLr ≈ (f_u · GFR) + '
                                                             'secretion − reabsorption. Urinary pH '
                                                             'can alter reabsorption of weak acids '
                                                             'and bases via ion trapping, changing '
                                                             'excretion of some drugs and toxins.'},
                                             {'question': 'Two-compartment model early phase is?',
                                              'options': ['A) Terminal elimination phase only',
                                                          'B) Steady-state infusion plateau only',
                                                          'C) Zero-order absorption from a depot',
                                                          'D) Distribution phase after IV bolus'],
                                              'answer': 'D) Distribution phase after IV bolus',
                                              'explanation': 'In a two-compartment model, drug '
                                                             'first distributes from a central '
                                                             'compartment (blood and rapidly '
                                                             'equilibrating tissues) into a '
                                                             'peripheral compartment. The early '
                                                             'steeper decline on a semilog plot is '
                                                             'this distribution (α) phase, '
                                                             'followed by a slower terminal '
                                                             'elimination (β) phase. Sampling '
                                                             'during distribution can misrepresent '
                                                             'concentrations intended to reflect '
                                                             'the elimination phase.'}],
                                    'extreme': [{'question': 'TDM for digoxin timing?',
                                                 'options': ['A) Avoid sampling in the '
                                                             'distribution phase; sample at steady '
                                                             'state appropriately',
                                                             'B) Draw levels 5 minutes after every '
                                                             'IV dose always',
                                                             'C) Sample only during the alpha '
                                                             'distribution phase',
                                                             'D) Any random time is equivalent for '
                                                             'interpretation'],
                                                 'answer': 'A) Avoid sampling in the distribution '
                                                           'phase; sample at steady state '
                                                           'appropriately',
                                                 'explanation': 'Digoxin distributes extensively '
                                                                'to tissues, so plasma levels '
                                                                'drawn too soon after a dose are '
                                                                'still falling through the '
                                                                'distribution phase and do not '
                                                                'reflect the post-distribution '
                                                                'concentration used for '
                                                                'interpretation. Therapeutic drug '
                                                                'monitoring therefore uses samples '
                                                                'at steady state, typically at '
                                                                'least 6–8 hours after a dose '
                                                                '(often a trough). Mis-timed '
                                                                'levels can prompt inappropriate '
                                                                'dose changes.'},
                                                {'question': 'Bioequivalence typically compares?',
                                                 'options': ['A) Tablet color and imprint code '
                                                             'only',
                                                             'B) AUC and Cmax within regulatory '
                                                             'limits',
                                                             'C) Melting point and crystal habit '
                                                             'only',
                                                             'D) Taste panel scores for oral '
                                                             'liquids'],
                                                 'answer': 'B) AUC and Cmax within regulatory '
                                                           'limits',
                                                 'explanation': 'Bioequivalence testing compares '
                                                                'rate and extent of absorption of '
                                                                'a test versus reference product, '
                                                                'primarily through AUC (extent) '
                                                                'and Cmax (rate) metrics. '
                                                                'Regulatory acceptance generally '
                                                                'requires the 90% confidence '
                                                                'interval for key pharmacokinetic '
                                                                'ratios to lie within predefined '
                                                                'limits (commonly 80–125%). '
                                                                'Demonstrated bioequivalence '
                                                                'underpins most generic '
                                                                'substitution decisions.'},
                                                {'question': 'Nonlinear binding plus saturable '
                                                             'clearance together can cause?',
                                                 'options': ['A) Strictly proportional '
                                                             'dose–concentration curves only',
                                                             'B) Elimination that is always '
                                                             'first-order forever',
                                                             'C) Complex dose–concentration '
                                                             'relationships',
                                                             'D) Complete absence of accumulation '
                                                             'on chronic dosing'],
                                                 'answer': 'C) Complex dose–concentration '
                                                           'relationships',
                                                 'explanation': 'When both plasma protein binding '
                                                                'and clearance pathways saturate, '
                                                                'free fraction, total '
                                                                'concentration, and elimination '
                                                                'rate can change together in a '
                                                                'dose-dependent manner. The '
                                                                'resulting relationship between '
                                                                'dose and exposure becomes '
                                                                'markedly nonlinear and '
                                                                'time-dependent. Such drugs '
                                                                'require cautious titration and '
                                                                'often specialized monitoring '
                                                                'rather than simple proportional '
                                                                'dose adjustments.'}]},
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
                                                             'B) Systemic absorption rate',
                                                             'C) Sustained-action release',
                                                             'D) Secondary amine rearrangement'],
                                                 'answer': 'A) Structure–activity relationship',
                                                 'explanation': 'Structure–activity relationships '
                                                                '(SAR) describe how systematic '
                                                                "changes in a molecule's "
                                                                'functional groups, scaffold, or '
                                                                'stereochemistry alter biological '
                                                                'potency, selectivity, or '
                                                                'toxicity. SAR analysis links '
                                                                'chemical features to target '
                                                                'binding and disposition. '
                                                                'Medicinal chemists use SAR to '
                                                                'optimize lead compounds toward '
                                                                'drug-like profiles.'},
                                                {'question': 'Prodrug is?',
                                                 'options': ['A) Already active drug given at '
                                                             'higher dose',
                                                             'B) Inactive form converted in vivo '
                                                             'to active drug',
                                                             'C) Active metabolite formed after '
                                                             'therapeutic failure',
                                                             'D) Excipient that enhances tablet '
                                                             'hardness'],
                                                 'answer': 'B) Inactive form converted in vivo to '
                                                           'active drug',
                                                 'explanation': 'A prodrug is a pharmacologically '
                                                                'inactive or less active '
                                                                'derivative that undergoes in vivo '
                                                                'biotransformation to release the '
                                                                'active parent drug. Common goals '
                                                                'include improving solubility, '
                                                                'permeability, stability, or '
                                                                'targeted activation. Ester and '
                                                                'phosphate prodrugs, for example, '
                                                                'are cleaved by hydrolases after '
                                                                'absorption or at the site of '
                                                                'action.'},
                                                {'question': 'pKa helps predict?',
                                                 'options': ['A) Crystal lattice energy of '
                                                             'polymorphs only',
                                                             'B) Tablet friability under shipping '
                                                             'stress',
                                                             'C) Ionization state at a given pH',
                                                             'D) Exact hepatic blood flow in '
                                                             'adults'],
                                                 'answer': 'C) Ionization state at a given pH',
                                                 'explanation': 'The pKa of an ionizable group '
                                                                'determines the equilibrium '
                                                                'between protonated and '
                                                                'deprotonated forms at a given pH '
                                                                'via the Henderson–Hasselbalch '
                                                                'relationship. Ionization state '
                                                                'strongly influences aqueous '
                                                                'solubility, membrane permeation, '
                                                                'and receptor recognition. '
                                                                'Predicting charged versus '
                                                                'uncharged fractions at '
                                                                'physiologic pH is therefore '
                                                                'central to absorption design.'}],
                                       'medium': [{'question': 'Beta-lactam ring is essential for?',
                                                   'options': ['A) Macrolide ribosomal binding '
                                                               'affinity',
                                                               'B) Aminoglycoside ototoxicity risk '
                                                               'only',
                                                               'C) Tetracycline chelation with '
                                                               'divalent metals',
                                                               'D) Antibacterial action of many '
                                                               'penicillins/cephalosporins'],
                                                   'answer': 'D) Antibacterial action of many '
                                                             'penicillins/cephalosporins',
                                                   'explanation': 'The strained β-lactam ring '
                                                                  'acylates serine residues in '
                                                                  'bacterial penicillin-binding '
                                                                  'proteins, irreversibly '
                                                                  'inhibiting cell-wall '
                                                                  'transpeptidation. Ring '
                                                                  'integrity is therefore '
                                                                  'essential for antibacterial '
                                                                  'activity of penicillins and '
                                                                  'cephalosporins. β-Lactamase '
                                                                  'enzymes hydrolyze the amide '
                                                                  'bond of the ring, conferring '
                                                                  'resistance unless a β-lactamase '
                                                                  'inhibitor or stable analog is '
                                                                  'used.'},
                                                  {'question': 'Chirality matters because?',
                                                   'options': ['A) Enantiomers can differ in '
                                                               'activity and toxicity',
                                                               'B) All enantiomers always have '
                                                               'identical ADME',
                                                               'C) Racemates cannot be formulated '
                                                               'as tablets',
                                                               'D) Optical rotation predicts '
                                                               'aqueous solubility alone'],
                                                   'answer': 'A) Enantiomers can differ in '
                                                             'activity and toxicity',
                                                   'explanation': 'Enantiomers are '
                                                                  'nonsuperimposable mirror-image '
                                                                  'stereoisomers that can interact '
                                                                  'differently with chiral '
                                                                  'biological targets such as '
                                                                  'receptors and enzymes. One '
                                                                  'enantiomer may provide most '
                                                                  'therapeutic activity while the '
                                                                  'other contributes little '
                                                                  'efficacy or distinct toxicity. '
                                                                  'Stereoselective metabolism and '
                                                                  'transport further differentiate '
                                                                  'clinical pharmacokinetics of '
                                                                  'many chiral drugs.'},
                                                  {'question': 'Bioisostere replacement aims to?',
                                                   'options': ['A) Destroy target binding to '
                                                               'reduce potency',
                                                               'B) Retain activity while improving '
                                                               'drug-like properties',
                                                               'C) Convert every drug into a '
                                                               'quaternary ammonium salt',
                                                               'D) Eliminate the need for any '
                                                               'metabolic soft spots'],
                                                   'answer': 'B) Retain activity while improving '
                                                             'drug-like properties',
                                                   'explanation': 'Bioisosteric replacement '
                                                                  'substitutes an atom or group '
                                                                  'with another of similar steric '
                                                                  'and electronic character to '
                                                                  'retain target affinity while '
                                                                  'modulating ADME or toxicity. '
                                                                  'Classic examples include '
                                                                  'replacing hydrogen with '
                                                                  'fluorine or a carboxylic acid '
                                                                  'with a tetrazole. The tactic is '
                                                                  'used to improve potency, '
                                                                  'selectivity, metabolic '
                                                                  'stability, or physicochemical '
                                                                  'properties.'}],
                                       'hard': [{'question': 'Log D differs from log P by?',
                                                 'options': ['A) Ignoring lipophilicity entirely',
                                                             'B) Using only melting point as the '
                                                             'input',
                                                             'C) Accounting for ionization at a '
                                                             'specified pH',
                                                             'D) Measuring only solid-state '
                                                             'polymorphism'],
                                                 'answer': 'C) Accounting for ionization at a '
                                                           'specified pH',
                                                 'explanation': 'Log P describes partitioning of '
                                                                'the purely unionized species, '
                                                                'whereas log D is the pH-dependent '
                                                                'distribution coefficient '
                                                                'including all ionized and '
                                                                'unionized forms present at that '
                                                                'pH. At physiologic pH, ionized '
                                                                'fractions often dominate for '
                                                                'acids and bases, so log D is '
                                                                'frequently more relevant to '
                                                                'membrane permeation. Comparing '
                                                                'log D across pH values maps '
                                                                'ionization-sensitive '
                                                                'lipophilicity.'},
                                                {'question': 'Suicide substrate / mechanism-based '
                                                             'inhibitor?',
                                                 'options': ['A) Binds reversibly without chemical '
                                                             'activation by the enzyme',
                                                             'B) Competes only at an allosteric '
                                                             'site with no turnover',
                                                             'C) Induces CYP expression without '
                                                             'engaging the target enzyme',
                                                             'D) Requires enzyme activation then '
                                                             'inactivates the enzyme'],
                                                 'answer': 'D) Requires enzyme activation then '
                                                           'inactivates the enzyme',
                                                 'explanation': 'A mechanism-based (suicide) '
                                                                'inhibitor is chemically '
                                                                'transformed by the target enzyme '
                                                                'into a reactive species that then '
                                                                'covalently inactivates that '
                                                                'enzyme. Catalytic turnover is '
                                                                'therefore required before '
                                                                'irreversible inhibition occurs. '
                                                                'This distinguishes suicide '
                                                                'substrates from simple reversible '
                                                                'competitive inhibitors that need '
                                                                'no enzymatic activation.'},
                                                {'question': 'Hansch analysis relates?',
                                                 'options': ['A) Physicochemical parameters to '
                                                             'biological activity',
                                                             'B) Tablet punch speed to content '
                                                             'uniformity only',
                                                             'C) NMR chemical shifts to film-coat '
                                                             'color only',
                                                             'D) Sterility assurance to autoclave '
                                                             'load size only'],
                                                 'answer': 'A) Physicochemical parameters to '
                                                           'biological activity',
                                                 'explanation': 'Hansch analysis is an early '
                                                                'quantitative structure–activity '
                                                                'relationship (QSAR) approach '
                                                                'correlating biological activity '
                                                                'with physicochemical descriptors '
                                                                'such as hydrophobic (π), '
                                                                'electronic (σ), and steric terms. '
                                                                'Regression models relate these '
                                                                'parameters to potency across a '
                                                                'congeneric series. It provided a '
                                                                'foundation for modern '
                                                                'computational QSAR and '
                                                                'property-based optimization.'}],
                                       'extreme': [{'question': 'Hard drug vs soft drug concepts?',
                                                    'options': ['A) Hard drugs always lack any '
                                                                'metabolic pathway forever',
                                                                'B) Soft drugs are designed for '
                                                                'predictable metabolism to '
                                                                'inactive metabolites',
                                                                'C) Soft drugs cannot be given '
                                                                'orally under any circumstance',
                                                                'D) Hard drugs are defined only by '
                                                                'tablet crushing strength'],
                                                    'answer': 'B) Soft drugs are designed for '
                                                              'predictable metabolism to inactive '
                                                              'metabolites',
                                                    'explanation': 'Soft drugs are active '
                                                                   'compounds deliberately '
                                                                   'designed to undergo rapid, '
                                                                   'predictable metabolism to '
                                                                   'inactive metabolites after '
                                                                   'exerting their effect, '
                                                                   'limiting systemic burden. Hard '
                                                                   'drugs, in contrast, are '
                                                                   'structurally resistant to '
                                                                   'metabolism or yield '
                                                                   'metabolites that remain '
                                                                   'active. Soft-drug design is a '
                                                                   'metabolism-based strategy to '
                                                                   'widen safety margins and '
                                                                   'control duration of action.'},
                                                   {'question': 'Covalent warheads in targeted '
                                                                'covalent inhibitors need?',
                                                    'options': ['A) Random reactivity with every '
                                                                'nucleophile in plasma',
                                                                'B) Complete avoidance of any '
                                                                'electrophile forever',
                                                                'C) Careful selectivity to limit '
                                                                'off-target binding',
                                                                'D) Mandatory permanent binding to '
                                                                'albumin only'],
                                                    'answer': 'C) Careful selectivity to limit '
                                                              'off-target binding',
                                                    'explanation': 'Targeted covalent inhibitors '
                                                                   'use an electrophilic warhead '
                                                                   'to form a bond with a '
                                                                   'nucleophilic residue (often '
                                                                   'cysteine) near the binding '
                                                                   'site after reversible '
                                                                   'recognition. Selectivity '
                                                                   'depends on both noncovalent '
                                                                   'binding complementarity and '
                                                                   'warhead reactivity matched to '
                                                                   'the intended residue. '
                                                                   'Excessive reactivity increases '
                                                                   'off-target covalent '
                                                                   'modification and toxicity '
                                                                   'risk.'},
                                                   {'question': 'PROTACs act by?',
                                                    'options': ['A) Competitively blocking only '
                                                                'orthosteric agonists',
                                                                'B) Irreversibly alkylating DNA in '
                                                                'all cells',
                                                                'C) Inhibiting only extracellular '
                                                                'ligand diffusion',
                                                                'D) Hijacking degradation '
                                                                'machinery to degrade target '
                                                                'proteins'],
                                                    'answer': 'D) Hijacking degradation machinery '
                                                              'to degrade target proteins',
                                                    'explanation': 'Proteolysis-targeting chimeras '
                                                                   '(PROTACs) are bifunctional '
                                                                   'molecules that simultaneously '
                                                                   'bind a target protein and an '
                                                                   'E3 ubiquitin ligase. Induced '
                                                                   'proximity leads to '
                                                                   'ubiquitination and proteasomal '
                                                                   'degradation of the target '
                                                                   'rather than simple '
                                                                   'occupancy-based inhibition. '
                                                                   'Because degradation can be '
                                                                   'catalytic, PROTACs represent '
                                                                   'an event-driven pharmacology '
                                                                   'modality.'}]},
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
                                           'options': ['A) Only synthetic industrial dye chemistry',
                                                       'B) Only hospital IV pump programming',
                                                       'C) Only clinical trial statistics methods',
                                                       'D) Medicines derived from natural sources'],
                                           'answer': 'D) Medicines derived from natural sources',
                                           'explanation': 'Pharmacognosy is the pharmaceutical '
                                                          'science concerned with medicines '
                                                          'derived from natural sources, including '
                                                          'plants, microbes, fungi, and marine '
                                                          'organisms. It covers identification, '
                                                          'chemistry, biosynthesis, quality, and '
                                                          'biological activity of natural '
                                                          'products. Many modern drugs originated '
                                                          'as purified or semi-synthetic natural '
                                                          'compounds.'},
                                          {'question': 'Digitalis historically relates to?',
                                           'options': ['A) Cardiac glycosides from foxglove',
                                                       'B) Opioid alkaloids from poppy latex',
                                                       'C) Antimalarial quinine from cinchona only',
                                                       'D) Local anesthetic cocaine from coca leaf '
                                                       'only'],
                                           'answer': 'A) Cardiac glycosides from foxglove',
                                           'explanation': 'Digitalis species yield cardenolide '
                                                          'cardiac glycosides such as digoxin and '
                                                          'digitoxin that inhibit the '
                                                          'Na+/K+-ATPase. The resulting rise in '
                                                          'intracellular sodium reduces calcium '
                                                          'extrusion via NCX, increasing cardiac '
                                                          'contractile force. Historically, '
                                                          'foxglove preparations were among the '
                                                          'earliest standardized natural cardiac '
                                                          'therapies.'},
                                          {'question': 'Alkaloids are typically?',
                                           'options': ['A) Neutral polysaccharides without '
                                                       'nitrogen',
                                                       'B) Nitrogen-containing natural bases',
                                                       'C) Simple inorganic mineral salts only',
                                                       'D) Volatile hydrocarbon oils exclusively'],
                                           'answer': 'B) Nitrogen-containing natural bases',
                                           'explanation': 'Alkaloids are typically basic, '
                                                          'nitrogen-containing secondary '
                                                          'metabolites produced by plants and '
                                                          'other organisms. The nitrogen often '
                                                          'resides in a heterocyclic ring and '
                                                          'confers characteristic solubility and '
                                                          'receptor activity. Morphine, quinine, '
                                                          'atropine, and caffeine illustrate the '
                                                          'pharmacologic diversity of alkaloid '
                                                          'natural products.'}],
                                 'medium': [{'question': "St John's wort interaction theme?",
                                             'options': ['A) CYP inhibition raising all drug '
                                                         'levels equally',
                                                         'B) Complete blockade of renal drug '
                                                         'excretion',
                                                         'C) CYP induction reducing many substrate '
                                                         'drug levels',
                                                         'D) Neutralization of gastric acid only'],
                                             'answer': 'C) CYP induction reducing many substrate '
                                                       'drug levels',
                                             'explanation': "Hypericum perforatum (St John's wort) "
                                                            'induces CYP3A4 and P-glycoprotein via '
                                                            'pregnane X receptor activation, '
                                                            'accelerating clearance of many '
                                                            'substrates. Plasma concentrations of '
                                                            'drugs such as some oral '
                                                            'contraceptives, immunosuppressants, '
                                                            'and antiretrovirals can fall below '
                                                            'therapeutic levels. The interaction '
                                                            'is a classic inductive herb–drug '
                                                            'interaction with loss-of-efficacy '
                                                            'risk.'},
                                            {'question': 'Secondary metabolites serve plants often '
                                                         'as?',
                                             'options': ['A) Primary energy stores like starch '
                                                         'only',
                                                         'B) Structural cellulose replacement only',
                                                         'C) Photosynthetic pigments exclusively',
                                                         'D) Defense or attraction chemicals; '
                                                         'humans may use as drugs'],
                                             'answer': 'D) Defense or attraction chemicals; humans '
                                                       'may use as drugs',
                                             'explanation': 'Secondary metabolites are organic '
                                                            'compounds not required for basic '
                                                            'plant growth and primary metabolism '
                                                            'but often mediating defense, '
                                                            'signaling, or pollinator attraction. '
                                                            'Humans exploit many of these '
                                                            'molecules—alkaloids, terpenoids, '
                                                            'phenolics, and glycosides—as drugs or '
                                                            'leads. Their ecological roles help '
                                                            'explain the prevalence of potent '
                                                            'bioactivity in medicinal plants.'},
                                            {'question': 'Standardization of herbal drugs aims to?',
                                             'options': ['A) Consistent content of marker or '
                                                         'active constituents',
                                                         'B) Random seasonal variation without '
                                                         'assay',
                                                         'C) Maximum bitterness as the sole '
                                                         'quality metric',
                                                         'D) Elimination of all secondary '
                                                         'metabolites'],
                                             'answer': 'A) Consistent content of marker or active '
                                                       'constituents',
                                             'explanation': 'Herbal drug standardization seeks '
                                                            'reproducible levels of marker '
                                                            'compounds or known actives across '
                                                            'batches of crude drugs or extracts. '
                                                            'Chemical assays, chromatographic '
                                                            'fingerprints, and botanical '
                                                            'identification reduce variability '
                                                            'from species, season, and processing. '
                                                            'Consistent constituent content is a '
                                                            'prerequisite for predictable '
                                                            'pharmacologic effect and quality '
                                                            'control.'}],
                                 'hard': [{'question': 'Microbial natural products gave us many?',
                                           'options': ['A) Inhaled beta-agonist bronchodilators',
                                                       'B) Antibiotics such as penicillins and '
                                                       'aminoglycosides',
                                                       'C) Synthetic ACE inhibitors only',
                                                       'D) Monoclonal antibodies from hybridomas '
                                                       'only'],
                                           'answer': 'B) Antibiotics such as penicillins and '
                                                     'aminoglycosides',
                                           'explanation': 'Microbial secondary metabolism has '
                                                          'supplied a large fraction of clinical '
                                                          'antibiotics, beginning with penicillin '
                                                          'from Penicillium and extending to '
                                                          'aminoglycosides, macrolides, '
                                                          'tetracyclines, and many others. '
                                                          'Actinomycetes and fungi remain major '
                                                          'sources of antibacterial scaffolds. '
                                                          'Semi-synthesis from microbial natural '
                                                          'products continues to expand spectrum '
                                                          'and overcome resistance.'},
                                          {'question': 'Adulteration of herbal products may '
                                                       'involve?',
                                           'options': ['A) Only improved drying under GMP',
                                                       'B) Only correct Latin binomial labeling',
                                                       'C) Wrong species, heavy metals, or '
                                                       'undeclared drugs',
                                                       'D) Only validated marker assay '
                                                       'certificates'],
                                           'answer': 'C) Wrong species, heavy metals, or '
                                                     'undeclared drugs',
                                           'explanation': 'Herbal product adulteration may '
                                                          'substitute incorrect species, add heavy '
                                                          'metals from contaminated soil or '
                                                          'processing, or illegally spike '
                                                          'undeclared synthetic drugs. Such '
                                                          'practices create toxicity, '
                                                          'hypersensitivity, and unexpected '
                                                          'pharmacologic effects. Authentication '
                                                          '(macroscopy, microscopy, DNA barcoding, '
                                                          'analytics) is therefore essential for '
                                                          'patient safety.'},
                                          {'question': 'Phytochemical screening tests detect '
                                                       'classes like?',
                                           'options': ['A) Only elemental sodium and potassium',
                                                       'B) Only residual organic solvents',
                                                       'C) Only tablet hardness and friability',
                                                       'D) Alkaloids, flavonoids, saponins, and '
                                                       'related classes'],
                                           'answer': 'D) Alkaloids, flavonoids, saponins, and '
                                                     'related classes',
                                           'explanation': 'Phytochemical screening uses '
                                                          'colorimetric and precipitation tests to '
                                                          'detect major natural-product classes '
                                                          'such as alkaloids, flavonoids, '
                                                          'saponins, tannins, and cardiac '
                                                          'glycosides in extracts. These assays '
                                                          'provide rapid preliminary '
                                                          'characterization before chromatographic '
                                                          'isolation. Positive screens guide '
                                                          'subsequent targeted extraction and '
                                                          'structural elucidation.'}],
                                 'extreme': [{'question': 'Aristolochic acid concern?',
                                              'options': ['A) Nephrotoxicity and carcinogenicity '
                                                          'in some botanicals',
                                                          'B) Reversible anticholinergic dryness '
                                                          'as the main toxicity',
                                                          'C) Dose-dependent serotonin syndrome '
                                                          'from MAO inhibition',
                                                          'D) Beneficial CYP3A4 induction raising '
                                                          'digoxin effect'],
                                              'answer': 'A) Nephrotoxicity and carcinogenicity in '
                                                        'some botanicals',
                                              'explanation': 'Aristolochic acids from Aristolochia '
                                                             'and related botanicals form DNA '
                                                             'adducts after nitroreduction and are '
                                                             'established nephrotoxins and '
                                                             'carcinogens. Exposure is linked to '
                                                             'aristolochic acid nephropathy and '
                                                             'urothelial carcinoma. Regulatory '
                                                             'bans and warnings reflect this '
                                                             'mechanism-based genotoxic risk in '
                                                             'certain traditional preparations.'},
                                             {'question': 'Aflatoxins in crude drugs are?',
                                              'options': ['A) Plant primary metabolites essential '
                                                          'for growth',
                                                          'B) Fungal toxins posing contamination '
                                                          'risk',
                                                          'C) Inorganic heavy-metal antidotes',
                                                          'D) Sterile filtration validation '
                                                          'markers'],
                                              'answer': 'B) Fungal toxins posing contamination '
                                                        'risk',
                                              'explanation': 'Aflatoxins are difuranocoumarin '
                                                             'mycotoxins produced mainly by '
                                                             'Aspergillus flavus and A. '
                                                             'parasiticus contaminating improperly '
                                                             'stored plant materials. Aflatoxin B1 '
                                                             'is metabolically activated to an '
                                                             'epoxide that binds DNA and is a '
                                                             'potent hepatocarcinogen. Crude drug '
                                                             'quality control therefore includes '
                                                             'limits and testing for fungal toxin '
                                                             'contamination.'},
                                             {'question': 'Ethnopharmacology contributes by?',
                                              'options': ['A) Replacing all clinical trials with '
                                                          'folklore alone',
                                                          'B) Ignoring traditional use during '
                                                          'discovery',
                                                          'C) Studying traditional use to guide '
                                                          'drug discovery',
                                                          'D) Mandating synthetic routes for every '
                                                          'natural product'],
                                              'answer': 'C) Studying traditional use to guide drug '
                                                        'discovery',
                                              'explanation': 'Ethnopharmacology investigates '
                                                             'traditional medicinal uses of '
                                                             'organisms within cultural contexts '
                                                             'to generate hypotheses for bioactive '
                                                             'compound discovery. Historical use '
                                                             'can prioritize species for '
                                                             'extraction and bioassay, but '
                                                             'traditional claims still require '
                                                             'chemical isolation, mechanistic '
                                                             'study, and clinical evidence. It is '
                                                             'a discovery guide, not proof of '
                                                             'efficacy or safety alone.'}]},
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
                                                           'frequency, and prescriber details',
                                                           'B) Only the drug name without strength '
                                                           'or directions',
                                                           'C) Only the pharmacy stamp date',
                                                           'D) Only the wholesaler invoice number'],
                                               'answer': 'A) Patient, drug, dose, route, '
                                                         'frequency, and prescriber details',
                                               'explanation': 'Legal and clinical prescription '
                                                              'review confirms that the patient '
                                                              'identity, medicine, strength, dose, '
                                                              'route, frequency, and prescriber '
                                                              'details are complete and '
                                                              'appropriate. Ambiguity or missing '
                                                              'elements can lead to wrong-drug or '
                                                              'wrong-dose errors. Pharmacists also '
                                                              'screen for contraindications and '
                                                              'interactions as part of safe '
                                                              'dispensing.'},
                                              {'question': 'OTC counseling should cover?',
                                               'options': ['A) Unlimited refill advice without '
                                                           'referral criteria',
                                                           'B) Indication limits, dose, warnings, '
                                                           'and when to refer',
                                                           'C) Encouraging use beyond labeled '
                                                           'maximum always',
                                                           'D) Sharing leftover packs with family '
                                                           'members'],
                                               'answer': 'B) Indication limits, dose, warnings, '
                                                         'and when to refer',
                                               'explanation': 'Over-the-counter counseling defines '
                                                              'the intended self-limiting '
                                                              'indication, correct dose and '
                                                              'duration, key warnings, and '
                                                              'red-flag symptoms that require '
                                                              'referral. This ensures responsible '
                                                              'self-care and reduces delayed '
                                                              'diagnosis of serious disease. '
                                                              'Product selection should match '
                                                              'symptom pattern, comorbidities, and '
                                                              'interacting medicines.'},
                                              {'question': 'Controlled drugs require?',
                                               'options': ['A) No special records beyond ordinary '
                                                           'OTC sales',
                                                           'B) Display on open self-selection '
                                                           'shelves only',
                                                           'C) Extra legal storage and record '
                                                           'controls per law',
                                                           'D) Verbal orders without any '
                                                           'documentation'],
                                               'answer': 'C) Extra legal storage and record '
                                                         'controls per law',
                                               'explanation': 'Controlled drugs are substances '
                                                              'with recognized abuse or dependence '
                                                              'potential and are subject to '
                                                              'heightened legal controls on '
                                                              'prescribing, storage, recording, '
                                                              'and destruction. Requirements vary '
                                                              'by jurisdiction but typically '
                                                              'include secure custody and '
                                                              'auditable registers. Compliance '
                                                              'protects patients and limits '
                                                              'diversion into illicit supply.'}],
                                     'medium': [{'question': 'Near miss reporting helps?',
                                                 'options': ['A) Punish staff without system '
                                                             'analysis',
                                                             'B) Hide process weaknesses from '
                                                             'managers',
                                                             'C) Replace all incident reviews with '
                                                             'silence',
                                                             'D) System learning without waiting '
                                                             'for patient harm'],
                                                 'answer': 'D) System learning without waiting for '
                                                           'patient harm',
                                                 'explanation': 'A near miss is an error that is '
                                                                'intercepted before it reaches the '
                                                                'patient or causes harm. Reporting '
                                                                'near misses reveals latent system '
                                                                'weaknesses—look-alike packaging, '
                                                                'workflow interruptions, or '
                                                                'unclear protocols—without waiting '
                                                                'for injury. Analysis supports '
                                                                'corrective actions that '
                                                                'strengthen medication-safety '
                                                                'culture.'},
                                                {'question': 'Generic substitution depends on?',
                                                 'options': ['A) Local law/formulary and clinical '
                                                             'appropriateness',
                                                             'B) Patient preference for tablet '
                                                             'color only',
                                                             'C) Wholesaler stock photos alone',
                                                             'D) Always substituting regardless of '
                                                             'narrow therapeutic index'],
                                                 'answer': 'A) Local law/formulary and clinical '
                                                           'appropriateness',
                                                 'explanation': 'Generic substitution replaces a '
                                                                'brand product with a '
                                                                'bioequivalent generic containing '
                                                                'the same active substance when '
                                                                'law and formulary policy allow. '
                                                                'Clinical appropriateness still '
                                                                'matters for narrow '
                                                                'therapeutic-index drugs, '
                                                                'modified-release forms, and '
                                                                'patient-specific concerns. '
                                                                'Pharmacists apply local rules '
                                                                'while ensuring therapeutic '
                                                                'equivalence and continuity of '
                                                                'effect.'},
                                                {'question': 'Privacy in pharmacy means?',
                                                 'options': ['A) Discussing therapy loudly at the '
                                                             'counter for teaching',
                                                             'B) Protecting patient confidential '
                                                             'information',
                                                             'C) Posting prescriptions on social '
                                                             'media for advice',
                                                             'D) Sharing full histories with '
                                                             'unrelated third parties'],
                                                 'answer': 'B) Protecting patient confidential '
                                                           'information',
                                                 'explanation': 'Pharmacy privacy obligations '
                                                                'protect confidential health '
                                                                'information from unauthorized '
                                                                'disclosure under professional '
                                                                'ethics and data-protection law. '
                                                                'Counseling should occur with '
                                                                'reasonable auditory privacy, and '
                                                                'records access must be limited to '
                                                                'legitimate care needs. Breaches '
                                                                'can harm patients and undermine '
                                                                'trust in pharmaceutical care.'}],
                                     'hard': [{'question': 'Emergency supply frameworks (where '
                                                           'legal) require?',
                                               'options': ['A) Dispensing any CD without records '
                                                           'if the patient asks',
                                                           'B) Ignoring all documentation to save '
                                                           'time',
                                                           'C) Professional judgment, legal '
                                                           'criteria, and documentation',
                                                           'D) Supplying unlimited quantities for '
                                                           'twelve months'],
                                               'answer': 'C) Professional judgment, legal '
                                                         'criteria, and documentation',
                                               'explanation': 'Where emergency supply without a '
                                                              'current prescription is legally '
                                                              'permitted, pharmacists apply '
                                                              'statutory criteria such as prior '
                                                              'treatment, appropriate indication, '
                                                              'and quantity limits. Professional '
                                                              'judgment assesses clinical risk if '
                                                              'supply is deferred versus provided. '
                                                              'Documentation of assessment and '
                                                              'supply is required for '
                                                              'accountability and continuity with '
                                                              'the usual prescriber.'},
                                              {'question': 'Antimicrobial stewardship in community '
                                                           'includes?',
                                               'options': ['A) Recommending antibiotics for all '
                                                           'viral colds',
                                                           'B) Pressure to complete leftover '
                                                           'courses from prior illnesses',
                                                           'C) Automatic OTC antibiotic sales '
                                                           'without assessment',
                                                           'D) Avoiding unnecessary antibiotics, '
                                                           'counseling adherence, referring '
                                                           'appropriately'],
                                               'answer': 'D) Avoiding unnecessary antibiotics, '
                                                         'counseling adherence, referring '
                                                         'appropriately',
                                               'explanation': 'Community antimicrobial stewardship '
                                                              'reduces unnecessary antibacterial '
                                                              'exposure that selects for resistant '
                                                              'organisms. Pharmacists counsel on '
                                                              'adherence when antibiotics are '
                                                              'indicated, avoid endorsing '
                                                              'antibiotics for viral self-limiting '
                                                              'illness, and refer patients with '
                                                              'red-flag infections. These actions '
                                                              'preserve antibiotic effectiveness '
                                                              'at a population level.'},
                                              {'question': 'Health promotion role example?',
                                               'options': ['A) Smoking cessation support',
                                                           'B) Refusing all public-health '
                                                           'conversations',
                                                           'C) Promoting unproven detox kits as '
                                                           'first-line',
                                                           'D) Replacing vaccines with herbal '
                                                           'tonics routinely'],
                                               'answer': 'A) Smoking cessation support',
                                               'explanation': 'Smoking cessation support is a core '
                                                              'health-promotion role in pharmacy '
                                                              'practice, combining behavioral '
                                                              'advice with evidence-based '
                                                              'pharmacotherapy such as nicotine '
                                                              'replacement, varenicline, or '
                                                              'bupropion where appropriate. '
                                                              'Nicotine addiction is mediated by '
                                                              'dopaminergic reinforcement pathways '
                                                              'that cessation medicines help '
                                                              'modulate. Reducing tobacco use '
                                                              'lowers cardiovascular, pulmonary, '
                                                              'and cancer risk.'}],
                                     'extreme': [{'question': 'Suspected forged CD prescription?',
                                                  'options': ['A) Dispense quickly to avoid '
                                                              'confrontation',
                                                              'B) Do not dispense; verify and '
                                                              'report per legal pathway',
                                                              'C) Alter the prescription to a '
                                                              'weaker opioid yourself',
                                                              'D) Give a partial supply without '
                                                              'any record'],
                                                  'answer': 'B) Do not dispense; verify and report '
                                                            'per legal pathway',
                                                  'explanation': 'Suspected forged or fraudulent '
                                                                 'controlled-drug prescriptions '
                                                                 'raise diversion and '
                                                                 'patient-safety risks if '
                                                                 'dispensed. Pharmacists must not '
                                                                 'supply when authenticity cannot '
                                                                 'be established and should verify '
                                                                 'with the purported prescriber '
                                                                 'and follow legal reporting '
                                                                 'pathways. This protects '
                                                                 'legitimate patients while '
                                                                 'interrupting illicit acquisition '
                                                                 'of controlled substances.'},
                                                 {'question': 'Child dosing error risk mitigation?',
                                                  'options': ['A) Estimate dose from adult tablets '
                                                              'by eye only',
                                                              'B) Ignore maximum dose caps if the '
                                                              'child is tall',
                                                              'C) mg/kg checks, max dose caps, and '
                                                              'double-checks when required',
                                                              'D) Use household spoons as the only '
                                                              'measuring device'],
                                                  'answer': 'C) mg/kg checks, max dose caps, and '
                                                            'double-checks when required',
                                                  'explanation': 'Pediatric doses are commonly '
                                                                 'calculated on a mg/kg (or mg/m²) '
                                                                 'basis because clearance and '
                                                                 'volume of distribution scale '
                                                                 'with size and maturation. '
                                                                 'Maximum dose caps prevent '
                                                                 'exceeding adult or '
                                                                 'product-labeled limits when '
                                                                 'weight-based math would '
                                                                 'overshoot. Independent '
                                                                 'double-checks reduce arithmetic '
                                                                 'and decimal-point errors that '
                                                                 'are especially hazardous in '
                                                                 'children.'},
                                                 {'question': 'Vaccine fridge excursion requires?',
                                                  'options': ['A) Immediate use of all vials '
                                                              'without assessment',
                                                              'B) Discard silently without '
                                                              'documentation',
                                                              'C) Return to stock as soon as the '
                                                              'fridge feels cold',
                                                              'D) Quarantine stock and follow '
                                                              'cold-chain protocol before use'],
                                                  'answer': 'D) Quarantine stock and follow '
                                                            'cold-chain protocol before use',
                                                  'explanation': 'Vaccines are '
                                                                 'temperature-sensitive biologics; '
                                                                 'excursions outside the labeled '
                                                                 'cold-chain range can denature '
                                                                 'antigens and reduce potency. '
                                                                 'Affected stock is quarantined '
                                                                 'and evaluated against stability '
                                                                 'data and public-health protocols '
                                                                 'before any release or discard '
                                                                 'decision. Using compromised '
                                                                 'vaccine risks failed '
                                                                 'immunization and false '
                                                                 'reassurance of protection.'}]},
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
                                               'options': ['A) Increase ward stockpiles of '
                                                           'multidose bottles',
                                                           'B) Reduce medication errors and waste',
                                                           'C) Eliminate pharmacist review of '
                                                           'orders',
                                                           'D) Replace all oral meds with IV '
                                                           'formulations'],
                                               'answer': 'B) Reduce medication errors and waste',
                                               'explanation': 'Unit-dose distribution dispenses '
                                                              'individually packaged, '
                                                              'ready-to-administer doses labeled '
                                                              'for a specific patient and '
                                                              'administration time. This reduces '
                                                              'ward stock manipulation, wrong-dose '
                                                              'selection, and wastage from unused '
                                                              'multidose supplies. The system '
                                                              'supports nurse verification against '
                                                              'the medication administration '
                                                              'record.'},
                                              {'question': 'IV admixture service focuses on?',
                                               'options': ['A) Only outpatient OTC counseling',
                                                           'B) Only tablet repackaging into '
                                                           'bottles',
                                                           'C) Aseptic compounding of injectable '
                                                           'preparations',
                                                           'D) Only narcotic vault inventory '
                                                           'counting'],
                                               'answer': 'C) Aseptic compounding of injectable '
                                                         'preparations',
                                               'explanation': 'An IV admixture service compounds '
                                                              'sterile parenteral preparations '
                                                              'under controlled aseptic '
                                                              'conditions, verifying calculations, '
                                                              'diluents, and compatibility. The '
                                                              'aim is to prevent microbial '
                                                              'contamination and particulate or '
                                                              'chemical incompatibility in '
                                                              'intravenous medicines. Centralized '
                                                              'aseptic compounding also '
                                                              'standardizes labeling and '
                                                              'beyond-use dating.'},
                                              {'question': 'Formulary manages?',
                                               'options': ['A) Nurse staffing ratios on medical '
                                                           'wards',
                                                           'B) Operating-room surgical instrument '
                                                           'trays',
                                                           'C) Ambulance response time targets',
                                                           'D) Which medicines are stocked and '
                                                           'approved for use'],
                                               'answer': 'D) Which medicines are stocked and '
                                                         'approved for use',
                                               'explanation': "A formulary is the institution's "
                                                              'approved list of medicines selected '
                                                              'for efficacy, safety, and '
                                                              'cost-effectiveness relative to '
                                                              'therapeutic alternatives. Pharmacy '
                                                              'and therapeutics processes evaluate '
                                                              'evidence and restrict nonformulary '
                                                              'use. Formulary management shapes '
                                                              'prescribing patterns and inventory '
                                                              'control in the hospital.'}],
                                     'medium': [{'question': 'TPN compounding requires?',
                                                 'options': ['A) Aseptic technique plus stability '
                                                             'and compatibility checks',
                                                             'B) Open-bench mixing without '
                                                             'sterility controls',
                                                             'C) Ignoring calcium–phosphate '
                                                             'precipitation risk',
                                                             'D) Adding all vitamins before '
                                                             'autoclaving the bag'],
                                                 'answer': 'A) Aseptic technique plus stability '
                                                           'and compatibility checks',
                                                 'explanation': 'Total parenteral nutrition '
                                                                'admixtures combine amino acids, '
                                                                'dextrose, lipid emulsions, '
                                                                'electrolytes, vitamins, and trace '
                                                                'elements in complex '
                                                                'physicochemical systems. Aseptic '
                                                                'technique prevents bloodstream '
                                                                'infection, while compatibility '
                                                                'and stability checks avoid '
                                                                'precipitation (for example '
                                                                'calcium–phosphate) and emulsion '
                                                                'cracking. Order review must also '
                                                                'match nutrient provision to '
                                                                'metabolic status.'},
                                                {'question': 'Antimicrobial stewardship rounds '
                                                             'include pharmacists to?',
                                                 'options': ['A) Increase duration of every '
                                                             'empiric regimen',
                                                             'B) Optimize antimicrobial choice, '
                                                             'dose, and duration',
                                                             'C) Stop all cultures before '
                                                             'reviewing therapy',
                                                             'D) Switch all patients to the '
                                                             'broadest IV agent'],
                                                 'answer': 'B) Optimize antimicrobial choice, '
                                                           'dose, and duration',
                                                 'explanation': 'Antimicrobial stewardship rounds '
                                                                'use multidisciplinary review to '
                                                                'optimize drug choice, dose, '
                                                                'route, and duration against '
                                                                'culture data and infection '
                                                                'syndromes. Pharmacists contribute '
                                                                'pharmacokinetic dosing, '
                                                                'IV-to-oral switch, and '
                                                                'de-escalation expertise. The '
                                                                'goals are improved clinical '
                                                                'outcomes and reduced selection '
                                                                'pressure for antimicrobial '
                                                                'resistance.'},
                                                {'question': 'Medication error disclosure ethics?',
                                                 'options': ['A) Conceal errors to protect '
                                                             'institutional reputation',
                                                             'B) Blame only the most junior staff '
                                                             'member publicly',
                                                             'C) Be honest with patient and team '
                                                             'per policy',
                                                             'D) Alter charts so the error cannot '
                                                             'be traced'],
                                                 'answer': 'C) Be honest with patient and team per '
                                                           'policy',
                                                 'explanation': 'Ethical medication-error '
                                                                'disclosure requires honest '
                                                                'communication with the patient '
                                                                'and care team according to '
                                                                'institutional policy once an '
                                                                'error is recognized. Transparency '
                                                                'enables timely clinical '
                                                                'mitigation and supports learning '
                                                                'systems rather than individual '
                                                                'blame alone. Concealing errors '
                                                                'undermines autonomy, safety '
                                                                'improvement, and professional '
                                                                'trust.'}],
                                     'hard': [{'question': 'Clean room grades/air quality matter '
                                                           'for?',
                                               'options': ['A) Only outpatient waiting-room '
                                                           'comfort',
                                                           'B) Only tablet bottle labeling speed',
                                                           'C) Only courier delivery temperature '
                                                           'logs',
                                                           'D) Aseptic preparation contamination '
                                                           'risk control'],
                                               'answer': 'D) Aseptic preparation contamination '
                                                         'risk control',
                                               'explanation': 'Cleanroom grade classifications '
                                                              'specify airborne particulate limits '
                                                              'and air-handling performance for '
                                                              'aseptic preparation areas. '
                                                              'Higher-grade environments (with '
                                                              'HEPA filtration and pressure '
                                                              'cascades) reduce contamination risk '
                                                              'during sterile compounding. '
                                                              'Environmental monitoring and '
                                                              'gowning discipline translate these '
                                                              'engineering controls into microbial '
                                                              'risk reduction for parenteral '
                                                              'products.'},
                                              {'question': 'Smart pump libraries reduce?',
                                               'options': ['A) Infusion programming and '
                                                           'dosing-limit errors',
                                                           'B) Need for any drug concentration '
                                                           'standardization',
                                                           'C) Pharmacist verification of '
                                                           'high-alert infusions',
                                                           'D) Use of soft and hard dose alerts '
                                                           'entirely'],
                                               'answer': 'A) Infusion programming and dosing-limit '
                                                         'errors',
                                               'explanation': 'Smart-pump drug libraries encode '
                                                              'standardized concentrations, dosing '
                                                              'units, and soft/hard limits for '
                                                              'intravenous infusions. When '
                                                              'clinicians select a library entry, '
                                                              'the pump constrains programming '
                                                              'that would otherwise allow 10-fold '
                                                              'overdoses or unit mismatches. '
                                                              'Technology thus reduces infusion '
                                                              'programming errors when libraries '
                                                              'are current and used.'},
                                              {'question': 'Recall management requires?',
                                               'options': ['A) Continuing to dispense recalled '
                                                           'batches until empty',
                                                           'B) Quarantine affected batches and '
                                                           'trace patients if needed',
                                                           'C) Relabeling recalled stock with a '
                                                           'new expiry only',
                                                           'D) Ignoring supplier notices for '
                                                           'slow-moving items'],
                                               'answer': 'B) Quarantine affected batches and trace '
                                                         'patients if needed',
                                               'explanation': 'Medicine recalls remove or restrict '
                                                              'batches with quality defects, '
                                                              'contamination, or safety signals. '
                                                              'Hospital pharmacy must quarantine '
                                                              'affected stock, stop further '
                                                              'dispensing, and trace patients who '
                                                              'already received implicated packs '
                                                              'when clinical risk warrants. Timely '
                                                              'quarantine and communication are '
                                                              'operational pharmacovigilance '
                                                              'duties.'}],
                                     'extreme': [{'question': 'Intrathecal vincristine error '
                                                              'prevention?',
                                                  'options': ['A) Prepare vincristine in the same '
                                                              'syringe style as IT meds',
                                                              'B) Deliver IV vinca to the theatre '
                                                              'IT tray routinely',
                                                              'C) Never manage IV vinca like IT '
                                                              'medicines; use systemic safeguards',
                                                              'D) Allow ward nurses to '
                                                              'reconstitute vinca at bedside for '
                                                              'IT use'],
                                                  'answer': 'C) Never manage IV vinca like IT '
                                                            'medicines; use systemic safeguards',
                                                  'explanation': 'Intrathecal vincristine is '
                                                                 'almost uniformly fatal because '
                                                                 'vinca alkaloids cause severe '
                                                                 'neurotoxicity when injected into '
                                                                 'the CSF. Prevention relies on '
                                                                 'systemic safeguards: distinct '
                                                                 'packaging, never dispensing IV '
                                                                 'vinca in intrathecal sets, '
                                                                 'timing separation, and '
                                                                 'independent checks. Treating '
                                                                 'intrathecal and intravenous '
                                                                 'cytotoxics as interchangeable '
                                                                 'workflows is a recognized '
                                                                 'never-event pathway.'},
                                                 {'question': 'Disaster formulary planning '
                                                              'includes?',
                                                  'options': ['A) Stocking only luxury '
                                                              'nonessential cosmetics',
                                                              'B) Eliminating cold-chain '
                                                              'contingency plans',
                                                              'C) Relying solely on just-in-time '
                                                              'wholesale with no buffer',
                                                              'D) Critical medicines continuity '
                                                              'and cold-chain contingency'],
                                                  'answer': 'D) Critical medicines continuity and '
                                                            'cold-chain contingency',
                                                  'explanation': 'Disaster formulary planning '
                                                                 'identifies critical medicines '
                                                                 'whose interruption would '
                                                                 'immediately threaten life or '
                                                                 'continuity of essential therapy, '
                                                                 'including cold-chain–dependent '
                                                                 'products. Contingency stocks, '
                                                                 'alternative agents, and backup '
                                                                 'refrigeration or generator plans '
                                                                 'maintain supply during '
                                                                 'emergencies. Resilience planning '
                                                                 'links inventory science to '
                                                                 'public-health surge needs.'},
                                                 {'question': 'Cytotoxic spill response?',
                                                  'options': ['A) Evacuate/protect, use spill kit, '
                                                              'report, follow hazardous-drug '
                                                              'protocol',
                                                              'B) Wipe with bare hands and '
                                                              'continue compounding',
                                                              'C) Hose the area into general '
                                                              'drains without PPE',
                                                              'D) Ignore small spills if they dry '
                                                              'quickly'],
                                                  'answer': 'A) Evacuate/protect, use spill kit, '
                                                            'report, follow hazardous-drug '
                                                            'protocol',
                                                  'explanation': 'Cytotoxic spills aerosolize or '
                                                                 'deposit hazardous drug residues '
                                                                 'that can cause occupational '
                                                                 'exposure through skin contact or '
                                                                 'inhalation. Response protocols '
                                                                 'evacuate unprotected staff, '
                                                                 'contain the spill with a '
                                                                 'dedicated kit, use appropriate '
                                                                 'PPE, and report the incident. '
                                                                 'Hazardous-drug policies define '
                                                                 'decontamination, waste disposal, '
                                                                 'and medical follow-up.'}]},
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
                                        'options': ['A) Benzodiazepine sedation only',
                                                    'B) Paracetamol hepatotoxicity primarily',
                                                    'C) Opioid toxicity with respiratory '
                                                    'depression',
                                                    'D) Organophosphate cholinergic crisis'],
                                        'answer': 'C) Opioid toxicity with respiratory depression',
                                        'explanation': 'Naloxone is a competitive antagonist at '
                                                       'μ-opioid receptors and rapidly reverses '
                                                       'opioid-induced respiratory depression and '
                                                       'sedation. Because many opioids outlast '
                                                       "naloxone's effect, repeated dosing or "
                                                       'infusion may be required. Supportive '
                                                       'airway and ventilation care remain '
                                                       'foundational while antagonism restores '
                                                       'respiratory drive.'},
                                       {'question': 'Activated charcoal useful when?',
                                        'options': ['A) Iron overdose as first-line binder always',
                                                    'B) Lithium ingestion where adsorption is '
                                                    'reliable',
                                                    'C) Corrosive alkali ingestion to neutralize '
                                                    'pH',
                                                    'D) Selected recent ingestions if the airway '
                                                    'is protected'],
                                        'answer': 'D) Selected recent ingestions if the airway is '
                                                  'protected',
                                        'explanation': 'Activated charcoal adsorbs many toxins in '
                                                       'the gut, reducing systemic absorption if '
                                                       'given soon after ingestion when the airway '
                                                       'is protected. It is ineffective for '
                                                       'alcohols, metals, and corrosives and is '
                                                       'contraindicated when aspiration risk is '
                                                       'high or bowel integrity is compromised. '
                                                       'Benefit depends on timing, charcoal–toxin '
                                                       'binding, and clinical stability.'},
                                       {'question': 'ABC approach in poisoning means?',
                                        'options': ['A) Airway, Breathing, Circulation prioritized '
                                                    'first',
                                                    'B) Antidote before any supportive care always',
                                                    'C) Arterial blood gas as the only assessment',
                                                    'D) Activated charcoal for every unconscious '
                                                    'patient'],
                                        'answer': 'A) Airway, Breathing, Circulation prioritized '
                                                  'first',
                                        'explanation': 'In acute poisoning, the ABC approach '
                                                       'prioritizes airway patency, adequate '
                                                       'breathing/ventilation, and circulatory '
                                                       'support before toxin-specific antidotes. '
                                                       'Hypoxia, hypoventilation, and shock cause '
                                                       'immediate death independent of the '
                                                       'intoxicant. Stabilization creates the '
                                                       'physiologic window in which '
                                                       'decontamination and antidotes can work.'}],
                              'medium': [{'question': 'Paracetamol toxicity antidote?',
                                          'options': ['A) Flumazenil as routine first-line therapy',
                                                      'B) N-acetylcysteine to replenish '
                                                      'glutathione defenses',
                                                      'C) Naloxone infusion for hepatocyte '
                                                      'protection',
                                                      'D) Deferoxamine chelation of NAPQI'],
                                          'answer': 'B) N-acetylcysteine to replenish glutathione '
                                                    'defenses',
                                          'explanation': 'In paracetamol overdose, a fraction of '
                                                         'the drug is oxidized by CYP2E1 to NAPQI, '
                                                         'which depletes hepatic glutathione and '
                                                         'binds hepatocyte proteins. '
                                                         'N-acetylcysteine replenishes glutathione '
                                                         'and improves NAPQI detoxification, '
                                                         'preventing or limiting centrilobular '
                                                         'necrosis. Efficacy is greatest when '
                                                         'started early after significant overdose '
                                                         'according to nomogram-guided risk '
                                                         'assessment.'},
                                         {'question': 'Methanol toxicity visual threat treated '
                                                      'with?',
                                          'options': ['A) Physostigmine to increase acetylcholine',
                                                      'B) Naloxone to reverse optic nerve effects',
                                                      'C) Fomepizole or ethanol, with dialysis '
                                                      'when indicated',
                                                      'D) Atropine as the primary antidote always'],
                                          'answer': 'C) Fomepizole or ethanol, with dialysis when '
                                                    'indicated',
                                          'explanation': 'Methanol is metabolized by alcohol '
                                                         'dehydrogenase to formaldehyde and then '
                                                         'to formic acid, which causes metabolic '
                                                         'acidosis and optic nerve injury. '
                                                         'Fomepizole or ethanol competitively '
                                                         'inhibit alcohol dehydrogenase, blocking '
                                                         'formation of toxic metabolites. '
                                                         'Hemodialysis removes methanol and '
                                                         'formate when acidosis or high levels '
                                                         'indicate extracorporeal elimination.'},
                                         {'question': 'Tricyclic antidepressant overdose ECG clue?',
                                          'options': ['A) Shortened PR interval as the hallmark',
                                                      'B) Peaked T waves from hyperkalemia only',
                                                      'C) Isolated sinus bradycardia without QRS '
                                                      'change',
                                                      'D) Wide QRS reflecting sodium-channel '
                                                      'blockade'],
                                          'answer': 'D) Wide QRS reflecting sodium-channel '
                                                    'blockade',
                                          'explanation': 'Tricyclic antidepressants block cardiac '
                                                         'fast sodium channels, slowing phase-0 '
                                                         'depolarization and widening the QRS '
                                                         'complex on ECG. Sodium channel blockade '
                                                         'promotes ventricular arrhythmias and '
                                                         'seizures in severe overdose. Intravenous '
                                                         'sodium bicarbonate provides sodium '
                                                         'loading and alkalinization that '
                                                         'partially overcome channel block and '
                                                         'stabilize the membrane.'}],
                              'hard': [{'question': 'Physostigmine sometimes considered in?',
                                        'options': ['A) Severe anticholinergic delirium in '
                                                    'selected cases',
                                                    'B) TCA overdose with wide-complex arrhythmias '
                                                    'as first-line',
                                                    'C) Organophosphate poisoning instead of '
                                                    'atropine',
                                                    'D) Opioid coma when naloxone is unavailable'],
                                        'answer': 'A) Severe anticholinergic delirium in selected '
                                                  'cases',
                                        'explanation': 'Physostigmine is a reversible '
                                                       'acetylcholinesterase inhibitor that '
                                                       'increases synaptic acetylcholine and can '
                                                       'temporarily reverse central '
                                                       'anticholinergic delirium from agents such '
                                                       'as atropine or certain antihistamines. It '
                                                       'crosses the blood–brain barrier unlike '
                                                       'neostigmine. Use is reserved for selected '
                                                       'severe cases because bradycardia, '
                                                       'seizures, and cholinergic excess are '
                                                       'risks, especially with tricyclic '
                                                       'co-ingestion.'},
                                       {'question': 'Hydrofluoric acid burn systemic risk?',
                                        'options': ['A) Hypernatremia from fluoride absorption',
                                                    'B) Hypocalcemia from fluoride binding cations',
                                                    'C) Isolated hyperkalemia without calcium '
                                                    'shifts',
                                                    'D) Methemoglobinemia as the dominant effect'],
                                        'answer': 'B) Hypocalcemia from fluoride binding cations',
                                        'explanation': 'Hydrofluoric acid penetrates tissue and '
                                                       'avidly binds cations, depleting ionized '
                                                       'calcium and magnesium and disrupting '
                                                       'cellular metabolism. Systemic hypocalcemia '
                                                       'can trigger tetany, QT prolongation, and '
                                                       'life-threatening arrhythmias after '
                                                       'significant burns or inhalational '
                                                       'exposure. Local and systemic calcium '
                                                       'therapy is used to chelate fluoride and '
                                                       'restore calcium homeostasis.'},
                                       {'question': 'Body packer rupture risk management?',
                                        'options': ['A) Routine endoscopy to retrieve all packets '
                                                    'immediately',
                                                    'B) Discharge home after one dose of charcoal',
                                                    'C) Urgent surgical/toxicology pathways; avoid '
                                                    'unsafe endoscopy themes',
                                                    'D) Induce vomiting repeatedly until packets '
                                                    'appear'],
                                        'answer': 'C) Urgent surgical/toxicology pathways; avoid '
                                                  'unsafe endoscopy themes',
                                        'explanation': 'Body packers conceal drug-filled packets '
                                                       'in the gastrointestinal tract; packet '
                                                       'rupture can release massive opioid or '
                                                       'cocaine doses with catastrophic toxicity. '
                                                       'Management centers on urgent toxicology '
                                                       'and surgical pathways when obstruction, '
                                                       'rupture, or severe poisoning occurs. Blind '
                                                       'endoscopic retrieval is generally avoided '
                                                       'because of rupture risk to remaining '
                                                       'packets.'}],
                              'extreme': [{'question': 'Cyanide antidote kits may include?',
                                           'options': ['A) N-acetylcysteine as the primary cyanide '
                                                       'binder',
                                                       'B) Deferoxamine to chelate cyanide ions',
                                                       'C) Naloxone to reverse histotoxic hypoxia',
                                                       'D) Hydroxocobalamin and other protocol '
                                                       'options'],
                                           'answer': 'D) Hydroxocobalamin and other protocol '
                                                     'options',
                                           'explanation': 'Cyanide inhibits mitochondrial '
                                                          'cytochrome c oxidase (complex IV), '
                                                          'halting oxidative phosphorylation and '
                                                          'causing histotoxic hypoxia. '
                                                          'Hydroxocobalamin binds cyanide to form '
                                                          'cyanocobalamin, which is renally '
                                                          'excreted, rapidly restoring aerobic '
                                                          'metabolism in many protocols. Smoke '
                                                          'inhalation victims may have concurrent '
                                                          'cyanide and carbon monoxide poisoning '
                                                          'requiring combined management.'},
                                          {'question': 'Serotonin syndrome vs NMS distinction '
                                                       'matters because?',
                                           'options': ['A) Different triggers and management '
                                                       'nuances',
                                                       'B) Both are treated identically with '
                                                       'bromocriptine only',
                                                       'C) Neither ever involves hyperthermia or '
                                                       'rigidity',
                                                       'D) ECG QRS widening defines both syndromes '
                                                       'equally'],
                                           'answer': 'A) Different triggers and management nuances',
                                           'explanation': 'Serotonin syndrome is typically '
                                                          'precipitated by serotonergic drug '
                                                          'combinations and features clonus, '
                                                          'hyperreflexia, and rapid onset '
                                                          'hyperthermia, whereas neuroleptic '
                                                          'malignant syndrome follows dopamine '
                                                          'antagonists with severe rigidity and '
                                                          'slower onset. Distinguishing them '
                                                          'matters because management differs: '
                                                          'cyproheptadine and withdrawal of '
                                                          'serotonergics versus dopaminergic '
                                                          'support and antipsychotic cessation. '
                                                          'Misclassification can delay '
                                                          'toxin-specific therapy.'},
                                          {'question': 'Extracorporeal removal considered for?',
                                           'options': ['A) All highly protein-bound drugs '
                                                       'regardless of toxicity',
                                                       'B) Selected dialyzable toxins with severe '
                                                       'toxicity',
                                                       'C) Only topical exposures without systemic '
                                                       'absorption',
                                                       'D) Every OTC analgesic overdose without '
                                                       'exception'],
                                           'answer': 'B) Selected dialyzable toxins with severe '
                                                     'toxicity',
                                           'explanation': 'Extracorporeal removal (hemodialysis or '
                                                          'related techniques) is considered when '
                                                          'a toxin has suitable physicochemical '
                                                          'properties—low molecular weight, low '
                                                          'protein binding, small volume of '
                                                          'distribution—and severe clinical '
                                                          'toxicity or failing endogenous '
                                                          'clearance. Examples include severe '
                                                          'lithium, salicylate, and toxic-alcohol '
                                                          'poisoning. Guidance groups such as '
                                                          'EXTRIP summarize evidence for when '
                                                          'extracorporeal treatment adds '
                                                          'benefit.'}]},
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
                                                'options': ['A) Reducing visible dirt on work '
                                                            'surfaces only',
                                                            'B) Killing vegetative bacteria but '
                                                            'never spores',
                                                            'C) Disinfecting skin before '
                                                            'venipuncture only',
                                                            'D) Validated killing/removal of '
                                                            'viable microorganisms including '
                                                            'spores'],
                                                'answer': 'D) Validated killing/removal of viable '
                                                          'microorganisms including spores',
                                                'explanation': 'Sterilization is a validated '
                                                               'process that destroys or removes '
                                                               'all viable microorganisms, '
                                                               'including bacterial spores, to a '
                                                               'specified sterility assurance '
                                                               'level. Methods include moist heat, '
                                                               'dry heat, filtration, ethylene '
                                                               'oxide, and radiation, chosen for '
                                                               'product compatibility. Injectable '
                                                               'medicines depend on sterilization '
                                                               'or aseptic processing to prevent '
                                                               'contamination.'},
                                               {'question': 'Gram-positive bacteria stain?',
                                                'options': ['A) Purple/blue after Gram staining',
                                                            'B) Pink/red because of thin '
                                                            'peptidoglycan',
                                                            'C) Green due to endospore stain '
                                                            'carryover',
                                                            'D) Colorless because they lack cell '
                                                            'walls'],
                                                'answer': 'A) Purple/blue after Gram staining',
                                                'explanation': 'Gram-positive bacteria retain '
                                                               'crystal violet–iodine complex '
                                                               'within a thick peptidoglycan cell '
                                                               'wall and appear purple/blue after '
                                                               'Gram staining. Gram-negative '
                                                               'organisms have a thin '
                                                               'peptidoglycan layer and outer '
                                                               'membrane that allow decolorization '
                                                               'and take up safranin counterstain '
                                                               '(pink/red). The stain thus '
                                                               'reflects fundamental cell-envelope '
                                                               'structure.'},
                                               {'question': 'Disinfection differs from '
                                                            'sterilization by?',
                                                'options': ['A) Always destroying bacterial spores '
                                                            'reliably',
                                                            'B) Reducing microbes on '
                                                            'surfaces/objects without necessarily '
                                                            'sterilizing',
                                                            'C) Guaranteeing SAL of 10^-6 for '
                                                            'every surface wipe',
                                                            'D) Applying only to injectable drug '
                                                            'products'],
                                                'answer': 'B) Reducing microbes on '
                                                          'surfaces/objects without necessarily '
                                                          'sterilizing',
                                                'explanation': 'Disinfection reduces pathogenic '
                                                               'microorganisms on inanimate '
                                                               'surfaces or objects to a level '
                                                               'judged safe for use, but it does '
                                                               'not reliably eliminate all spores '
                                                               'or achieve sterilization. Agent '
                                                               'selection depends on spectrum, '
                                                               'concentration, contact time, and '
                                                               'material compatibility. '
                                                               'Sterilization is required when '
                                                               'absolute absence of viable '
                                                               'microbes is needed, as for '
                                                               'critical injectables.'}],
                                      'medium': [{'question': 'Endotoxin (LPS) risk is mainly '
                                                              'from?',
                                                  'options': ['A) Gram-positive spore-forming rods '
                                                              'only',
                                                              'B) Fungi that produce aflatoxins in '
                                                              'grains',
                                                              'C) Gram-negative bacteria '
                                                              'outer-membrane LPS',
                                                              'D) Viruses lacking any lipid '
                                                              'envelope'],
                                                  'answer': 'C) Gram-negative bacteria '
                                                            'outer-membrane LPS',
                                                  'explanation': 'Bacterial endotoxin is '
                                                                 'lipopolysaccharide (LPS) from '
                                                                 'the outer membrane of '
                                                                 'Gram-negative bacteria and is a '
                                                                 'potent pyrogen. Even sterile '
                                                                 'solutions can cause fever and '
                                                                 'septic-like reactions if LPS '
                                                                 'remains. Pharmaceutical water '
                                                                 'and parenteral products are '
                                                                 'therefore controlled with '
                                                                 'bacterial endotoxin tests such '
                                                                 'as LAL/recombinant factor C '
                                                                 'assays.'},
                                                 {'question': 'Autoclaving typical condition '
                                                              'theme?',
                                                  'options': ['A) Dry heat at 60°C for five '
                                                              'minutes',
                                                              'B) UV light exposure of sealed '
                                                              'vials only',
                                                              'C) Membrane filtration as the '
                                                              'autoclave method',
                                                              'D) Moist heat under pressure (e.g., '
                                                              '121°C hold)'],
                                                  'answer': 'D) Moist heat under pressure (e.g., '
                                                            '121°C hold)',
                                                  'explanation': 'Autoclaving uses saturated steam '
                                                                 'under pressure to achieve '
                                                                 'moist-heat sterilization, '
                                                                 'classically exemplified by 121 '
                                                                 '°C for a validated hold time '
                                                                 '(often about 15 minutes for many '
                                                                 'loads). Steam kills '
                                                                 'microorganisms by coagulating '
                                                                 'proteins and is highly effective '
                                                                 'against spores when air removal '
                                                                 'and heat penetration are '
                                                                 'assured. Cycle parameters must '
                                                                 'be validated for load '
                                                                 'configuration.'},
                                                 {'question': 'Preservatives in multi-dose vials '
                                                              'help?',
                                                  'options': ['A) Inhibit microbial growth after '
                                                              'repeated entries',
                                                              'B) Replace the need for aseptic '
                                                              'manufacturing',
                                                              'C) Sterilize the vial contents '
                                                              'after contamination',
                                                              'D) Neutralize bacterial endotoxin '
                                                              'in solution'],
                                                  'answer': 'A) Inhibit microbial growth after '
                                                            'repeated entries',
                                                  'explanation': 'Antimicrobial preservatives in '
                                                                 'multi-dose vials suppress growth '
                                                                 'of microbes introduced during '
                                                                 'repeated needle entries after '
                                                                 'first opening. They do not '
                                                                 'sterilize a grossly contaminated '
                                                                 'product and are not a substitute '
                                                                 'for aseptic handling. '
                                                                 'Preservative efficacy testing '
                                                                 'supports their inclusion within '
                                                                 'labeled beyond-use '
                                                                 'constraints.'}],
                                      'hard': [{'question': 'HEPA filters in cleanrooms remove?',
                                                'options': ['A) Only dissolved endotoxin from WFI '
                                                            'loops',
                                                            'B) Airborne particles/microbes to '
                                                            'specified efficiency',
                                                            'C) Only volatile organic solvent '
                                                            'vapors',
                                                            'D) Only chlorine residual from tap '
                                                            'water'],
                                                'answer': 'B) Airborne particles/microbes to '
                                                          'specified efficiency',
                                                'explanation': 'High-efficiency particulate air '
                                                               '(HEPA) filters remove airborne '
                                                               'particles by interception, '
                                                               'impaction, and diffusion with '
                                                               'defined efficiency (typically '
                                                               '≥99.97% for 0.3 μm challenge '
                                                               'particles). In cleanrooms they '
                                                               'supply particle-controlled air '
                                                               'that reduces microbial and '
                                                               'particulate contamination risk '
                                                               'during aseptic work. Filter '
                                                               'integrity and airflow patterns are '
                                                               'critical environmental controls.'},
                                               {'question': 'Biological indicator for autoclave '
                                                            'often uses?',
                                                'options': ['A) Escherichia coli vegetative cells '
                                                            'only',
                                                            'B) Candida albicans yeast suspensions',
                                                            'C) Geobacillus stearothermophilus '
                                                            'spores',
                                                            'D) Influenza virus cultured in eggs'],
                                                'answer': 'C) Geobacillus stearothermophilus '
                                                          'spores',
                                                'explanation': 'Biological indicators for steam '
                                                               'sterilization commonly use spores '
                                                               'of Geobacillus stearothermophilus, '
                                                               'which are highly heat resistant. '
                                                               'Survival or kill of the spore '
                                                               'challenge after a cycle provides a '
                                                               'direct measure of lethality beyond '
                                                               'physical parametric readouts '
                                                               'alone. BI results support '
                                                               'validation and routine monitoring '
                                                               'of autoclave performance.'},
                                               {'question': 'Biofilm on equipment causes?',
                                                'options': ['A) Improved sterilant penetration '
                                                            'every cycle',
                                                            'B) Guaranteed sterility without '
                                                            'cleaning',
                                                            'C) Faster drying of stainless '
                                                            'surfaces only',
                                                            'D) Persistent contamination that is '
                                                            'hard to eradicate'],
                                                'answer': 'D) Persistent contamination that is '
                                                          'hard to eradicate',
                                                'explanation': 'Biofilms are surface-associated '
                                                               'microbial communities embedded in '
                                                               'extracellular polymeric substance '
                                                               'that impede biocide penetration '
                                                               'and slow metabolism. Once '
                                                               'established on pharmaceutical '
                                                               'equipment, they shed planktonic '
                                                               'cells and cause persistent '
                                                               'contamination hard to eradicate by '
                                                               'ordinary rinsing. Cleaning '
                                                               'validation and hygienic design aim '
                                                               'to prevent biofilm niches.'}],
                                      'extreme': [{'question': 'Aseptic process simulation (media '
                                                               'fill) demonstrates?',
                                                   'options': ['A) Operator/process capability to '
                                                               'maintain sterility',
                                                               'B) Potency assay of the finished '
                                                               'active ingredient',
                                                               'C) Endotoxin destruction by dry '
                                                               'heat tunnels only',
                                                               'D) Tablet content uniformity '
                                                               'across a batch'],
                                                   'answer': 'A) Operator/process capability to '
                                                             'maintain sterility',
                                                   'explanation': 'Aseptic process simulation '
                                                                  '(media fill) replaces product '
                                                                  'with sterile growth medium '
                                                                  'processed through the full '
                                                                  'aseptic manufacturing train by '
                                                                  'operators under routine '
                                                                  'conditions. Subsequent '
                                                                  'incubation tests whether '
                                                                  'contamination was introduced, '
                                                                  'thereby demonstrating process '
                                                                  'and operator capability to '
                                                                  'maintain sterility. Media fills '
                                                                  'are a GMP expectation for '
                                                                  'validating aseptic operations.'},
                                                  {'question': 'Mycoplasma contamination is '
                                                               'problematic in?',
                                                   'options': ['A) Terminal steam sterilization of '
                                                               'glass vials only',
                                                               'B) Cell culture and biologic '
                                                               'production systems',
                                                               'C) Dry-powder inhaler capsule '
                                                               'filling only',
                                                               'D) Sugar-coating pans for oral '
                                                               'tablets only'],
                                                   'answer': 'B) Cell culture and biologic '
                                                             'production systems',
                                                   'explanation': 'Mycoplasmas are '
                                                                  'cell-wall–deficient bacteria '
                                                                  'that pass many sterilizing '
                                                                  'filters and do not produce '
                                                                  'turbidity typical of ordinary '
                                                                  'bacterial contamination. In '
                                                                  'cell-culture and biologic '
                                                                  'manufacturing systems they '
                                                                  'alter metabolism, reduce yield, '
                                                                  'and can contaminate products. '
                                                                  'Dedicated nucleic-acid or '
                                                                  'culture-based mycoplasma tests '
                                                                  'are required because standard '
                                                                  'microscopy often misses them.'},
                                                  {'question': 'Parametric release concepts rely '
                                                               'on?',
                                                   'options': ['A) Skipping all process validation '
                                                               'indefinitely',
                                                               'B) Visual inspection as the sole '
                                                               'release criterion',
                                                               'C) Validated process data in lieu '
                                                               'of finished testing in defined '
                                                               'cases',
                                                               'D) Customer complaints as the '
                                                               'primary batch-release signal'],
                                                   'answer': 'C) Validated process data in lieu of '
                                                             'finished testing in defined cases',
                                                   'explanation': 'Parametric release authorizes '
                                                                  'batch release based on '
                                                                  'demonstrated control of '
                                                                  'validated critical process '
                                                                  'parameters instead of awaiting '
                                                                  'finished-product sterility test '
                                                                  'results in defined regulatory '
                                                                  'frameworks. It requires robust '
                                                                  'process understanding, '
                                                                  'monitoring, and '
                                                                  'documentation—commonly applied '
                                                                  'to terminally sterilized '
                                                                  'products. Without that '
                                                                  'validated evidence package, '
                                                                  'traditional end-product testing '
                                                                  'remains required.'}]},
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
        "🩺 *CharaNas Pharmacy*\n"
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
