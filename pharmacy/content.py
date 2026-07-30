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
                                                      'B) Occupies a receptor without '
                                                      'activating it',
                                                      'C) Irreversibly destroys the receptor '
                                                      'protein',
                                                      'D) Only inhibits an enzyme at all '
                                                      'doses'],
                                          'answer': 'A) Activates a receptor and increases '
                                                    'signaling',
                                          'explanation': 'An agonist binds a receptor and '
                                                         'stabilizes an active conformation, '
                                                         'thereby increasing receptor '
                                                         'signaling relative to basal tone. '
                                                         'Full agonists can elicit the '
                                                         "system's maximal response, whereas "
                                                         'partial agonists produce a '
                                                         'submaximal effect even at full '
                                                         'occupancy. Antagonists occupy the '
                                                         'same or related sites without '
                                                         'activating the receptor and '
                                                         'therefore reduce agonist effect.',
                                          'choice_explanations': {'A': 'An agonist binds its '
                                                                       'receptor and '
                                                                       'stabilizes the active '
                                                                       'conformation, '
                                                                       'increasing downstream '
                                                                       'signaling above basal '
                                                                       'tone; full agonists '
                                                                       'can reach system Emax.',
                                                                  'B': 'Occupying a receptor '
                                                                       'without activating it '
                                                                       'describes a '
                                                                       'competitive antagonist '
                                                                       '(or inverse agonist '
                                                                       'context), which '
                                                                       'reduces agonist effect '
                                                                       'rather than increasing '
                                                                       'signaling.',
                                                                  'C': 'Irreversible receptor '
                                                                       'destruction is not '
                                                                       'agonist pharmacology; '
                                                                       'agonists modulate '
                                                                       'conformation and '
                                                                       'signaling, they do not '
                                                                       'proteolytically '
                                                                       'destroy the receptor '
                                                                       'protein.',
                                                                  'D': 'Enzyme inhibition at '
                                                                       'all doses describes an '
                                                                       'enzyme inhibitor, not '
                                                                       'receptor agonism; '
                                                                       'agonists act primarily '
                                                                       'via receptor '
                                                                       'activation, not '
                                                                       'blanket enzyme '
                                                                       'blockade.'}},
                                         {'question': 'First-pass metabolism mainly occurs '
                                                      'after?',
                                          'options': ['A) Intravenous bolus administration',
                                                      'B) Oral absorption with hepatic portal '
                                                      'passage',
                                                      'C) Intramuscular injection into deltoid '
                                                      'muscle',
                                                      'D) Topical application to intact skin'],
                                          'answer': 'B) Oral absorption with hepatic portal '
                                                    'passage',
                                          'explanation': 'After oral absorption, drug in the '
                                                         'portal circulation passes through '
                                                         'the liver before reaching the '
                                                         'systemic arterial blood. Extensive '
                                                         'hepatic extraction or gut-wall '
                                                         'metabolism during this first pass '
                                                         'can substantially reduce '
                                                         'bioavailability. Intravenous '
                                                         'administration bypasses first-pass '
                                                         'metabolism, which is why oral and IV '
                                                         'doses often differ for '
                                                         'high-extraction drugs.',
                                          'choice_explanations': {'A': 'IV bolus places drug '
                                                                       'directly into systemic '
                                                                       'venous blood, '
                                                                       'bypassing the hepatic '
                                                                       'portal vein, so it '
                                                                       'avoids classic '
                                                                       'first-pass hepatic '
                                                                       'extraction after gut '
                                                                       'absorption.',
                                                                  'B': 'After oral absorption, '
                                                                       'drug enters the portal '
                                                                       'vein and passes '
                                                                       'through the liver '
                                                                       'before systemic '
                                                                       'arterial distribution; '
                                                                       'gut-wall and hepatic '
                                                                       'metabolism during this '
                                                                       'first pass can '
                                                                       'markedly cut '
                                                                       'bioavailability.',
                                                                  'C': 'Intramuscular '
                                                                       'injection delivers '
                                                                       'drug into muscle '
                                                                       'vasculature that '
                                                                       'drains to the systemic '
                                                                       'circulation without '
                                                                       'obligatory portal '
                                                                       'transit, so first-pass '
                                                                       'hepatic extraction is '
                                                                       'minimal compared with '
                                                                       'oral dosing.',
                                                                  'D': 'Topical application to '
                                                                       'intact skin relies on '
                                                                       'dermal absorption into '
                                                                       'local or systemic '
                                                                       'capillaries; '
                                                                       'intact-skin products '
                                                                       'are not primarily '
                                                                       'subject to hepatic '
                                                                       'portal first-pass '
                                                                       'after oral '
                                                                       'absorption.'}},
                                         {'question': 'Therapeutic index relates to?',
                                          'options': ['A) Tablet dissolution rate in gastric '
                                                      'fluid',
                                                      'B) Plasma protein-binding percentage '
                                                      'alone',
                                                      'C) Safety margin between effective and '
                                                      'toxic doses',
                                                      'D) Time to reach peak plasma '
                                                      'concentration'],
                                          'answer': 'C) Safety margin between effective and '
                                                    'toxic doses',
                                          'explanation': 'The therapeutic index compares a '
                                                         'toxic dose measure (for example '
                                                         'TD50) with an effective dose measure '
                                                         '(for example ED50), reflecting the '
                                                         'margin between efficacy and harm. '
                                                         'Drugs with a narrow therapeutic '
                                                         'index have overlapping effective and '
                                                         'toxic concentration ranges. Such '
                                                         'agents typically require careful '
                                                         'dose titration and, when '
                                                         'appropriate, therapeutic drug '
                                                         'monitoring.',
                                          'choice_explanations': {'A': 'Tablet dissolution '
                                                                       'rate is a '
                                                                       'pharmaceutic/biopharmaceutic '
                                                                       'property controlling '
                                                                       'absorption onset, not '
                                                                       'the toxic-to-effective '
                                                                       'dose ratio that '
                                                                       'defines therapeutic '
                                                                       'index.',
                                                                  'B': 'Plasma protein-binding '
                                                                       'percentage influences '
                                                                       'free fraction and '
                                                                       'distribution but alone '
                                                                       'does not quantify the '
                                                                       'safety margin between '
                                                                       'effective and toxic '
                                                                       'doses.',
                                                                  'C': 'Therapeutic index '
                                                                       'compares a toxic dose '
                                                                       'metric (e.g., TD50) '
                                                                       'with an effective dose '
                                                                       'metric (e.g., ED50), '
                                                                       'expressing the margin '
                                                                       'between efficacy and '
                                                                       'harm for dose '
                                                                       'selection and '
                                                                       'monitoring.',
                                                                  'D': 'Time to peak plasma '
                                                                       'concentration (Tmax) '
                                                                       'reflects absorption '
                                                                       'and distribution '
                                                                       'kinetics, not the '
                                                                       'dose-based safety '
                                                                       'margin between '
                                                                       'efficacy and '
                                                                       'toxicity.'}}],
                                'medium': [{'question': 'Beta-blocker caution is highest in?',
                                            'options': ['A) Mild seasonal allergic rhinitis '
                                                        'only',
                                                        'B) Stable hypothyroidism on '
                                                        'levothyroxine',
                                                        'C) Osteoarthritis treated with NSAIDs',
                                                        'D) Asthma when using nonselective '
                                                        'agents'],
                                            'answer': 'D) Asthma when using nonselective '
                                                      'agents',
                                            'explanation': 'Nonselective β-blockers antagonize '
                                                           'β2-adrenergic receptors that '
                                                           'mediate bronchial smooth-muscle '
                                                           'relaxation. Loss of β2 tone can '
                                                           'precipitate bronchoconstriction in '
                                                           'patients with asthma or reactive '
                                                           'airway disease. Cardioselective '
                                                           'β1-blockers reduce but do not '
                                                           'abolish this risk at higher doses.',
                                            'choice_explanations': {'A': 'Mild seasonal '
                                                                         'allergic rhinitis is '
                                                                         'histamine/IgE-driven '
                                                                         'mucosal '
                                                                         'inflammation; '
                                                                         'nonselective '
                                                                         'β-blockade is not '
                                                                         'the primary '
                                                                         'high-risk '
                                                                         'contraindication '
                                                                         'scenario compared '
                                                                         'with reactive '
                                                                         'airways disease.',
                                                                    'B': 'Stable '
                                                                         'hypothyroidism on '
                                                                         'replacement thyroid '
                                                                         'hormone does not '
                                                                         'create the '
                                                                         'β2-bronchodilator '
                                                                         'antagonism risk that '
                                                                         'makes nonselective '
                                                                         'β-blockers hazardous '
                                                                         'in asthma.',
                                                                    'C': 'Osteoarthritis '
                                                                         'treated with NSAIDs '
                                                                         'involves COX-related '
                                                                         'analgesia/inflammation '
                                                                         'pathways, not '
                                                                         'β2-mediated '
                                                                         'bronchodilation that '
                                                                         'nonselective '
                                                                         'β-blockers '
                                                                         'antagonize.',
                                                                    'D': 'Nonselective '
                                                                         'β-blockers '
                                                                         'antagonize β2 '
                                                                         'receptors that relax '
                                                                         'bronchial smooth '
                                                                         'muscle; loss of β2 '
                                                                         'tone can precipitate '
                                                                         'bronchoconstriction '
                                                                         'in asthma, making '
                                                                         'this the highest '
                                                                         'caution setting.'}},
                                           {'question': 'ACE inhibitor common side effect?',
                                            'options': ['A) Dry cough from bradykinin '
                                                        'accumulation',
                                                        'B) Gingival hyperplasia as the class '
                                                        'hallmark',
                                                        'C) Orange urine discoloration in most '
                                                        'users',
                                                        'D) Ototoxicity at standard '
                                                        'antihypertensive doses'],
                                            'answer': 'A) Dry cough from bradykinin '
                                                      'accumulation',
                                            'explanation': 'ACE inhibitors block '
                                                           'angiotensin-converting enzyme, '
                                                           'which also degrades bradykinin in '
                                                           'the lungs and vasculature. '
                                                           'Accumulated bradykinin and related '
                                                           'peptides stimulate sensory nerves '
                                                           'and are the principal mechanism of '
                                                           'ACE-inhibitor–associated dry '
                                                           'cough. Angiotensin-receptor '
                                                           'blockers spare ACE and therefore '
                                                           'rarely cause this cough, making '
                                                           'them a common alternative.',
                                            'choice_explanations': {'A': 'ACE also degrades '
                                                                         'bradykinin; ACE '
                                                                         'inhibition raises '
                                                                         'local bradykinin '
                                                                         '(and related '
                                                                         'peptides) in '
                                                                         'lung/vasculature, '
                                                                         'stimulating sensory '
                                                                         'nerves and producing '
                                                                         'the characteristic '
                                                                         'dry cough.',
                                                                    'B': 'Gingival hyperplasia '
                                                                         'is classically '
                                                                         'linked to '
                                                                         'calcium-channel '
                                                                         'blockers (e.g., '
                                                                         'nifedipine), '
                                                                         'phenytoin, or '
                                                                         'ciclosporin—not an '
                                                                         'ACE-inhibitor class '
                                                                         'hallmark from '
                                                                         'bradykinin '
                                                                         'accumulation.',
                                                                    'C': 'Orange urine '
                                                                         'discoloration is not '
                                                                         'a typical '
                                                                         'ACE-inhibitor '
                                                                         'effect; it is seen '
                                                                         'with agents such as '
                                                                         'rifampicin or '
                                                                         'phenazopyridine, '
                                                                         'unrelated to '
                                                                         'ACE–bradykinin '
                                                                         'pharmacology.',
                                                                    'D': 'Ototoxicity at '
                                                                         'antihypertensive '
                                                                         'doses is '
                                                                         'characteristic of '
                                                                         'aminoglycosides or '
                                                                         'high-dose loop '
                                                                         'diuretics, not ACE '
                                                                         'inhibitors whose '
                                                                         'cough arises from '
                                                                         'bradykinin '
                                                                         'accumulation.'}},
                                           {'question': 'Zero-order elimination example theme?',
                                            'options': ['A) Most beta-lactam antibiotics at '
                                                        'usual doses',
                                                        'B) Phenytoin and ethanol at higher '
                                                        'levels',
                                                        'C) All water-soluble vitamins without '
                                                        'exception',
                                                        'D) Isotonic saline infused as '
                                                        'maintenance fluid'],
                                            'answer': 'B) Phenytoin and ethanol at higher '
                                                      'levels',
                                            'explanation': 'Zero-order (saturation) '
                                                           'elimination occurs when '
                                                           'metabolizing enzymes operate near '
                                                           'Vmax, so a constant amount of drug '
                                                           'is removed per unit time. '
                                                           'Phenytoin and ethanol classically '
                                                           'show this nonlinear behavior at '
                                                           'clinically relevant '
                                                           'concentrations. Small dose '
                                                           'increases can then produce '
                                                           'disproportionately large rises in '
                                                           'plasma concentration and toxicity '
                                                           'risk.',
                                            'choice_explanations': {'A': 'Most β-lactam '
                                                                         'antibiotics at usual '
                                                                         'doses exhibit '
                                                                         'approximately '
                                                                         'first-order (linear) '
                                                                         'elimination with '
                                                                         'concentration-proportional '
                                                                         'clearance, not '
                                                                         'capacity-limited '
                                                                         'zero-order kinetics.',
                                                                    'B': 'Phenytoin and '
                                                                         'ethanol undergo '
                                                                         'capacity-limited '
                                                                         'metabolism near Vmax '
                                                                         'at higher '
                                                                         'concentrations, so a '
                                                                         'roughly constant '
                                                                         'amount is eliminated '
                                                                         'per time '
                                                                         '(zero-order/Michaelis–Menten '
                                                                         'behavior).',
                                                                    'C': 'Water-soluble '
                                                                         'vitamins are not '
                                                                         'uniformly zero-order '
                                                                         'eliminated; many '
                                                                         'show linear renal '
                                                                         'handling at '
                                                                         'physiologic intakes, '
                                                                         'so they are not a '
                                                                         'defining zero-order '
                                                                         'theme.',
                                                                    'D': 'Isotonic saline as '
                                                                         'maintenance fluid is '
                                                                         'volume/electrolyte '
                                                                         'replacement without '
                                                                         'saturable '
                                                                         'drug-metabolizing '
                                                                         'enzyme kinetics; it '
                                                                         'is not an example of '
                                                                         'zero-order drug '
                                                                         'elimination.'}}],
                                'hard': [{'question': 'Competitive antagonist effect on '
                                                      'agonist curve?',
                                          'options': ['A) Depresses Emax with no change in '
                                                      'EC50',
                                                      'B) Left-shifts the curve and raises '
                                                      'Emax',
                                                      'C) Right shift with same maximal '
                                                      'response if surmountable',
                                                      'D) Converts the agonist into an '
                                                      'irreversible binder'],
                                          'answer': 'C) Right shift with same maximal response '
                                                    'if surmountable',
                                          'explanation': 'A surmountable competitive '
                                                         'antagonist and agonist compete for '
                                                         'the same receptor site, so higher '
                                                         'agonist concentrations restore '
                                                         'receptor occupancy. On a '
                                                         'concentration–response curve this '
                                                         'produces a parallel rightward shift '
                                                         'with preserved maximal response '
                                                         '(Emax). Noncompetitive or '
                                                         'irreversible antagonism more '
                                                         'typically depresses Emax when '
                                                         'receptor reserve is limited.',
                                          'choice_explanations': {'A': 'Depressing Emax '
                                                                       'without changing EC50 '
                                                                       'is the hallmark of '
                                                                       'noncompetitive/insurmountable '
                                                                       'antagonism or '
                                                                       'irreversible receptor '
                                                                       'loss, not surmountable '
                                                                       'competitive '
                                                                       'antagonism.',
                                                                  'B': 'Left-shifting the '
                                                                       'curve and raising Emax '
                                                                       'would increase '
                                                                       'apparent agonist '
                                                                       'potency/efficacy; '
                                                                       'competitive '
                                                                       'antagonists do the '
                                                                       'opposite by reducing '
                                                                       'agonist occupancy at a '
                                                                       'given concentration.',
                                                                  'C': 'A surmountable '
                                                                       'competitive antagonist '
                                                                       'competes for the '
                                                                       'orthosteric site, so '
                                                                       'higher agonist '
                                                                       'concentrations restore '
                                                                       'occupancy: the curve '
                                                                       'shifts right with '
                                                                       'unchanged Emax when '
                                                                       'reserve allows.',
                                                                  'D': 'Competitive '
                                                                       'antagonists do not '
                                                                       'chemically convert '
                                                                       'agonists into '
                                                                       'irreversible binders; '
                                                                       'they reversibly occupy '
                                                                       'the shared site and '
                                                                       'reduce agonist binding '
                                                                       'probability.'}},
                                         {'question': 'CYP3A4 induction may?',
                                          'options': ['A) Block first-pass metabolism '
                                                      'completely',
                                                      'B) Increase oral bioavailability of all '
                                                      'substrates',
                                                      'C) Prolong half-life of every CYP3A4 '
                                                      'substrate',
                                                      'D) Reduce plasma levels of sensitive '
                                                      'substrate drugs'],
                                          'answer': 'D) Reduce plasma levels of sensitive '
                                                    'substrate drugs',
                                          'explanation': 'CYP3A4 induction increases '
                                                         'transcription and amount of active '
                                                         'enzyme, accelerating oxidative '
                                                         'metabolism of many substrates. '
                                                         'Faster clearance lowers steady-state '
                                                         'plasma concentrations and can cause '
                                                         'loss of therapeutic effect for '
                                                         'inducer-sensitive drugs. The '
                                                         'interaction magnitude depends on '
                                                         'inducer potency, substrate fraction '
                                                         'metabolized by CYP3A4, and dosing '
                                                         'time course.',
                                          'choice_explanations': {'A': 'CYP3A4 induction '
                                                                       'increases enzyme '
                                                                       'amount and accelerates '
                                                                       'substrate metabolism; '
                                                                       'it does not block '
                                                                       'first-pass '
                                                                       'metabolism—it '
                                                                       'typically intensifies '
                                                                       'first-pass extraction '
                                                                       'of oral CYP3A4 '
                                                                       'substrates.',
                                                                  'B': 'Induction lowers, '
                                                                       'rather than increases, '
                                                                       'oral bioavailability '
                                                                       'of many CYP3A4 '
                                                                       'substrates by '
                                                                       'enhancing gut/hepatic '
                                                                       'first-pass clearance, '
                                                                       'so plasma exposure '
                                                                       'falls.',
                                                                  'C': 'Faster CYP3A4-mediated '
                                                                       'clearance shortens, '
                                                                       'not prolongs, '
                                                                       'half-life of sensitive '
                                                                       'substrates when '
                                                                       'clearance rises '
                                                                       'relative to volume of '
                                                                       'distribution.',
                                                                  'D': 'By increasing '
                                                                       'oxidative clearance of '
                                                                       'CYP3A4 substrates, '
                                                                       'induction reduces '
                                                                       'steady-state plasma '
                                                                       'concentrations and AUC '
                                                                       'of sensitive drugs, '
                                                                       'potentially causing '
                                                                       'therapeutic failure.'}},
                                         {'question': 'Loading dose mainly depends on?',
                                          'options': ['A) Volume of distribution and target '
                                                      'concentration',
                                                      'B) Clearance alone without considering '
                                                      'Vd',
                                                      'C) Elimination half-life as the sole '
                                                      'determinant',
                                                      'D) Dosing interval chosen for '
                                                      'maintenance therapy'],
                                          'answer': 'A) Volume of distribution and target '
                                                    'concentration',
                                          'explanation': 'Loading dose is chosen to rapidly '
                                                         'achieve a target concentration in '
                                                         'the apparent volume of distribution: '
                                                         'LD ≈ Css × Vd (adjusted for '
                                                         'bioavailability). It fills the '
                                                         'distributive space rather than '
                                                         'matching elimination rate. '
                                                         'Maintenance dose, by contrast, '
                                                         'replaces drug lost through clearance '
                                                         'and is therefore governed mainly by '
                                                         'CL and dosing interval.',
                                          'choice_explanations': {'A': 'Loading dose is sized '
                                                                       'to fill the apparent '
                                                                       'volume of distribution '
                                                                       'to a target '
                                                                       'concentration: LD ≈ '
                                                                       'Css × Vd (adjusted for '
                                                                       'bioavailability), '
                                                                       'independent of '
                                                                       'clearance for the '
                                                                       'initial fill.',
                                                                  'B': 'Clearance determines '
                                                                       'the maintenance dose '
                                                                       'rate needed to replace '
                                                                       'eliminated drug at '
                                                                       'steady state; it is '
                                                                       'not the primary '
                                                                       'determinant of the '
                                                                       'one-time loading fill '
                                                                       'of Vd.',
                                                                  'C': 'Elimination half-life '
                                                                       'governs time to steady '
                                                                       'state and dosing '
                                                                       'interval choices, but '
                                                                       'loading dose magnitude '
                                                                       'is set by Vd and '
                                                                       'target concentration, '
                                                                       'not t½ alone.',
                                                                  'D': 'Dosing interval shapes '
                                                                       'fluctuation and '
                                                                       'average Css for '
                                                                       'maintenance regimens; '
                                                                       'the loading dose '
                                                                       'itself targets rapid '
                                                                       'achievement of '
                                                                       'concentration in '
                                                                       'Vd.'}}],
                                'extreme': [{'question': 'Torsades risk rises with?',
                                             'options': ['A) Therapeutic-dose paracetamol used '
                                                         'alone',
                                                         'B) QT-prolonging drugs plus '
                                                         'electrolyte imbalance',
                                                         'C) Topical emollients applied to dry '
                                                         'skin',
                                                         'D) Routine vitamin C and D '
                                                         'supplementation'],
                                             'answer': 'B) QT-prolonging drugs plus '
                                                       'electrolyte imbalance',
                                             'explanation': 'Torsades de pointes is a '
                                                            'polymorphic ventricular '
                                                            'tachycardia linked to delayed '
                                                            'ventricular repolarization and QT '
                                                            'interval prolongation. Many drugs '
                                                            'block cardiac IKr (hERG) '
                                                            'potassium channels, and '
                                                            'hypokalemia or hypomagnesemia '
                                                            'further destabilize '
                                                            'repolarization. Concurrent '
                                                            'QT-prolonging drugs plus '
                                                            'electrolyte imbalance therefore '
                                                            'synergistically elevate torsades '
                                                            'risk.',
                                             'choice_explanations': {'A': 'Therapeutic-dose '
                                                                          'paracetamol alone '
                                                                          'does not '
                                                                          'meaningfully '
                                                                          'prolong ventricular '
                                                                          'repolarization or '
                                                                          'precipitate '
                                                                          'torsades via IKr '
                                                                          'blockade at usual '
                                                                          'exposures.',
                                                                     'B': 'Torsades de pointes '
                                                                          'arises when delayed '
                                                                          'ventricular '
                                                                          'repolarization (QT '
                                                                          'prolongation)—often '
                                                                          'from IKr-blocking '
                                                                          'drugs—combines with '
                                                                          'risk amplifiers '
                                                                          'such as '
                                                                          'hypokalemia/hypomagnesemia '
                                                                          'that further slow '
                                                                          'repolarization.',
                                                                     'C': 'Topical emollients '
                                                                          'act locally on skin '
                                                                          'barrier lipids and '
                                                                          'do not systemically '
                                                                          'block cardiac '
                                                                          'potassium channels '
                                                                          'or prolong the QT '
                                                                          'interval.',
                                                                     'D': 'Routine vitamin C/D '
                                                                          'supplementation '
                                                                          'does not cause IKr '
                                                                          'blockade or '
                                                                          'electrolyte '
                                                                          'patterns that '
                                                                          'typically trigger '
                                                                          'drug-associated '
                                                                          'torsades.'}},
                                            {'question': 'Serotonin syndrome risk combination '
                                                         'theme?',
                                             'options': ['A) Two low-potency topical '
                                                         'corticosteroids together',
                                                         'B) Antacid plus alginate taken after '
                                                         'meals',
                                                         'C) MAOI combined with SSRI or other '
                                                         'strong serotonergics',
                                                         'D) Fluoride toothpaste used with '
                                                         'calcium supplements'],
                                             'answer': 'C) MAOI combined with SSRI or other '
                                                       'strong serotonergics',
                                             'explanation': 'Serotonin syndrome reflects '
                                                            'excess serotonergic tone at '
                                                            'central 5-HT receptors, '
                                                            'especially 5-HT2A. Combining '
                                                            'monoamine oxidase inhibitors with '
                                                            'SSRIs, or other strongly '
                                                            'serotonergic pairs, can produce '
                                                            'hyperthermia, autonomic '
                                                            'instability, clonus, and altered '
                                                            'mentation. The interaction is '
                                                            'pharmacodynamic amplification of '
                                                            'synaptic serotonin rather than a '
                                                            'simple additive sedative effect.',
                                             'choice_explanations': {'A': 'Combining '
                                                                          'low-potency topical '
                                                                          'corticosteroids '
                                                                          'does not elevate '
                                                                          'central synaptic '
                                                                          'serotonin; steroid '
                                                                          'receptor agonism is '
                                                                          'unrelated to 5-HT '
                                                                          'toxicity.',
                                                                     'B': 'Antacid plus '
                                                                          'alginate modulates '
                                                                          'gastric '
                                                                          'acidity/reflux '
                                                                          'mechanically and '
                                                                          'chemically without '
                                                                          'inhibiting '
                                                                          'monoamine oxidase '
                                                                          'or serotonin '
                                                                          'reuptake.',
                                                                     'C': 'MAOIs impair '
                                                                          'serotonin breakdown '
                                                                          'while SSRIs (and '
                                                                          'related '
                                                                          'serotonergics) '
                                                                          'increase synaptic '
                                                                          '5-HT; together they '
                                                                          'can produce excess '
                                                                          '5-HT2A tone and '
                                                                          'serotonin syndrome.',
                                                                     'D': 'Fluoride toothpaste '
                                                                          'with calcium '
                                                                          'affects dental '
                                                                          'remineralization '
                                                                          'locally; it does '
                                                                          'not raise central '
                                                                          'serotonergic '
                                                                          'neurotransmission.'}},
                                            {'question': 'Narrow therapeutic index warfarin '
                                                         'interaction?',
                                             'options': ['A) Warfarin never has clinically '
                                                         'relevant CYP interactions',
                                                         'B) CYP2C9 induction always lowers '
                                                         'bleeding risk only',
                                                         'C) Toothpaste fluoride is the main '
                                                         'INR determinant',
                                                         'D) CYP2C9 inhibitors can raise INR '
                                                         'and bleed risk'],
                                             'answer': 'D) CYP2C9 inhibitors can raise INR and '
                                                       'bleed risk',
                                             'explanation': 'S-warfarin, the more potent '
                                                            'enantiomer, is cleared largely by '
                                                            'CYP2C9. CYP2C9 inhibitors reduce '
                                                            'S-warfarin clearance, raising '
                                                            'plasma levels and vitamin K '
                                                            'epoxide reductase inhibition. The '
                                                            'resulting increase in INR '
                                                            'prolongs coagulation and elevates '
                                                            'bleeding risk, which is '
                                                            'clinically important because '
                                                            "warfarin's therapeutic index is "
                                                            'narrow.',
                                             'choice_explanations': {'A': 'Warfarin—especially '
                                                                          'S-warfarin via '
                                                                          'CYP2C9—has numerous '
                                                                          'clinically relevant '
                                                                          'metabolic '
                                                                          'interactions that '
                                                                          'change INR and '
                                                                          'bleeding risk.',
                                                                     'B': 'CYP2C9 induction '
                                                                          'increases '
                                                                          'S-warfarin '
                                                                          'clearance and '
                                                                          'typically lowers '
                                                                          'INR (less '
                                                                          'anticoagulant '
                                                                          'effect), so it does '
                                                                          'not always lower '
                                                                          'bleeding risk by a '
                                                                          'single fixed rule '
                                                                          'and is not the '
                                                                          'inhibitor scenario.',
                                                                     'C': 'Toothpaste fluoride '
                                                                          'has negligible '
                                                                          'effect on hepatic '
                                                                          'CYP2C9 clearance of '
                                                                          'S-warfarin; INR is '
                                                                          'driven by vitamin K '
                                                                          'status, genetics, '
                                                                          'and interacting '
                                                                          'drugs.',
                                                                     'D': 'CYP2C9 inhibitors '
                                                                          'reduce clearance of '
                                                                          'S-warfarin, raising '
                                                                          'plasma levels, '
                                                                          'stronger VKORC1 '
                                                                          'inhibition, higher '
                                                                          'INR, and increased '
                                                                          'bleeding risk.'}}]},
                  'cases': {'easy': [{'title': 'New Oral Drug Discussion',
                                      'stem': 'A student asks why an oral dose is much higher '
                                              'than the IV dose for the same drug.',
                                      'question': 'Key concept?',
                                      'answer': 'First-pass hepatic metabolism reducing oral '
                                                'bioavailability.',
                                      'discussion': 'Compare bioavailability and route '
                                                    'selection.',
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
                                              'high-yield next concept before definitive '
                                              'results.',
                                      'question': 'Mechanism theme?',
                                      'answer': 'Induction lowering carbamazepine '
                                                'concentration.',
                                      'discussion': 'Monitor levels and adjust.',
                                      'book_hint': "Rang and Dale's Pharmacology / Katzung"}],
                            'extreme': [{'title': 'Polypharmacy Syncope',
                                         'stem': 'An elderly patient on multiple QT-prolonging '
                                                 'drugs has syncope and polymorphic VT. Avoid '
                                                 'harmful premature treatment while '
                                                 'catastrophic differentials remain open.',
                                         'question': 'Concern?',
                                         'answer': 'Drug-induced TdP — stop offenders, correct '
                                                   'electrolytes, specialist care.',
                                         'discussion': 'Review all QT drugs and interactions.',
                                         'book_hint': "Rang and Dale's Pharmacology / "
                                                      'Katzung'}]}},
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
                                               'options': ['A) Replace all brand products with '
                                                           'the cheapest generic',
                                                           'B) Ensure accurate medication '
                                                           'lists across care transitions',
                                                           'C) Stop therapeutic drug '
                                                           'monitoring for all inpatients',
                                                           'D) Limit counseling to discharge '
                                                           'antibiotics only'],
                                               'answer': 'B) Ensure accurate medication lists '
                                                         'across care transitions',
                                               'explanation': 'Medication reconciliation '
                                                              'systematically compares '
                                                              'medication lists across care '
                                                              'transitions such as admission, '
                                                              'transfer, and discharge. The '
                                                              'process identifies omissions, '
                                                              'duplications, dosing errors, '
                                                              'and unintended discrepancies '
                                                              'between what the patient takes '
                                                              'and what is ordered. Accurate '
                                                              'lists reduce preventable '
                                                              'adverse drug events at '
                                                              'interfaces of care.',
                                               'choice_explanations': {'A': 'Automatic '
                                                                            'brand-to-cheapest-generic '
                                                                            'switches address '
                                                                            'formulary cost, '
                                                                            'not the '
                                                                            'reconciliation '
                                                                            'goal of aligning '
                                                                            'actual medication '
                                                                            'lists across '
                                                                            'transitions of '
                                                                            'care.',
                                                                       'B': 'Medication '
                                                                            'reconciliation '
                                                                            'systematically '
                                                                            'compares lists at '
                                                                            'admission, '
                                                                            'transfer, and '
                                                                            'discharge to '
                                                                            'detect omissions, '
                                                                            'duplications, '
                                                                            'dose errors, and '
                                                                            'unintended '
                                                                            'discrepancies.',
                                                                       'C': 'Stopping '
                                                                            'therapeutic drug '
                                                                            'monitoring '
                                                                            'removes a safety '
                                                                            'tool for '
                                                                            'narrow-index '
                                                                            'drugs and is '
                                                                            'unrelated to '
                                                                            'verifying '
                                                                            'accurate '
                                                                            'medication '
                                                                            'histories across '
                                                                            'care transitions.',
                                                                       'D': 'Limiting '
                                                                            'counseling to '
                                                                            'discharge '
                                                                            'antibiotics '
                                                                            'narrows education '
                                                                            'scope; '
                                                                            'reconciliation '
                                                                            'addresses the '
                                                                            'full medication '
                                                                            'list continuity, '
                                                                            'not a single drug '
                                                                            'class.'}},
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
                                                              'noxious, unintended response to '
                                                              'a medicine at doses used for '
                                                              'prophylaxis, diagnosis, or '
                                                              'therapy. ADRs include augmented '
                                                              '(type A) dose-related effects '
                                                              'and bizarre (type B) '
                                                              'idiosyncratic or '
                                                              'immune-mediated reactions. '
                                                              'Detection, causality '
                                                              'assessment, management, and '
                                                              'spontaneous reporting are core '
                                                              'pharmacovigilance tasks.',
                                               'choice_explanations': {'A': 'Average daily '
                                                                            'requirement is a '
                                                                            'nutrition concept '
                                                                            'for '
                                                                            'vitamins/minerals, '
                                                                            'not the '
                                                                            'pharmacovigilance '
                                                                            'term for '
                                                                            'unintended '
                                                                            'harmful drug '
                                                                            'responses.',
                                                                       'B': 'Authorized '
                                                                            'dispensing record '
                                                                            'describes '
                                                                            'documentation '
                                                                            'workflow, not the '
                                                                            'clinical '
                                                                            'definition of a '
                                                                            'noxious '
                                                                            'unintended drug '
                                                                            'effect.',
                                                                       'C': 'An adverse drug '
                                                                            'reaction (ADR) is '
                                                                            'a noxious, '
                                                                            'unintended '
                                                                            'response to a '
                                                                            'medicine used at '
                                                                            'normal doses for '
                                                                            'prophylaxis, '
                                                                            'diagnosis, or '
                                                                            'therapy, '
                                                                            'including '
                                                                            'augmented and '
                                                                            'idiosyncratic '
                                                                            'types.',
                                                                       'D': 'Absolute dose '
                                                                            'reduction '
                                                                            'annually is a '
                                                                            'dosing strategy, '
                                                                            'not the '
                                                                            'definition of an '
                                                                            'adverse drug '
                                                                            'reaction.'}},
                                              {'question': 'Counseling on antibiotics should '
                                                           'include?',
                                               'options': ['A) Stopping as soon as symptoms '
                                                           'improve by 24 hours',
                                                           'B) Sharing leftover tablets with '
                                                           'household contacts',
                                                           'C) Doubling the dose if a dose was '
                                                           'missed yesterday',
                                                           'D) Completing the course as '
                                                           'directed and stewardship themes'],
                                               'answer': 'D) Completing the course as directed '
                                                         'and stewardship themes',
                                               'explanation': 'Completing an antibiotic course '
                                                              'as prescribed helps eradicate '
                                                              'susceptible pathogens when the '
                                                              'indication, agent, and duration '
                                                              'are appropriate. Unnecessary '
                                                              'prolongation or use without '
                                                              'infection, however, selects for '
                                                              'resistant organisms and harms '
                                                              'stewardship goals. Counseling '
                                                              'therefore balances adherence '
                                                              'with clear advice on '
                                                              'indication, duration, and when '
                                                              'to seek review.',
                                               'choice_explanations': {'A': 'Stopping '
                                                                            'antibiotics after '
                                                                            '24 hours of '
                                                                            'symptom '
                                                                            'improvement can '
                                                                            'leave residual '
                                                                            'viable pathogens '
                                                                            'and select '
                                                                            'resistance when a '
                                                                            'full indicated '
                                                                            'course is still '
                                                                            'warranted.',
                                                                       'B': 'Sharing leftover '
                                                                            'antibiotics '
                                                                            'exposes contacts '
                                                                            'to inappropriate '
                                                                            'spectra/doses '
                                                                            'without '
                                                                            'assessment and '
                                                                            'promotes '
                                                                            'resistance and '
                                                                            'adverse effects.',
                                                                       'C': 'Doubling a missed '
                                                                            'dose can produce '
                                                                            'unnecessary peak '
                                                                            'toxicity without '
                                                                            'reliably '
                                                                            'restoring the '
                                                                            'intended AUC/time '
                                                                            'above MIC '
                                                                            'profile.',
                                                                       'D': 'Completing the '
                                                                            'prescribed course '
                                                                            'when indicated '
                                                                            'supports pathogen '
                                                                            'eradication while '
                                                                            'stewardship '
                                                                            'avoids '
                                                                            'unnecessary '
                                                                            'prolongation; '
                                                                            'counseling covers '
                                                                            'adherence and '
                                                                            'when to seek '
                                                                            'review.'}}],
                                     'medium': [{'question': 'Beers Criteria help identify?',
                                                 'options': ['A) Potentially inappropriate '
                                                             'medicines in older adults',
                                                             'B) IV compatibility charts for '
                                                             'pediatric TPN only',
                                                             'C) Bioequivalence limits for '
                                                             'generic antibiotics',
                                                             'D) WHO essential medicines for '
                                                             'tropical infections'],
                                                 'answer': 'A) Potentially inappropriate '
                                                           'medicines in older adults',
                                                 'explanation': 'Beers Criteria catalog '
                                                                'medicines that are often '
                                                                'potentially inappropriate in '
                                                                'older adults because of '
                                                                'altered pharmacokinetics, '
                                                                'pharmacodynamics, and higher '
                                                                'adverse-effect burden. '
                                                                'Examples include strong '
                                                                'anticholinergics and '
                                                                'long-acting benzodiazepines. '
                                                                'The lists support '
                                                                'deprescribing discussions but '
                                                                'must be individualized to '
                                                                'comorbidity, goals of care, '
                                                                'and safer alternatives.',
                                                 'choice_explanations': {'A': 'Beers Criteria '
                                                                              'list medicines '
                                                                              'that are often '
                                                                              'potentially '
                                                                              'inappropriate '
                                                                              'in older adults '
                                                                              'because of '
                                                                              'age-related '
                                                                              'PK/PD changes '
                                                                              'and higher '
                                                                              'adverse-effect '
                                                                              'rates for '
                                                                              'modest benefit.',
                                                                         'B': 'IV '
                                                                              'compatibility '
                                                                              'charts for '
                                                                              'pediatric TPN '
                                                                              'are '
                                                                              'pharmaceutic/compatibility '
                                                                              'references, not '
                                                                              'geriatric '
                                                                              'potentially-inappropriate-medication '
                                                                              'criteria.',
                                                                         'C': 'Bioequivalence '
                                                                              'limits govern '
                                                                              'generic '
                                                                              'interchangeability '
                                                                              'metrics '
                                                                              '(AUC/Cmax), not '
                                                                              'identification '
                                                                              'of high-risk '
                                                                              'drugs in the '
                                                                              'elderly.',
                                                                         'D': 'WHO essential '
                                                                              'medicines lists '
                                                                              'prioritize '
                                                                              'public-health '
                                                                              'needs globally; '
                                                                              'they are not '
                                                                              'the Beers '
                                                                              'framework for '
                                                                              'geriatric '
                                                                              'prescribing '
                                                                              'risk.'}},
                                                {'question': 'Renal dose adjustment needed '
                                                             'when?',
                                                 'options': ['A) The drug is cleared only by '
                                                             'hepatic CYP3A4',
                                                             'B) Drug is cleared renally and '
                                                             'GFR is reduced',
                                                             'C) The patient has mild seasonal '
                                                             'allergic rhinitis',
                                                             'D) Plasma albumin is high '
                                                             'without renal impairment'],
                                                 'answer': 'B) Drug is cleared renally and GFR '
                                                           'is reduced',
                                                 'explanation': 'When glomerular filtration '
                                                                'rate falls, renally cleared '
                                                                'drugs and active metabolites '
                                                                'accumulate unless the dose or '
                                                                'interval is adjusted. '
                                                                'Accumulation increases '
                                                                'exposure and toxicity risk '
                                                                'for agents such as many '
                                                                'aminoglycosides, '
                                                                'gabapentinoids, and renally '
                                                                'excreted anticoagulants. Dose '
                                                                'adjustment uses estimated '
                                                                'kidney function and '
                                                                'drug-specific renal dosing '
                                                                'guidance.',
                                                 'choice_explanations': {'A': 'Drugs cleared '
                                                                              'solely by '
                                                                              'hepatic CYP3A4 '
                                                                              'are adjusted '
                                                                              'mainly for '
                                                                              'liver '
                                                                              'function/interactions, '
                                                                              'not primarily '
                                                                              'for reduced '
                                                                              'GFR.',
                                                                         'B': 'When GFR falls, '
                                                                              'renally '
                                                                              'eliminated '
                                                                              'parent drugs or '
                                                                              'active '
                                                                              'metabolites '
                                                                              'accumulate, '
                                                                              'raising '
                                                                              'exposure and '
                                                                              'toxicity risk '
                                                                              'unless dose or '
                                                                              'interval is '
                                                                              'reduced.',
                                                                         'C': 'Mild seasonal '
                                                                              'allergic '
                                                                              'rhinitis does '
                                                                              'not impair '
                                                                              'renal clearance '
                                                                              'and does not by '
                                                                              'itself mandate '
                                                                              'renal dose '
                                                                              'adjustment.',
                                                                         'D': 'High albumin '
                                                                              'without renal '
                                                                              'impairment does '
                                                                              'not indicate '
                                                                              'reduced GFR; '
                                                                              'renal dosing '
                                                                              'hinges on renal '
                                                                              'clearance '
                                                                              'capacity for '
                                                                              'renally '
                                                                              'eliminated '
                                                                              'drugs.'}},
                                                {'question': 'Anticoagulant counseling key '
                                                             'point?',
                                                 'options': ['A) Ignore dietary vitamin K '
                                                             'fluctuations entirely',
                                                             'B) Crush all tablets to improve '
                                                             'absorption always',
                                                             'C) Recognize bleeding signs and '
                                                             'interaction awareness',
                                                             'D) Stop therapy whenever a '
                                                             'headache occurs once'],
                                                 'answer': 'C) Recognize bleeding signs and '
                                                           'interaction awareness',
                                                 'explanation': 'Therapeutic anticoagulation '
                                                                'intentionally impairs '
                                                                'hemostasis, so patients must '
                                                                'recognize bleeding warning '
                                                                'signs such as melena, '
                                                                'hematuria, or uncontrolled '
                                                                'bruising. Drug–drug and '
                                                                'drug–food interactions can '
                                                                'raise or lower anticoagulant '
                                                                'effect, especially with '
                                                                'warfarin and some DOAC '
                                                                'pathways. Counseling links '
                                                                'efficacy to safety-net '
                                                                'actions when bleeding or '
                                                                'interacting medicines appear.',
                                                 'choice_explanations': {'A': 'Dietary vitamin '
                                                                              'K fluctuations '
                                                                              'alter vitamin '
                                                                              'K–antagonist '
                                                                              'INR; ignoring '
                                                                              'them undermines '
                                                                              'safe '
                                                                              'anticoagulant '
                                                                              'education for '
                                                                              'warfarin users.',
                                                                         'B': 'Crushing all '
                                                                              'anticoagulant '
                                                                              'tablets can '
                                                                              'destroy '
                                                                              'modified-release '
                                                                              'designs or '
                                                                              'create '
                                                                              'exposure/handling '
                                                                              'hazards; it is '
                                                                              'not a general '
                                                                              'counseling '
                                                                              'rule.',
                                                                         'C': 'Therapeutic '
                                                                              'anticoagulation '
                                                                              'impairs '
                                                                              'hemostasis, so '
                                                                              'patients must '
                                                                              'recognize '
                                                                              'bleeding signs '
                                                                              'and understand '
                                                                              'interacting '
                                                                              'drugs/foods '
                                                                              'that change '
                                                                              'anticoagulant '
                                                                              'effect.',
                                                                         'D': 'Stopping '
                                                                              'anticoagulation '
                                                                              'for a single '
                                                                              'mild headache '
                                                                              'can leave '
                                                                              'high-risk '
                                                                              'patients '
                                                                              'unprotected '
                                                                              'from '
                                                                              'thrombosis; '
                                                                              'headache needs '
                                                                              'assessment, not '
                                                                              'automatic '
                                                                              'cessation.'}}],
                                     'hard': [{'question': 'Vancomycin dosing commonly uses?',
                                               'options': ['A) Ideal body weight only, '
                                                           'ignoring renal function',
                                                           'B) Fixed 1 g for every adult '
                                                           'regardless of levels',
                                                           'C) Hepatic Child–Pugh score as the '
                                                           'primary guide',
                                                           'D) Weight and renal function, '
                                                           'often with level monitoring'],
                                               'answer': 'D) Weight and renal function, often '
                                                         'with level monitoring',
                                               'explanation': 'Vancomycin is a large '
                                                              'glycopeptide cleared '
                                                              'predominantly by glomerular '
                                                              'filtration, so dosing is guided '
                                                              'by actual body weight and renal '
                                                              'function. AUC- or trough-based '
                                                              'therapeutic drug monitoring is '
                                                              'used in many protocols to '
                                                              'balance bactericidal exposure '
                                                              'against nephrotoxicity. Loading '
                                                              'strategies and subsequent '
                                                              'adjustment reflect distribution '
                                                              'volume and changing clearance.',
                                               'choice_explanations': {'A': 'Ideal body weight '
                                                                            'alone ignores '
                                                                            'that vancomycin '
                                                                            'clearance tracks '
                                                                            'renal function '
                                                                            'and that obese '
                                                                            'patients often '
                                                                            'need '
                                                                            'weight-informed '
                                                                            'dosing with '
                                                                            'monitoring.',
                                                                       'B': 'A fixed 1 g for '
                                                                            'every adult '
                                                                            'neglects weight '
                                                                            'and GFR '
                                                                            'differences that '
                                                                            'drive vancomycin '
                                                                            'AUC and '
                                                                            'nephrotoxicity '
                                                                            'risk.',
                                                                       'C': 'Child–Pugh '
                                                                            'hepatic scoring '
                                                                            'guides some '
                                                                            'hepatically '
                                                                            'cleared drugs; '
                                                                            'vancomycin is '
                                                                            'predominantly '
                                                                            'renally cleared, '
                                                                            'so renal function '
                                                                            'dominates dosing.',
                                                                       'D': 'Vancomycin dosing '
                                                                            'uses patient '
                                                                            'weight and renal '
                                                                            'function, with '
                                                                            'AUC- or '
                                                                            'trough-guided '
                                                                            'TDM, because '
                                                                            'clearance is '
                                                                            'mainly glomerular '
                                                                            'filtration.'}},
                                              {'question': 'Hyperkalemia risk with?',
                                               'options': ['A) ACE inhibitor plus '
                                                           'spironolactone combinations',
                                                           'B) Loop diuretic plus thiazide '
                                                           'used together only',
                                                           'C) Short-acting insulin given '
                                                           'before meals',
                                                           'D) Inhaled salbutamol used for '
                                                           'acute asthma'],
                                               'answer': 'A) ACE inhibitor plus spironolactone '
                                                         'combinations',
                                               'explanation': 'ACE inhibitors reduce '
                                                              'angiotensin II–mediated '
                                                              'aldosterone secretion, '
                                                              'decreasing renal potassium '
                                                              'excretion. '
                                                              'Mineralocorticoid-receptor '
                                                              'antagonists such as '
                                                              'spironolactone further block '
                                                              'aldosterone effect in the '
                                                              'collecting duct. Combined use '
                                                              'therefore markedly increases '
                                                              'hyperkalemia risk, especially '
                                                              'in chronic kidney disease or '
                                                              'with potassium supplements.',
                                               'choice_explanations': {'A': 'ACE inhibitors '
                                                                            'reduce '
                                                                            'angiotensin '
                                                                            'II–driven '
                                                                            'aldosterone, '
                                                                            'lowering renal K+ '
                                                                            'excretion, while '
                                                                            'spironolactone '
                                                                            'blocks '
                                                                            'mineralocorticoid '
                                                                            'receptors; '
                                                                            'together they '
                                                                            'synergistically '
                                                                            'raise '
                                                                            'hyperkalemia '
                                                                            'risk.',
                                                                       'B': 'Loop plus '
                                                                            'thiazide '
                                                                            'diuretics '
                                                                            'increase '
                                                                            'kaliuresis and '
                                                                            'typically cause '
                                                                            'hypokalemia, not '
                                                                            'hyperkalemia from '
                                                                            'reduced '
                                                                            'aldosterone '
                                                                            'signaling.',
                                                                       'C': 'Mealtime insulin '
                                                                            'drives K+ into '
                                                                            'cells via '
                                                                            'Na+/K+-ATPase '
                                                                            'stimulation, '
                                                                            'lowering serum '
                                                                            'potassium rather '
                                                                            'than causing '
                                                                            'hyperkalemia.',
                                                                       'D': 'Inhaled '
                                                                            'salbutamol '
                                                                            '(β2-agonist) '
                                                                            'similarly '
                                                                            'promotes '
                                                                            'intracellular K+ '
                                                                            'shift and can '
                                                                            'lower serum K+, '
                                                                            'opposite to '
                                                                            'hyperkalemia '
                                                                            'risk.'}},
                                              {'question': 'Steroid sick-day rules teach?',
                                               'options': ['A) Stop glucocorticoids abruptly '
                                                           'during fever',
                                                           'B) Increase dose during '
                                                           'significant illness per plan',
                                                           'C) Replace oral steroids with '
                                                           'topical cream only',
                                                           'D) Halve the dose whenever '
                                                           'appetite decreases'],
                                               'answer': 'B) Increase dose during significant '
                                                         'illness per plan',
                                               'explanation': 'Long-term exogenous '
                                                              'glucocorticoids suppress the '
                                                              'hypothalamic–pituitary–adrenal '
                                                              'axis, so endogenous cortisol '
                                                              'may be inadequate during '
                                                              'physiologic stress. Sick-day '
                                                              'rules instruct temporary dose '
                                                              'increases during significant '
                                                              'illness, fever, or vomiting '
                                                              'according to an individualized '
                                                              'plan. The goal is to prevent '
                                                              'adrenal crisis from relative '
                                                              'cortisol deficiency.',
                                               'choice_explanations': {'A': 'Abruptly stopping '
                                                                            'chronic '
                                                                            'glucocorticoids '
                                                                            'during illness '
                                                                            'risks adrenal '
                                                                            'crisis because '
                                                                            'HPA suppression '
                                                                            'leaves endogenous '
                                                                            'cortisol '
                                                                            'inadequate for '
                                                                            'stress.',
                                                                       'B': 'Sick-day rules '
                                                                            'increase '
                                                                            'glucocorticoid '
                                                                            'dose during '
                                                                            'significant '
                                                                            'physiologic '
                                                                            'stress (fever, '
                                                                            'infection, '
                                                                            'surgery) to cover '
                                                                            'cortisol needs '
                                                                            'when the HPA axis '
                                                                            'is suppressed.',
                                                                       'C': 'Topical cream '
                                                                            'provides '
                                                                            'negligible '
                                                                            'systemic '
                                                                            'glucocorticoid '
                                                                            'coverage compared '
                                                                            'with physiologic '
                                                                            'stress '
                                                                            'requirements '
                                                                            'during illness.',
                                                                       'D': 'Halving the dose '
                                                                            'when appetite '
                                                                            'falls further '
                                                                            'reduces cortisol '
                                                                            'coverage at a '
                                                                            'time when stress '
                                                                            'may demand more, '
                                                                            'increasing '
                                                                            'adrenal '
                                                                            'insufficiency '
                                                                            'risk.'}}],
                                     'extreme': [{'question': 'Chemotherapy extravasation '
                                                              'priority?',
                                                  'options': ['A) Increase infusion rate to '
                                                              'clear the line faster',
                                                              'B) Apply heat to all vesicants '
                                                              'without identifying the drug',
                                                              'C) Stop infusion and follow '
                                                              'protocol antidote pathway',
                                                              'D) Flush vigorously with large '
                                                              'volumes of undiluted drug'],
                                                  'answer': 'C) Stop infusion and follow '
                                                            'protocol antidote pathway',
                                                  'explanation': 'Vesicant chemotherapy '
                                                                 'extravasated into soft '
                                                                 'tissue can cause severe '
                                                                 'local necrosis through '
                                                                 'direct cytotoxicity and '
                                                                 'inflammation. Immediate '
                                                                 'priorities are to stop the '
                                                                 'infusion, leave or aspirate '
                                                                 'via the cannula as protocol '
                                                                 'directs, and mark the site '
                                                                 'while arranging antidote or '
                                                                 'surgical pathways. '
                                                                 'Agent-specific measures (for '
                                                                 'example dexrazoxane for '
                                                                 'anthracyclines) follow '
                                                                 'institutional extravasation '
                                                                 'protocols.',
                                                  'choice_explanations': {'A': 'Increasing '
                                                                               'infusion rate '
                                                                               'worsens '
                                                                               'extravasation '
                                                                               'injury by '
                                                                               'delivering '
                                                                               'more vesicant '
                                                                               'into '
                                                                               'subcutaneous '
                                                                               'tissue.',
                                                                          'B': 'Heat is '
                                                                               'agent-specific '
                                                                               '(sometimes '
                                                                               'used for vinca '
                                                                               'alkaloids); '
                                                                               'applying heat '
                                                                               'to all '
                                                                               'vesicants '
                                                                               'without '
                                                                               'identifying '
                                                                               'the drug can '
                                                                               'worsen '
                                                                               'anthracycline '
                                                                               'injury.',
                                                                          'C': 'Vesicants '
                                                                               'cause necrosis '
                                                                               'via local '
                                                                               'cytotoxicity; '
                                                                               'immediate stop '
                                                                               'of infusion, '
                                                                               'aspiration '
                                                                               'attempts per '
                                                                               'protocol, and '
                                                                               'drug-specific '
                                                                               'antidote/antidote '
                                                                               'pathway limit '
                                                                               'tissue damage.',
                                                                          'D': 'Flushing with '
                                                                               'undiluted drug '
                                                                               'increases the '
                                                                               'amount of '
                                                                               'vesicant in '
                                                                               'extravasated '
                                                                               'tissue and is '
                                                                               'contraindicated.'}},
                                                 {'question': 'Clozapine pharmacy monitoring '
                                                              'theme?',
                                                  'options': ['A) Only liver enzymes every '
                                                              'five years',
                                                              'B) Only fasting lipids on day '
                                                              'one of therapy',
                                                              'C) Only blood pressure after '
                                                              'each dose forever',
                                                              'D) Mandatory blood counts for '
                                                              'agranulocytosis risk'],
                                                  'answer': 'D) Mandatory blood counts for '
                                                            'agranulocytosis risk',
                                                  'explanation': 'Clozapine can cause '
                                                                 'idiosyncratic '
                                                                 'agranulocytosis through '
                                                                 'toxic or immune-mediated '
                                                                 'injury to neutrophils. '
                                                                 'Mandatory scheduled full '
                                                                 'blood counts detect falling '
                                                                 'absolute neutrophil counts '
                                                                 'before life-threatening '
                                                                 'infection develops. '
                                                                 'Dispensing is typically '
                                                                 'linked to registry or '
                                                                 'protocol confirmation that '
                                                                 'hematologic monitoring '
                                                                 'remains within acceptable '
                                                                 'limits.',
                                                  'choice_explanations': {'A': 'Liver enzymes '
                                                                               'every five '
                                                                               'years miss the '
                                                                               'rapid '
                                                                               'agranulocytosis '
                                                                               'risk that '
                                                                               'requires '
                                                                               'frequent '
                                                                               'scheduled '
                                                                               'neutrophil '
                                                                               'monitoring '
                                                                               'early and '
                                                                               'ongoing.',
                                                                          'B': 'A single '
                                                                               'day-one lipid '
                                                                               'panel does not '
                                                                               'detect '
                                                                               'clozapine-induced '
                                                                               'agranulocytosis; '
                                                                               'mandatory '
                                                                               'hematologic '
                                                                               'monitoring is '
                                                                               'the safety '
                                                                               'cornerstone.',
                                                                          'C': 'Blood pressure '
                                                                               'checks address '
                                                                               'metabolic/orthostatic '
                                                                               'issues but do '
                                                                               'not substitute '
                                                                               'for absolute '
                                                                               'neutrophil '
                                                                               'count '
                                                                               'surveillance '
                                                                               'for '
                                                                               'agranulocytosis.',
                                                                          'D': 'Clozapine can '
                                                                               'cause '
                                                                               'idiosyncratic '
                                                                               'agranulocytosis; '
                                                                               'mandatory '
                                                                               'timed full '
                                                                               'blood counts '
                                                                               'detect falling '
                                                                               'ANC so therapy '
                                                                               'can be stopped '
                                                                               'before '
                                                                               'life-threatening '
                                                                               'infection.'}},
                                                 {'question': 'Opioid stewardship in hospital '
                                                              'includes?',
                                                  'options': ['A) Appropriate indication, '
                                                              'dose, naloxone awareness, '
                                                              'constipation prophylaxis',
                                                              'B) Automatic escalation to '
                                                              'long-acting opioids for all '
                                                              'acute pain',
                                                              'C) Avoiding laxatives to '
                                                              'prevent opioid withdrawal',
                                                              'D) Discharging all patients '
                                                              'with unlimited PRN refills'],
                                                  'answer': 'A) Appropriate indication, dose, '
                                                            'naloxone awareness, constipation '
                                                            'prophylaxis',
                                                  'explanation': 'Hospital opioid stewardship '
                                                                 'matches opioid choice and '
                                                                 'dose to verified pain '
                                                                 'indication while minimizing '
                                                                 'respiratory depression and '
                                                                 'misuse risk. Naloxone '
                                                                 'availability and education '
                                                                 'address μ-opioid receptor '
                                                                 'overdose reversibility. '
                                                                 'Because opioids slow gut '
                                                                 'motility via enteric '
                                                                 'μ-receptors, prophylactic '
                                                                 'laxatives are routine to '
                                                                 'prevent opioid-induced '
                                                                 'constipation.',
                                                  'choice_explanations': {'A': 'Opioid '
                                                                               'stewardship '
                                                                               'requires '
                                                                               'verified '
                                                                               'indication, '
                                                                               'appropriate '
                                                                               'dose '
                                                                               'titration, '
                                                                               'naloxone '
                                                                               'readiness for '
                                                                               'respiratory '
                                                                               'depression, '
                                                                               'and stimulant '
                                                                               'laxatives '
                                                                               'because '
                                                                               'μ-agonists '
                                                                               'slow gut '
                                                                               'motility.',
                                                                          'B': 'Automatic '
                                                                               'escalation to '
                                                                               'long-acting '
                                                                               'opioids for '
                                                                               'all acute pain '
                                                                               'increases '
                                                                               'accumulation '
                                                                               'and overdose '
                                                                               'risk without '
                                                                               'matching '
                                                                               'pharmacokinetics '
                                                                               'to acute pain '
                                                                               'trajectories.',
                                                                          'C': 'Avoiding '
                                                                               'laxatives '
                                                                               'worsens '
                                                                               'opioid-induced '
                                                                               'constipation; '
                                                                               'prophylaxis is '
                                                                               'part of '
                                                                               'stewardship, '
                                                                               'not a cause of '
                                                                               'withdrawal.',
                                                                          'D': 'Unlimited PRN '
                                                                               'refills at '
                                                                               'discharge '
                                                                               'facilitate '
                                                                               'misuse and '
                                                                               'diversion '
                                                                               'without '
                                                                               'clinical '
                                                                               'reassessment '
                                                                               'of ongoing '
                                                                               'opioid '
                                                                               'need.'}}]},
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
                                             'stem': 'An older adult on multiple sedating '
                                                     'drugs has recurrent falls.',
                                             'question': 'Pharmacy action theme?',
                                             'answer': 'Review sedatives; consider '
                                                       'deprescribing per Beers/STOPP themes.',
                                             'discussion': 'Falls are a major ADR outcome.',
                                             'book_hint': 'Clinical Pharmacy and Therapeutics '
                                                          '— Walker/Whittlesea'}],
                                 'hard': [{'title': 'Rising Creatinine on Dual Blockade',
                                           'stem': 'Patient on ACEI + NSAID + diuretic has '
                                                   'rising creatinine. Choose the safest '
                                                   'high-yield next concept before definitive '
                                                   'results.',
                                           'question': 'Triple whammy concept?',
                                           'answer': 'Hemodynamically mediated AKI risk — '
                                                     'review and modify regimen.',
                                           'discussion': 'Hydration and follow-up labs matter.',
                                           'book_hint': 'Clinical Pharmacy and Therapeutics — '
                                                        'Walker/Whittlesea'}],
                                 'extreme': [{'title': 'Neutropenic Fever Post Chemo',
                                              'stem': 'A patient on myelosuppressive chemo '
                                                      'presents febrile and unwell. Avoid '
                                                      'harmful premature treatment while '
                                                      'catastrophic differentials remain open.',
                                              'question': 'Pharmacy/clinical priority concept?',
                                              'answer': 'Urgent sepsis pathway and protocol '
                                                        'antibiotics; review chemo '
                                                        'timing/growth factors per oncology '
                                                        'plan.',
                                              'discussion': 'Do not delay for outpatient '
                                                            'review.',
                                              'book_hint': 'Clinical Pharmacy and Therapeutics '
                                                           '— Walker/Whittlesea'}]}},
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
                                                       'C) Hold powder particles together in '
                                                       'the compact',
                                                       'D) Sterilize the blend during '
                                                       'compression'],
                                           'answer': 'C) Hold powder particles together in the '
                                                     'compact',
                                           'explanation': 'Binders are tablet excipients that '
                                                          'adhesively link powder particles '
                                                          'during granulation or compression, '
                                                          'imparting mechanical strength to '
                                                          'the compact. Adequate binding '
                                                          'reduces friability and capping, '
                                                          'while excess binder can slow '
                                                          'disintegration and dissolution. '
                                                          'Common examples include povidone, '
                                                          'starch paste, and cellulose '
                                                          'derivatives.',
                                           'choice_explanations': {'A': 'Increasing '
                                                                        'disintegration speed '
                                                                        'alone is typically '
                                                                        'the role of '
                                                                        'disintegrants, which '
                                                                        'promote breakup; '
                                                                        'binders increase '
                                                                        'cohesive strength and '
                                                                        'can slow '
                                                                        'disintegration if '
                                                                        'overused.',
                                                                   'B': 'Taste masking uses '
                                                                        'coatings/flavors/complexation; '
                                                                        'binders primarily '
                                                                        'provide mechanical '
                                                                        'integrity of the '
                                                                        'compact, not '
                                                                        'organoleptic masking '
                                                                        'per se.',
                                                                   'C': 'Binders adhesively '
                                                                        'link powder particles '
                                                                        'during granulation or '
                                                                        'compression, '
                                                                        'imparting tensile '
                                                                        'strength so the '
                                                                        'tablet holds together '
                                                                        'as a compact.',
                                                                   'D': 'Compression binders '
                                                                        'do not sterilize '
                                                                        'blends; sterility '
                                                                        'requires validated '
                                                                        'sterilization or '
                                                                        'aseptic processing, '
                                                                        'not binder '
                                                                        'chemistry.'}},
                                          {'question': 'Bioavailability compares?',
                                           'options': ['A) Tablet hardness and friability '
                                                       'scores only',
                                                       'B) Shelf-life under accelerated '
                                                       'humidity stress',
                                                       'C) Cost per milligram across brand '
                                                       'products',
                                                       'D) Rate and extent of drug reaching '
                                                       'systemic circulation'],
                                           'answer': 'D) Rate and extent of drug reaching '
                                                     'systemic circulation',
                                           'explanation': 'Bioavailability is the rate and '
                                                          'extent to which unchanged drug '
                                                          'reaches the systemic circulation. '
                                                          'Extent is commonly quantified by '
                                                          'area under the plasma '
                                                          'concentration–time curve (AUC) '
                                                          'relative to an intravenous '
                                                          'reference for absolute '
                                                          'bioavailability. Rate is reflected '
                                                          'in parameters such as Cmax and '
                                                          'tmax, which matter for onset and '
                                                          'peak effect.',
                                           'choice_explanations': {'A': 'Hardness and '
                                                                        'friability measure '
                                                                        'mechanical tablet '
                                                                        'strength, not the '
                                                                        'fraction of dose that '
                                                                        'reaches systemic '
                                                                        'circulation.',
                                                                   'B': 'Accelerated '
                                                                        'shelf-life testing '
                                                                        'assesses '
                                                                        'chemical/physical '
                                                                        'stability under '
                                                                        'stress, not systemic '
                                                                        'exposure metrics.',
                                                                   'C': 'Cost per milligram is '
                                                                        'an economic '
                                                                        'comparison, unrelated '
                                                                        'to rate and extent of '
                                                                        'absorption into '
                                                                        'blood.',
                                                                   'D': 'Bioavailability is '
                                                                        'the rate and extent '
                                                                        'to which unchanged '
                                                                        'drug reaches systemic '
                                                                        'circulation, commonly '
                                                                        'assessed by Cmax/Tmax '
                                                                        'and AUC relative to a '
                                                                        'reference.'}},
                                          {'question': 'Sterile products must be?',
                                           'options': ['A) Free from viable microorganisms per '
                                                       'specifications',
                                                       'B) Colored red to indicate parenteral '
                                                       'use',
                                                       'C) Stored only in amber glass '
                                                       'regardless of light sensitivity',
                                                       'D) Isotonic with plasma even for oral '
                                                       'liquids'],
                                           'answer': 'A) Free from viable microorganisms per '
                                                     'specifications',
                                           'explanation': 'Sterility means the absence of '
                                                          'viable contaminating microorganisms '
                                                          'in the finished product within the '
                                                          'sensitivity of validated sterility '
                                                          'assurance processes. Injectable and '
                                                          'ophthalmic preparations require '
                                                          'sterilization or aseptic '
                                                          'manufacture because parenteral '
                                                          'routes bypass skin and mucosal '
                                                          'barriers. Failure of sterility can '
                                                          'cause severe infection including '
                                                          'sepsis.',
                                           'choice_explanations': {'A': 'Sterile products must '
                                                                        'meet validated '
                                                                        'sterility '
                                                                        'assurance—absence of '
                                                                        'viable contaminating '
                                                                        'microorganisms within '
                                                                        'specified process '
                                                                        'capability—because '
                                                                        'parenteral/ophthalmic '
                                                                        'routes bypass many '
                                                                        'host defenses.',
                                                                   'B': 'Red coloring is not a '
                                                                        'sterility criterion; '
                                                                        'colorants do not '
                                                                        'equate to microbial '
                                                                        'kill or removal.',
                                                                   'C': 'Amber glass protects '
                                                                        'light-sensitive drugs '
                                                                        'but is not required '
                                                                        'for all sterile '
                                                                        'products and does not '
                                                                        'itself define '
                                                                        'sterility.',
                                                                   'D': 'Isotonicity with '
                                                                        'plasma is important '
                                                                        'for many injectables '
                                                                        'to limit tissue '
                                                                        'irritation, but oral '
                                                                        'liquids are not '
                                                                        'sterile-product '
                                                                        'requirements and '
                                                                        'isotonicity is not '
                                                                        'the sterility '
                                                                        'definition.'}}],
                                 'medium': [{'question': 'BCS Class II drugs are?',
                                             'options': ['A) High solubility and low '
                                                         'permeability',
                                                         'B) Low solubility and high '
                                                         'permeability',
                                                         'C) High solubility and high '
                                                         'permeability',
                                                         'D) Low solubility and low '
                                                         'permeability'],
                                             'answer': 'B) Low solubility and high '
                                                       'permeability',
                                             'explanation': 'The Biopharmaceutics '
                                                            'Classification System places '
                                                            'Class II drugs in the low aqueous '
                                                            'solubility, high intestinal '
                                                            'permeability quadrant. For these '
                                                            'compounds, dissolution in '
                                                            'gastrointestinal fluid is '
                                                            'frequently rate-limiting for '
                                                            'absorption. Formulation '
                                                            'strategies that increase '
                                                            'dissolution rate (particle size '
                                                            'reduction, salts, solid '
                                                            'dispersions) therefore often '
                                                            'improve oral bioavailability.',
                                             'choice_explanations': {'A': 'High solubility '
                                                                          'with low '
                                                                          'permeability '
                                                                          'defines BCS Class '
                                                                          'III, where '
                                                                          'permeability—not '
                                                                          'dissolution—often '
                                                                          'rate-limits '
                                                                          'absorption.',
                                                                     'B': 'BCS Class II drugs '
                                                                          'have low aqueous '
                                                                          'solubility and high '
                                                                          'intestinal '
                                                                          'permeability, so '
                                                                          'dissolution/solubilization '
                                                                          'commonly limits '
                                                                          'oral absorption '
                                                                          'rate and extent.',
                                                                     'C': 'High solubility and '
                                                                          'high permeability '
                                                                          'define BCS Class I, '
                                                                          'where absorption is '
                                                                          'usually less '
                                                                          'formulation-limited.',
                                                                     'D': 'Low solubility and '
                                                                          'low permeability '
                                                                          'define BCS Class '
                                                                          'IV, the most '
                                                                          'challenging '
                                                                          'biopharmaceutic '
                                                                          'quadrant.'}},
                                            {'question': 'Lyophilization is?',
                                             'options': ['A) Spray-drying of oils into soft '
                                                         'gelatin capsules',
                                                         'B) Wet granulation with alcoholic '
                                                         'binders',
                                                         'C) Freeze-drying by sublimation '
                                                         'under vacuum',
                                                         'D) Hot-melt extrusion of crystalline '
                                                         'APIs only'],
                                             'answer': 'C) Freeze-drying by sublimation under '
                                                       'vacuum',
                                             'explanation': 'Lyophilization (freeze-drying) '
                                                            'removes water by sublimation from '
                                                            'a frozen product under vacuum, '
                                                            'yielding a dry solid cake. Lower '
                                                            'residual moisture slows '
                                                            'hydrolysis and many other '
                                                            'degradation pathways, improving '
                                                            'stability of injectables and '
                                                            'biologics. The process also '
                                                            'enables reconstitution to a '
                                                            'solution at the point of use.',
                                             'choice_explanations': {'A': 'Spray-drying oils '
                                                                          'into softgels is a '
                                                                          'different '
                                                                          'manufacturing '
                                                                          'approach; '
                                                                          'lyophilization '
                                                                          'specifically '
                                                                          'freezes then '
                                                                          'sublimes ice under '
                                                                          'vacuum.',
                                                                     'B': 'Wet granulation '
                                                                          'with alcoholic '
                                                                          'binders builds '
                                                                          'granules for '
                                                                          'tablets; it is not '
                                                                          'freeze-drying by '
                                                                          'sublimation.',
                                                                     'C': 'Lyophilization '
                                                                          'freezes the product '
                                                                          'then removes water '
                                                                          'by sublimation '
                                                                          'under vacuum, '
                                                                          'yielding a porous '
                                                                          'dry cake with low '
                                                                          'residual moisture '
                                                                          'for stability.',
                                                                     'D': 'Hot-melt extrusion '
                                                                          'plasticizes/melts '
                                                                          'material through a '
                                                                          'die; it is thermal '
                                                                          'processing, not ice '
                                                                          'sublimation under '
                                                                          'vacuum.'}},
                                            {'question': 'Osmotic pump tablets provide?',
                                             'options': ['A) Immediate burst release triggered '
                                                         'by chewing',
                                                         'B) pH-independent taste masking only',
                                                         'C) Zero gastric emptying for all '
                                                         'meal states',
                                                         'D) Controlled release driven by '
                                                         'osmotic pressure'],
                                             'answer': 'D) Controlled release driven by '
                                                       'osmotic pressure',
                                             'explanation': 'Osmotic pump tablets admit water '
                                                            'through a semipermeable membrane; '
                                                            'osmotic pressure then drives drug '
                                                            'solution out through a '
                                                            'laser-drilled orifice at a '
                                                            'controlled rate. Release is '
                                                            'relatively independent of '
                                                            'gastrointestinal pH and motility '
                                                            'within design limits. Crushing '
                                                            'destroys the membrane system and '
                                                            'can cause dose dumping.',
                                             'choice_explanations': {'A': 'Immediate burst '
                                                                          'release from '
                                                                          'chewing destroys '
                                                                          'controlled osmotic '
                                                                          'delivery and is not '
                                                                          'the design intent '
                                                                          'of osmotic pumps.',
                                                                     'B': 'pH-independent '
                                                                          'taste masking may '
                                                                          'use '
                                                                          'coatings/complexes; '
                                                                          'osmotic pumps '
                                                                          'primarily meter '
                                                                          'drug release via '
                                                                          'osmotic pressure '
                                                                          'through an orifice.',
                                                                     'C': 'Osmotic tablets do '
                                                                          'not freeze gastric '
                                                                          'emptying across '
                                                                          'meal states; they '
                                                                          'control release '
                                                                          'after water ingress '
                                                                          'regardless of that '
                                                                          'claim.',
                                                                     'D': 'Water enters '
                                                                          'through a '
                                                                          'semipermeable '
                                                                          'membrane; osmotic '
                                                                          'pressure then '
                                                                          'drives drug '
                                                                          'solution out a '
                                                                          'laser-drilled '
                                                                          'orifice at a '
                                                                          'controlled, often '
                                                                          'near zero-order, '
                                                                          'rate.'}}],
                                 'hard': [{'question': 'Noyes–Whitney relates to?',
                                           'options': ['A) Dissolution rate of solid drugs',
                                                       'B) Protein binding equilibrium '
                                                       'constants',
                                                       'C) Renal tubular secretion capacity',
                                                       'D) Tablet punch pressure calibration '
                                                       'only'],
                                           'answer': 'A) Dissolution rate of solid drugs',
                                           'explanation': 'The Noyes–Whitney equation states '
                                                          'that dissolution rate is '
                                                          'proportional to surface area and to '
                                                          'the concentration gradient between '
                                                          "the drug's saturation solubility at "
                                                          'the particle surface and the bulk '
                                                          'solution. A diffusion layer '
                                                          'thickness term and diffusion '
                                                          'coefficient also govern mass '
                                                          'transport. Particle-size reduction '
                                                          'increases surface area and thus '
                                                          'often accelerates dissolution.',
                                           'choice_explanations': {'A': 'The Noyes–Whitney '
                                                                        'equation states '
                                                                        'dissolution rate is '
                                                                        'proportional to '
                                                                        'surface area and the '
                                                                        'concentration '
                                                                        'gradient between '
                                                                        'saturation solubility '
                                                                        'at the solid surface '
                                                                        'and bulk solution '
                                                                        'concentration.',
                                                                   'B': 'Protein-binding '
                                                                        'equilibria are '
                                                                        'governed by '
                                                                        'association constants '
                                                                        'and free fraction, '
                                                                        'not the Noyes–Whitney '
                                                                        'dissolution flux '
                                                                        'relationship.',
                                                                   'C': 'Renal tubular '
                                                                        'secretion capacity '
                                                                        'reflects '
                                                                        'transporter-mediated '
                                                                        'clearance, unrelated '
                                                                        'to solid-drug '
                                                                        'dissolution kinetics.',
                                                                   'D': 'Punch pressure '
                                                                        'calibration is a '
                                                                        'process/engineering '
                                                                        'control for '
                                                                        'compression force, '
                                                                        'not the '
                                                                        'dissolution-rate '
                                                                        'equation.'}},
                                          {'question': 'Partition coefficient (log P) '
                                                       'indicates?',
                                           'options': ['A) Aqueous solubility at every pH '
                                                       'equally',
                                                       'B) Lipophilicity of the unionized '
                                                       'species',
                                                       'C) Melting point of polymorphic forms',
                                                       'D) Tablet disintegration time in vivo'],
                                           'answer': 'B) Lipophilicity of the unionized '
                                                     'species',
                                           'explanation': 'The partition coefficient P is the '
                                                          'equilibrium concentration ratio of '
                                                          'unionized solute between octanol '
                                                          'and water, usually expressed as log '
                                                          'P. Higher log P indicates greater '
                                                          'lipophilicity, favoring membrane '
                                                          'permeation but often reducing '
                                                          'aqueous solubility. Log P therefore '
                                                          'helps predict absorption, '
                                                          'distribution, and formulation '
                                                          'challenges.',
                                           'choice_explanations': {'A': 'Aqueous solubility '
                                                                        'varies with '
                                                                        'ionization and pH '
                                                                        '(pH–solubility '
                                                                        'profile); log P '
                                                                        'specifically reports '
                                                                        'partitioning of the '
                                                                        'unionized species, '
                                                                        'not solubility at '
                                                                        'every pH.',
                                                                   'B': 'Log P is the '
                                                                        'octanol–water '
                                                                        'partition coefficient '
                                                                        'of the unionized '
                                                                        'form, quantifying '
                                                                        'lipophilicity that '
                                                                        'influences membrane '
                                                                        'permeation and '
                                                                        'distribution.',
                                                                   'C': 'Melting points of '
                                                                        'polymorphs reflect '
                                                                        'crystal lattice '
                                                                        'energy differences, '
                                                                        'not the equilibrium '
                                                                        'partition coefficient '
                                                                        'of the solute.',
                                                                   'D': 'In vivo '
                                                                        'disintegration time '
                                                                        'depends on '
                                                                        'formulation and GI '
                                                                        'fluids; it is not '
                                                                        'what log P '
                                                                        'measures.'}},
                                          {'question': 'HLB system helps select?',
                                           'options': ['A) Capsule shell gelatin bloom '
                                                       'strength',
                                                       'B) Autoclave cycle hold times for '
                                                       'vials',
                                                       'C) Emulsifying agents for oil–water '
                                                       'systems',
                                                       'D) Sieve sizes for powder blending '
                                                       'only'],
                                           'answer': 'C) Emulsifying agents for oil–water '
                                                     'systems',
                                           'explanation': 'The hydrophilic–lipophilic balance '
                                                          '(HLB) scale ranks surfactants by '
                                                          'their relative affinity for water '
                                                          'versus oil. Low-HLB agents tend to '
                                                          'stabilize water-in-oil emulsions, '
                                                          'whereas higher-HLB agents favor '
                                                          'oil-in-water systems. Formulators '
                                                          'select emulsifiers (or blends) '
                                                          'whose HLB matches the required '
                                                          'emulsion type and oil phase.',
                                           'choice_explanations': {'A': 'Gelatin bloom '
                                                                        'strength '
                                                                        'characterizes capsule '
                                                                        'shell mechanical '
                                                                        'properties, not '
                                                                        'surfactant '
                                                                        'hydrophilic–lipophilic '
                                                                        'balance for '
                                                                        'emulsions.',
                                                                   'B': 'Autoclave hold times '
                                                                        'are sterilization '
                                                                        'cycle parameters, '
                                                                        'unrelated to '
                                                                        'HLB-based emulsifier '
                                                                        'selection.',
                                                                   'C': 'The HLB scale ranks '
                                                                        'surfactants by '
                                                                        'relative '
                                                                        'hydrophilicity versus '
                                                                        'lipophilicity to '
                                                                        'match emulsifiers to '
                                                                        'oil-in-water or '
                                                                        'water-in-oil systems.',
                                                                   'D': 'Sieve sizes control '
                                                                        'particle-size '
                                                                        'distribution for '
                                                                        'blending/content '
                                                                        'uniformity, not '
                                                                        'emulsifier selection '
                                                                        'via HLB.'}}],
                                 'extreme': [{'question': 'Nanoparticle carriers aim to?',
                                              'options': ['A) Eliminate the need for any '
                                                          'excipients forever',
                                                          'B) Convert all drugs into '
                                                          'immediate-release syrups',
                                                          'C) Guarantee 100% oral '
                                                          'bioavailability always',
                                                          'D) Modify distribution, targeting, '
                                                          'or solubility profiles'],
                                              'answer': 'D) Modify distribution, targeting, or '
                                                        'solubility profiles',
                                              'explanation': 'Nanoparticle carriers such as '
                                                             'liposomes, polymeric '
                                                             'nanoparticles, and lipid '
                                                             "nanoparticles alter a drug's "
                                                             'effective solubility, '
                                                             'circulation time, and tissue '
                                                             'distribution. Surface properties '
                                                             'and size can promote passive '
                                                             'accumulation or ligand-mediated '
                                                             'targeting while protecting '
                                                             'labile actives. These systems '
                                                             'are formulation tools to '
                                                             'optimize pharmacokinetics and '
                                                             'local exposure rather than '
                                                             "changing the drug's intrinsic "
                                                             'receptor pharmacology alone.',
                                              'choice_explanations': {'A': 'Nanocarriers still '
                                                                           'require '
                                                                           'formulation '
                                                                           'components; they '
                                                                           'do not eliminate '
                                                                           'excipients from '
                                                                           'pharmaceutical '
                                                                           'design.',
                                                                      'B': 'Nanoparticles are '
                                                                           'not used to '
                                                                           'convert all drugs '
                                                                           'into '
                                                                           'immediate-release '
                                                                           'syrups; they often '
                                                                           'prolong '
                                                                           'circulation or '
                                                                           'control release.',
                                                                      'C': 'They cannot '
                                                                           'guarantee 100% '
                                                                           'oral '
                                                                           'bioavailability; '
                                                                           'many barriers '
                                                                           '(dissolution, '
                                                                           'permeation, '
                                                                           'first-pass) remain '
                                                                           'molecule- and '
                                                                           'formulation-dependent.',
                                                                      'D': 'Nanoparticle '
                                                                           'carriers '
                                                                           '(liposomes, '
                                                                           'polymeric/lipid '
                                                                           'NPs) alter '
                                                                           'effective '
                                                                           'solubility, '
                                                                           'pharmacokinetics, '
                                                                           'tissue '
                                                                           'distribution, and '
                                                                           'targeting relative '
                                                                           'to free drug.'}},
                                             {'question': 'Glass transition (Tg) matters for?',
                                              'options': ['A) Amorphous solid physical '
                                                          'stability and mobility',
                                                          'B) Only crystalline melting point '
                                                          'determination',
                                                          'C) Only capsule locking ring '
                                                          'dimensions',
                                                          'D) Only syringe needle gauge '
                                                          'selection'],
                                              'answer': 'A) Amorphous solid physical stability '
                                                        'and mobility',
                                              'explanation': 'The glass transition temperature '
                                                             '(Tg) is the temperature region '
                                                             'where an amorphous solid softens '
                                                             'from a glassy to a rubbery state '
                                                             'with increased molecular '
                                                             'mobility. Above Tg, '
                                                             'crystallization and chemical '
                                                             'degradation of amorphous drugs '
                                                             'or dispersions accelerate. '
                                                             'Storage well below Tg, with '
                                                             'controlled moisture '
                                                             'plasticization, is therefore '
                                                             'critical for amorphous physical '
                                                             'stability.',
                                              'choice_explanations': {'A': 'Above Tg, '
                                                                           'amorphous solids '
                                                                           'gain molecular '
                                                                           'mobility that '
                                                                           'accelerates '
                                                                           'crystallization '
                                                                           'and chemical '
                                                                           'degradation; Tg '
                                                                           'therefore governs '
                                                                           'physical stability '
                                                                           'of amorphous '
                                                                           'formulations.',
                                                                      'B': 'Crystalline '
                                                                           'melting point (Tm) '
                                                                           'characterizes '
                                                                           'ordered crystals; '
                                                                           'Tg is the '
                                                                           'glass-to-rubber '
                                                                           'transition of '
                                                                           'amorphous '
                                                                           'materials, not '
                                                                           'melting of '
                                                                           'crystals.',
                                                                      'C': 'Capsule '
                                                                           'locking-ring '
                                                                           'dimensions are '
                                                                           'mechanical design '
                                                                           'features unrelated '
                                                                           'to amorphous '
                                                                           'molecular '
                                                                           'mobility.',
                                                                      'D': 'Syringe needle '
                                                                           'gauge is a '
                                                                           'delivery-device '
                                                                           'parameter, not a '
                                                                           'solid-state '
                                                                           'glass-transition '
                                                                           'property.'}},
                                             {'question': 'Extractables/leachables concern in?',
                                              'options': ['A) Oral sugar-coated tablets '
                                                          'exclusively',
                                                          'B) Container–closure systems for '
                                                          'injectables',
                                                          'C) Hardness testing of chewable '
                                                          'vitamins',
                                                          'D) Color lake selection for film '
                                                          'coats only'],
                                              'answer': 'B) Container–closure systems for '
                                                        'injectables',
                                              'explanation': 'Extractables are compounds that '
                                                             'can be pulled from packaging '
                                                             'under aggressive laboratory '
                                                             'conditions; leachables migrate '
                                                             'into the product under real '
                                                             'storage. For injectables, '
                                                             'container–closure systems '
                                                             '(elastomers, plastics, glass) '
                                                             'are primary sources of such '
                                                             'impurities. Leachables may cause '
                                                             'toxicity, particulate issues, or '
                                                             'drug degradation, so materials '
                                                             'are qualified with '
                                                             'extractable/leachable studies.',
                                              'choice_explanations': {'A': 'Sugar-coated oral '
                                                                           'tablets have lower '
                                                                           'leachables concern '
                                                                           'than parenteral '
                                                                           'container–closure '
                                                                           'systems contacting '
                                                                           'sterile solutions '
                                                                           'for prolonged '
                                                                           'storage.',
                                                                      'B': 'Extractables/leachables '
                                                                           'from elastomers, '
                                                                           'plastics, and '
                                                                           'coatings can '
                                                                           'migrate into '
                                                                           'injectables; '
                                                                           'assessing '
                                                                           'container–closure '
                                                                           'systems protects '
                                                                           'purity and safety '
                                                                           'of parenteral '
                                                                           'products.',
                                                                      'C': 'Hardness testing '
                                                                           'of chewables '
                                                                           'measures '
                                                                           'mechanical '
                                                                           'strength, not '
                                                                           'chemical migration '
                                                                           'from packaging '
                                                                           'into drug product.',
                                                                      'D': 'Color-lake '
                                                                           'selection for film '
                                                                           'coats is a '
                                                                           'formulation '
                                                                           'aesthetic/process '
                                                                           'choice, not the '
                                                                           'primary '
                                                                           'extractables/leachables '
                                                                           'concern for '
                                                                           'injectables.'}}]},
                   'cases': {'easy': [{'title': 'Why Not Crush This Tablet?',
                                       'stem': 'A nurse asks to crush an enteric-coated tablet '
                                               'for a tube feed.',
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
                                               'Choose the safest high-yield next concept '
                                               'before definitive results.',
                                       'question': 'Concern?',
                                       'answer': 'Incompatibility/precipitation — do not '
                                                 'infuse; check compatibility resources.',
                                       'discussion': 'Line flushing/separation strategies.',
                                       'book_hint': "Aulton's Pharmaceutics"}],
                             'extreme': [{'title': 'Biologic Aggregation After Shaking',
                                          'stem': 'A nurse vigorously shakes a protein '
                                                  'biologic; product foams. Avoid harmful '
                                                  'premature treatment while catastrophic '
                                                  'differentials remain open.',
                                          'question': 'Issue?',
                                          'answer': 'Possible denaturation/aggregation — '
                                                    'follow handling IFU; may need to discard '
                                                    'per protocol.',
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
                                                          'B) Absorption of 50% of an oral '
                                                          'dose',
                                                          'C) Distribution equilibrium with '
                                                          'every tissue',
                                                          'D) Plasma concentration to fall by '
                                                          '50%'],
                                              'answer': 'D) Plasma concentration to fall by '
                                                        '50%',
                                              'explanation': 'Elimination half-life (t½) is '
                                                             'the time required for plasma '
                                                             'drug concentration to decrease '
                                                             'by 50% during the terminal '
                                                             'elimination phase in linear '
                                                             'kinetics. It is determined by '
                                                             'both clearance and volume of '
                                                             'distribution (t½ ≈ 0.693 × '
                                                             'Vd/CL). Half-life informs dosing '
                                                             'interval selection and the time '
                                                             'needed to approach steady state.',
                                              'choice_explanations': {'A': 'Complete '
                                                                           'elimination of all '
                                                                           'drug would require '
                                                                           'theoretically '
                                                                           'infinite '
                                                                           'half-lives in '
                                                                           'linear kinetics '
                                                                           '(~97% after ~5 '
                                                                           't½), so t½ is not '
                                                                           'defined as total '
                                                                           'body clearance '
                                                                           'completion.',
                                                                      'B': 'Absorption of 50% '
                                                                           'of an oral dose '
                                                                           'relates to '
                                                                           'absorption '
                                                                           'kinetics/Ka, not '
                                                                           'the elimination '
                                                                           'half-life of the '
                                                                           'decline phase.',
                                                                      'C': 'Distribution '
                                                                           'equilibrium timing '
                                                                           'depends on '
                                                                           'intercompartmental '
                                                                           'clearances; t½ '
                                                                           'usually refers to '
                                                                           'plasma '
                                                                           'concentration '
                                                                           'falling by half '
                                                                           'during '
                                                                           'elimination.',
                                                                      'D': 'Elimination '
                                                                           'half-life is the '
                                                                           'time for plasma '
                                                                           'concentration to '
                                                                           'decrease by 50% in '
                                                                           'the terminal phase '
                                                                           'under linear '
                                                                           'kinetics, '
                                                                           'reflecting '
                                                                           '0.693·Vd/CL.'}},
                                             {'question': 'Clearance reflects?',
                                              'options': ['A) Volume of plasma cleared of drug '
                                                          'per unit time',
                                                          'B) Fraction unbound in tissues at '
                                                          'steady state',
                                                          'C) Time from dosing to maximum '
                                                          'effect only',
                                                          'D) Tablet surface area available '
                                                          'for dissolution'],
                                              'answer': 'A) Volume of plasma cleared of drug '
                                                        'per unit time',
                                              'explanation': 'Clearance is the theoretical '
                                                             'volume of plasma completely '
                                                             'cleared of drug per unit time '
                                                             'and equals the sum of organ '
                                                             'clearances (notably hepatic and '
                                                             'renal). At steady state, dosing '
                                                             'rate equals clearance times '
                                                             'steady-state concentration. '
                                                             'Maintenance dose design '
                                                             'therefore depends primarily on '
                                                             'clearance and bioavailability.',
                                              'choice_explanations': {'A': 'Clearance is the '
                                                                           'volume of plasma '
                                                                           'completely cleared '
                                                                           'of drug per unit '
                                                                           'time, summing '
                                                                           'organ clearances; '
                                                                           'at steady state, '
                                                                           'dosing rate = CL × '
                                                                           'Css.',
                                                                      'B': 'Fraction unbound '
                                                                           'in tissues relates '
                                                                           'to '
                                                                           'distribution/binding, '
                                                                           'not the clearance '
                                                                           'flow-volume '
                                                                           'metric.',
                                                                      'C': 'Time to maximum '
                                                                           'effect is a PD '
                                                                           'onset parameter '
                                                                           '(ke0/effect '
                                                                           'compartment), not '
                                                                           'clearance.',
                                                                      'D': 'Tablet surface '
                                                                           'area affects '
                                                                           'dissolution rate, '
                                                                           'a biopharmaceutic '
                                                                           'input factor, not '
                                                                           'systemic '
                                                                           'clearance.'}},
                                             {'question': 'Steady state roughly after?',
                                              'options': ['A) One half-life with any '
                                                          'intermittent regimen',
                                                          'B) About 4–5 half-lives with '
                                                          'regular dosing',
                                                          'C) Thirty minutes regardless of '
                                                          'drug half-life',
                                                          'D) Two dosing intervals for every '
                                                          'medicine'],
                                              'answer': 'B) About 4–5 half-lives with regular '
                                                        'dosing',
                                              'explanation': 'With regular fixed dosing and '
                                                             'linear kinetics, plasma '
                                                             'concentrations accumulate until '
                                                             'input equals elimination at '
                                                             'steady state. About 4–5 '
                                                             'elimination half-lives are '
                                                             'required to reach approximately '
                                                             '94–97% of steady-state exposure. '
                                                             'A loading dose can achieve '
                                                             'target concentrations sooner, '
                                                             'but steady-state timing still '
                                                             'follows half-life for subsequent '
                                                             'accumulation.',
                                              'choice_explanations': {'A': 'After one '
                                                                           'half-life with '
                                                                           'intermittent '
                                                                           'dosing, '
                                                                           'accumulation is '
                                                                           'incomplete (~50% '
                                                                           'of eventual '
                                                                           'steady-state '
                                                                           'accumulation for '
                                                                           'linear kinetics), '
                                                                           'not yet near '
                                                                           'steady state.',
                                                                      'B': 'With regular fixed '
                                                                           'dosing and linear '
                                                                           'kinetics, input '
                                                                           'equals elimination '
                                                                           'near steady state '
                                                                           'after about 4–5 '
                                                                           'elimination '
                                                                           'half-lives '
                                                                           '(~94–97% of Css).',
                                                                      'C': 'Thirty minutes is '
                                                                           'arbitrary and '
                                                                           'independent of t½; '
                                                                           'drugs with long '
                                                                           'half-lives take '
                                                                           'days to approach '
                                                                           'Css.',
                                                                      'D': 'Two dosing '
                                                                           'intervals may be '
                                                                           'far shorter or '
                                                                           'longer than 4–5 '
                                                                           'half-lives '
                                                                           'depending on the '
                                                                           'drug; interval '
                                                                           'count alone does '
                                                                           'not define time to '
                                                                           'steady state.'}}],
                                    'medium': [{'question': 'AUC represents?',
                                                'options': ['A) Peak-to-trough fluctuation '
                                                            'ratio only',
                                                            'B) Volume of distribution at '
                                                            'steady state',
                                                            'C) Overall systemic drug exposure',
                                                            'D) Absorption lag time after oral '
                                                            'dosing'],
                                                'answer': 'C) Overall systemic drug exposure',
                                                'explanation': 'Area under the plasma '
                                                               'concentration–time curve (AUC) '
                                                               'integrates concentration over '
                                                               'time and quantifies total '
                                                               'systemic exposure. For linear '
                                                               'kinetics, AUC is proportional '
                                                               'to dose and inversely related '
                                                               'to clearance (AUC = '
                                                               'F·Dose/CL). Bioavailability '
                                                               'and bioequivalence assessments '
                                                               'rely heavily on AUC '
                                                               'comparisons between '
                                                               'formulations.',
                                                'choice_explanations': {'A': 'Peak-to-trough '
                                                                             'fluctuation '
                                                                             'quantifies '
                                                                             'concentration '
                                                                             'swing within a '
                                                                             'dosing interval; '
                                                                             'AUC integrates '
                                                                             'concentration '
                                                                             'over time as '
                                                                             'total exposure.',
                                                                        'B': 'Volume of '
                                                                             'distribution '
                                                                             'relates amount '
                                                                             'in body to '
                                                                             'plasma '
                                                                             'concentration '
                                                                             '(Vd = Amount/C); '
                                                                             'it is not the '
                                                                             'integral AUC.',
                                                                        'C': 'AUC under the '
                                                                             'concentration–time '
                                                                             'curve quantifies '
                                                                             'overall systemic '
                                                                             'exposure; for '
                                                                             'linear kinetics '
                                                                             'AUC = F·Dose/CL.',
                                                                        'D': 'Absorption lag '
                                                                             'time (tlag) is a '
                                                                             'delay before '
                                                                             'absorption '
                                                                             'begins, not the '
                                                                             'exposure '
                                                                             'integral.'}},
                                               {'question': 'Nonlinear PK means?',
                                                'options': ['A) Half-life is identical at all '
                                                            'doses forever',
                                                            'B) Clearance is constant across '
                                                            'the dose range',
                                                            'C) AUC always rises exactly '
                                                            'proportional to dose',
                                                            'D) Parameters change with dose, '
                                                            'e.g. saturation'],
                                                'answer': 'D) Parameters change with dose, '
                                                          'e.g. saturation',
                                                'explanation': 'Nonlinear (dose-dependent) '
                                                               'pharmacokinetics occur when '
                                                               'absorption, distribution, '
                                                               'binding, or elimination '
                                                               'processes saturate within the '
                                                               'clinical dose range. '
                                                               'Michaelis–Menten metabolism of '
                                                               'phenytoin is a classic '
                                                               'example: clearance falls as '
                                                               'concentration rises. '
                                                               'Consequently, steady-state '
                                                               'concentration is no longer '
                                                               'proportional to dose.',
                                                'choice_explanations': {'A': 'Identical '
                                                                             'half-life at all '
                                                                             'doses describes '
                                                                             'linear kinetics; '
                                                                             'nonlinear PK '
                                                                             'features '
                                                                             'dose-dependent '
                                                                             'parameters when '
                                                                             'pathways '
                                                                             'saturate.',
                                                                        'B': 'Constant '
                                                                             'clearance across '
                                                                             'doses is the '
                                                                             'linear '
                                                                             'assumption; '
                                                                             'saturation makes '
                                                                             'clearance '
                                                                             'concentration-dependent.',
                                                                        'C': 'Exact '
                                                                             'proportional '
                                                                             'AUC–dose rise '
                                                                             'defines '
                                                                             'linearity '
                                                                             '(superposition); '
                                                                             'nonlinearity '
                                                                             'breaks that '
                                                                             'proportionality.',
                                                                        'D': 'Nonlinear PK '
                                                                             'means '
                                                                             'absorption, '
                                                                             'binding, or '
                                                                             'elimination '
                                                                             'processes '
                                                                             'saturate so CL, '
                                                                             'F, or Vd change '
                                                                             'with dose—e.g., '
                                                                             'Michaelis–Menten '
                                                                             'elimination.'}},
                                               {'question': 'Protein binding displacement may?',
                                                'options': ['A) Transiently raise free '
                                                            'fraction for highly bound drugs',
                                                            'B) Always double total plasma '
                                                            'concentration permanently',
                                                            'C) Eliminate renal clearance of '
                                                            'unbound drug',
                                                            'D) Convert first-order kinetics '
                                                            'into zero-order always'],
                                                'answer': 'A) Transiently raise free fraction '
                                                          'for highly bound drugs',
                                                'explanation': 'For highly protein-bound '
                                                               'drugs, displacement can '
                                                               'transiently increase unbound '
                                                               'fraction and free '
                                                               'concentration. Increased free '
                                                               'drug is often also more '
                                                               'available for clearance and '
                                                               'distribution, so total '
                                                               'concentration may fall while '
                                                               'free levels partly '
                                                               're-equilibrate. Clinically '
                                                               'important displacement '
                                                               'interactions are therefore '
                                                               'less common than total-level '
                                                               'changes alone might suggest, '
                                                               'but remain relevant for '
                                                               'narrow-index, highly bound '
                                                               'drugs.',
                                                'choice_explanations': {'A': 'For highly bound '
                                                                             'drugs, '
                                                                             'displacement can '
                                                                             'acutely raise '
                                                                             'unbound fraction '
                                                                             'and free '
                                                                             'concentration '
                                                                             'until '
                                                                             'redistribution '
                                                                             'and clearance of '
                                                                             'free drug '
                                                                             're-equilibrate '
                                                                             'totals.',
                                                                        'B': 'Displacement '
                                                                             'does not '
                                                                             'permanently '
                                                                             'double total '
                                                                             'plasma '
                                                                             'concentration; '
                                                                             'total levels '
                                                                             'often fall as '
                                                                             'free drug '
                                                                             'clears, while '
                                                                             'free '
                                                                             'concentration '
                                                                             'changes are '
                                                                             'often transient.',
                                                                        'C': 'Renal clearance '
                                                                             'of unbound drug '
                                                                             'typically '
                                                                             'continues or '
                                                                             'increases with '
                                                                             'higher free '
                                                                             'fraction; '
                                                                             'displacement '
                                                                             'does not '
                                                                             'eliminate '
                                                                             'unbound '
                                                                             'clearance.',
                                                                        'D': 'Protein binding '
                                                                             'displacement '
                                                                             'does not '
                                                                             'inherently '
                                                                             'convert '
                                                                             'first-order to '
                                                                             'zero-order '
                                                                             'elimination; '
                                                                             'zero-order '
                                                                             'requires '
                                                                             'capacity-limited '
                                                                             'pathways near '
                                                                             'Vmax.'}}],
                                    'hard': [{'question': 'Hepatic clearance for high '
                                                          'extraction drugs depends strongly '
                                                          'on?',
                                              'options': ['A) Plasma protein binding as the '
                                                          'sole driver',
                                                          'B) Liver blood flow',
                                                          'C) Fraction unbound in the gut '
                                                          'lumen only',
                                                          'D) Gastric pH at the time of '
                                                          'dosing'],
                                              'answer': 'B) Liver blood flow',
                                              'explanation': 'For high hepatic '
                                                             'extraction-ratio drugs, the '
                                                             'liver removes most drug from '
                                                             'afferent blood in a single pass, '
                                                             'so clearance approximates liver '
                                                             'blood flow. Changes in hepatic '
                                                             'perfusion (heart failure, shock, '
                                                             'vasoactive drugs) therefore '
                                                             'strongly alter clearance of '
                                                             'flow-limited compounds. '
                                                             'Low-extraction drugs are instead '
                                                             'more sensitive to intrinsic '
                                                             'metabolizing capacity and '
                                                             'unbound fraction.',
                                              'choice_explanations': {'A': 'For high '
                                                                           'extraction drugs, '
                                                                           'binding changes '
                                                                           'have limited '
                                                                           'effect on hepatic '
                                                                           'clearance because '
                                                                           'extraction is '
                                                                           'flow-limited, not '
                                                                           'solely '
                                                                           'binding-driven.',
                                                                      'B': 'High hepatic '
                                                                           'extraction-ratio '
                                                                           'drugs are cleared '
                                                                           'nearly completely '
                                                                           'on first pass '
                                                                           'through the liver, '
                                                                           'so hepatic '
                                                                           'clearance '
                                                                           'approximates liver '
                                                                           'blood flow '
                                                                           '(flow-limited '
                                                                           'clearance).',
                                                                      'C': 'Fraction unbound '
                                                                           'in the gut lumen '
                                                                           'affects oral '
                                                                           'absorption, not '
                                                                           'the dominant '
                                                                           'determinant of '
                                                                           'systemic hepatic '
                                                                           'clearance for '
                                                                           'high-extraction IV '
                                                                           'concepts.',
                                                                      'D': 'Gastric pH can '
                                                                           'alter '
                                                                           'dissolution/ionization '
                                                                           'of oral drugs but '
                                                                           'does not set '
                                                                           'hepatic clearance '
                                                                           'of high-extraction '
                                                                           'compounds.'}},
                                             {'question': 'Renal clearance includes?',
                                              'options': ['A) Only glomerular filtration with '
                                                          'no other processes',
                                                          'B) Only tubular secretion without '
                                                          'filtration',
                                                          'C) Filtration minus reabsorption '
                                                          'plus secretion',
                                                          'D) Only hepatic conjugative '
                                                          'metabolism'],
                                              'answer': 'C) Filtration minus reabsorption plus '
                                                        'secretion',
                                              'explanation': 'Renal clearance is the net '
                                                             'result of glomerular filtration '
                                                             'of unbound drug, tubular '
                                                             'secretion into urine, and '
                                                             'tubular reabsorption back into '
                                                             'blood. Thus CLr ≈ (f_u · GFR) + '
                                                             'secretion − reabsorption. '
                                                             'Urinary pH can alter '
                                                             'reabsorption of weak acids and '
                                                             'bases via ion trapping, changing '
                                                             'excretion of some drugs and '
                                                             'toxins.',
                                              'choice_explanations': {'A': 'Glomerular '
                                                                           'filtration is only '
                                                                           'one component; '
                                                                           'secretion and '
                                                                           'reabsorption also '
                                                                           'determine net '
                                                                           'renal clearance.',
                                                                      'B': 'Tubular secretion '
                                                                           'alone omits '
                                                                           'filtration of '
                                                                           'unbound drug and '
                                                                           'passive/active '
                                                                           'reabsorption that '
                                                                           'modify net '
                                                                           'excretion.',
                                                                      'C': 'Renal clearance '
                                                                           'equals filtration '
                                                                           'of unbound drug '
                                                                           'plus tubular '
                                                                           'secretion minus '
                                                                           'tubular '
                                                                           'reabsorption: CLr '
                                                                           '≈ (fu·GFR + '
                                                                           'secretion − '
                                                                           'reabsorption).',
                                                                      'D': 'Hepatic '
                                                                           'conjugative '
                                                                           'metabolism is '
                                                                           'liver '
                                                                           'biotransformation, '
                                                                           'not renal '
                                                                           'excretory '
                                                                           'clearance '
                                                                           'processes.'}},
                                             {'question': 'Two-compartment model early phase '
                                                          'is?',
                                              'options': ['A) Terminal elimination phase only',
                                                          'B) Steady-state infusion plateau '
                                                          'only',
                                                          'C) Zero-order absorption from a '
                                                          'depot',
                                                          'D) Distribution phase after IV '
                                                          'bolus'],
                                              'answer': 'D) Distribution phase after IV bolus',
                                              'explanation': 'In a two-compartment model, drug '
                                                             'first distributes from a central '
                                                             'compartment (blood and rapidly '
                                                             'equilibrating tissues) into a '
                                                             'peripheral compartment. The '
                                                             'early steeper decline on a '
                                                             'semilog plot is this '
                                                             'distribution (α) phase, followed '
                                                             'by a slower terminal elimination '
                                                             '(β) phase. Sampling during '
                                                             'distribution can misrepresent '
                                                             'concentrations intended to '
                                                             'reflect the elimination phase.',
                                              'choice_explanations': {'A': 'The terminal (β) '
                                                                           'phase reflects '
                                                                           'elimination after '
                                                                           'distribution '
                                                                           'equilibrium, not '
                                                                           'the early rapid '
                                                                           'decline.',
                                                                      'B': 'Steady-state '
                                                                           'infusion plateau '
                                                                           'is a '
                                                                           'continuous-input '
                                                                           'condition, not the '
                                                                           'early post-bolus '
                                                                           'distribution '
                                                                           'phase.',
                                                                      'C': 'Zero-order '
                                                                           'absorption from a '
                                                                           'depot is an input '
                                                                           'model; the early '
                                                                           'IV two-compartment '
                                                                           'phase is '
                                                                           'distribution, not '
                                                                           'depot absorption.',
                                                                      'D': 'After IV bolus in '
                                                                           'a two-compartment '
                                                                           'model, the early α '
                                                                           'phase reflects net '
                                                                           'distribution from '
                                                                           'central to '
                                                                           'peripheral tissues '
                                                                           'before the '
                                                                           'terminal '
                                                                           'elimination phase '
                                                                           'dominates.'}}],
                                    'extreme': [{'question': 'TDM for digoxin timing?',
                                                 'options': ['A) Avoid sampling in the '
                                                             'distribution phase; sample at '
                                                             'steady state appropriately',
                                                             'B) Draw levels 5 minutes after '
                                                             'every IV dose always',
                                                             'C) Sample only during the alpha '
                                                             'distribution phase',
                                                             'D) Any random time is equivalent '
                                                             'for interpretation'],
                                                 'answer': 'A) Avoid sampling in the '
                                                           'distribution phase; sample at '
                                                           'steady state appropriately',
                                                 'explanation': 'Digoxin distributes '
                                                                'extensively to tissues, so '
                                                                'plasma levels drawn too soon '
                                                                'after a dose are still '
                                                                'falling through the '
                                                                'distribution phase and do not '
                                                                'reflect the post-distribution '
                                                                'concentration used for '
                                                                'interpretation. Therapeutic '
                                                                'drug monitoring therefore '
                                                                'uses samples at steady state, '
                                                                'typically at least 6–8 hours '
                                                                'after a dose (often a '
                                                                'trough). Mis-timed levels can '
                                                                'prompt inappropriate dose '
                                                                'changes.',
                                                 'choice_explanations': {'A': 'Digoxin '
                                                                              'distributes '
                                                                              'extensively; '
                                                                              'levels drawn in '
                                                                              'the '
                                                                              'distribution '
                                                                              'phase '
                                                                              'overestimate '
                                                                              'the '
                                                                              'post-distribution '
                                                                              'concentration '
                                                                              'linked to '
                                                                              'effect—sample '
                                                                              'after '
                                                                              'distribution, '
                                                                              'ideally at '
                                                                              'steady state '
                                                                              'for maintenance '
                                                                              'assessment.',
                                                                         'B': 'Drawing 5 '
                                                                              'minutes after '
                                                                              'every IV dose '
                                                                              'captures '
                                                                              'distribution-phase '
                                                                              'concentrations '
                                                                              'that do not '
                                                                              'represent '
                                                                              'equilibrated '
                                                                              'tissue-effect '
                                                                              'relationships '
                                                                              'for digoxin.',
                                                                         'C': 'Sampling only '
                                                                              'during α '
                                                                              'distribution '
                                                                              'yields '
                                                                              'misleadingly '
                                                                              'high levels '
                                                                              'unrelated to '
                                                                              'post-distribution '
                                                                              'digoxin '
                                                                              'activity.',
                                                                         'D': 'Random timing '
                                                                              'ignores '
                                                                              'distribution '
                                                                              'and '
                                                                              'accumulation '
                                                                              'state, making '
                                                                              'digoxin level '
                                                                              'interpretation '
                                                                              'scientifically '
                                                                              'invalid.'}},
                                                {'question': 'Bioequivalence typically '
                                                             'compares?',
                                                 'options': ['A) Tablet color and imprint code '
                                                             'only',
                                                             'B) AUC and Cmax within '
                                                             'regulatory limits',
                                                             'C) Melting point and crystal '
                                                             'habit only',
                                                             'D) Taste panel scores for oral '
                                                             'liquids'],
                                                 'answer': 'B) AUC and Cmax within regulatory '
                                                           'limits',
                                                 'explanation': 'Bioequivalence testing '
                                                                'compares rate and extent of '
                                                                'absorption of a test versus '
                                                                'reference product, primarily '
                                                                'through AUC (extent) and Cmax '
                                                                '(rate) metrics. Regulatory '
                                                                'acceptance generally requires '
                                                                'the 90% confidence interval '
                                                                'for key pharmacokinetic '
                                                                'ratios to lie within '
                                                                'predefined limits (commonly '
                                                                '80–125%). Demonstrated '
                                                                'bioequivalence underpins most '
                                                                'generic substitution '
                                                                'decisions.',
                                                 'choice_explanations': {'A': 'Tablet '
                                                                              'color/imprint '
                                                                              'are '
                                                                              'identification '
                                                                              'features, not '
                                                                              'pharmacokinetic '
                                                                              'bioequivalence '
                                                                              'metrics.',
                                                                         'B': 'Bioequivalence '
                                                                              'compares rate '
                                                                              'and extent of '
                                                                              'absorption '
                                                                              'primarily via '
                                                                              'AUC (extent) '
                                                                              'and Cmax (rate) '
                                                                              'within '
                                                                              'predefined '
                                                                              'regulatory '
                                                                              'confidence '
                                                                              'limits versus '
                                                                              'reference.',
                                                                         'C': 'Melting point '
                                                                              'and crystal '
                                                                              'habit are '
                                                                              'solid-state '
                                                                              'properties that '
                                                                              'may affect '
                                                                              'performance but '
                                                                              'are not the '
                                                                              'clinical BE '
                                                                              'endpoints.',
                                                                         'D': 'Taste-panel '
                                                                              'scores assess '
                                                                              'palatability, '
                                                                              'not systemic '
                                                                              'exposure '
                                                                              'equivalence.'}},
                                                {'question': 'Nonlinear binding plus saturable '
                                                             'clearance together can cause?',
                                                 'options': ['A) Strictly proportional '
                                                             'dose–concentration curves only',
                                                             'B) Elimination that is always '
                                                             'first-order forever',
                                                             'C) Complex dose–concentration '
                                                             'relationships',
                                                             'D) Complete absence of '
                                                             'accumulation on chronic dosing'],
                                                 'answer': 'C) Complex dose–concentration '
                                                           'relationships',
                                                 'explanation': 'When both plasma protein '
                                                                'binding and clearance '
                                                                'pathways saturate, free '
                                                                'fraction, total '
                                                                'concentration, and '
                                                                'elimination rate can change '
                                                                'together in a dose-dependent '
                                                                'manner. The resulting '
                                                                'relationship between dose and '
                                                                'exposure becomes markedly '
                                                                'nonlinear and time-dependent. '
                                                                'Such drugs require cautious '
                                                                'titration and often '
                                                                'specialized monitoring rather '
                                                                'than simple proportional dose '
                                                                'adjustments.',
                                                 'choice_explanations': {'A': 'Strict '
                                                                              'dose–concentration '
                                                                              'proportionality '
                                                                              'assumes linear '
                                                                              'binding and '
                                                                              'clearance; dual '
                                                                              'saturation '
                                                                              'breaks '
                                                                              'superposition.',
                                                                         'B': 'Elimination is '
                                                                              'not always '
                                                                              'first-order '
                                                                              'when clearance '
                                                                              'pathways '
                                                                              'saturate at '
                                                                              'clinical '
                                                                              'concentrations.',
                                                                         'C': 'Saturable '
                                                                              'protein binding '
                                                                              'plus saturable '
                                                                              'clearance '
                                                                              'jointly produce '
                                                                              'dose-dependent '
                                                                              'free fraction, '
                                                                              'total levels, '
                                                                              'and clearance, '
                                                                              'yielding '
                                                                              'complex '
                                                                              'nonlinear '
                                                                              'dose–concentration '
                                                                              'relationships.',
                                                                         'D': 'Nonlinear '
                                                                              'clearance often '
                                                                              'increases '
                                                                              'accumulation at '
                                                                              'higher doses '
                                                                              'rather than '
                                                                              'abolishing '
                                                                              'chronic '
                                                                              'accumulation.'}}]},
                      'cases': {'easy': [{'title': 'Why Wait for Steady State?',
                                          'stem': 'Team wants a level 2 hours after first '
                                                  "gentamicin dose as 'trough steady state'.",
                                          'question': 'Teaching point?',
                                          'answer': 'Steady state needs multiple half-lives '
                                                    'unless loading used; interpret timing '
                                                    'correctly.',
                                          'discussion': 'Wrong timing misleads TDM.',
                                          'book_hint': 'Applied Biopharmaceutics & '
                                                       'Pharmacokinetics — Shargel'}],
                                'medium': [{'title': 'Phenytoin Dose Doubled',
                                            'stem': 'Phenytoin dose doubled because level was '
                                                    'slightly low; patient becomes toxic.',
                                            'question': 'Why?',
                                            'answer': 'Saturable metabolism — small dose hikes '
                                                      'can cause large level jumps.',
                                            'discussion': 'Titrate carefully.',
                                            'book_hint': 'Applied Biopharmaceutics & '
                                                         'Pharmacokinetics — Shargel'}],
                                'hard': [{'title': 'Aminoglycoside Once-Daily',
                                          'stem': 'Protocol uses extended-interval '
                                                  'aminoglycoside dosing. Choose the safest '
                                                  'high-yield next concept before definitive '
                                                  'results.',
                                          'question': 'PK/PD rationale theme?',
                                          'answer': 'Concentration-dependent killing + '
                                                    'adaptive resistance considerations; '
                                                    'monitor levels/renal function per '
                                                    'protocol.',
                                          'discussion': 'Not the same as old multiple-daily '
                                                        'empiric habits.',
                                          'book_hint': 'Applied Biopharmaceutics & '
                                                       'Pharmacokinetics — Shargel'}],
                                'extreme': [{'title': 'Transplant Tacrolimus Interaction',
                                             'stem': 'Tacrolimus levels soar after starting a '
                                                     'strong CYP3A4/P-gp inhibitor. Avoid '
                                                     'harmful premature treatment while '
                                                     'catastrophic differentials remain open.',
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
                                                 'options': ['A) Structure–activity '
                                                             'relationship',
                                                             'B) Systemic absorption rate',
                                                             'C) Sustained-action release',
                                                             'D) Secondary amine '
                                                             'rearrangement'],
                                                 'answer': 'A) Structure–activity relationship',
                                                 'explanation': 'Structure–activity '
                                                                'relationships (SAR) describe '
                                                                'how systematic changes in a '
                                                                "molecule's functional groups, "
                                                                'scaffold, or stereochemistry '
                                                                'alter biological potency, '
                                                                'selectivity, or toxicity. SAR '
                                                                'analysis links chemical '
                                                                'features to target binding '
                                                                'and disposition. Medicinal '
                                                                'chemists use SAR to optimize '
                                                                'lead compounds toward '
                                                                'drug-like profiles.',
                                                 'choice_explanations': {'A': 'Structure–activity '
                                                                              'relationships '
                                                                              '(SAR) map how '
                                                                              'changes in '
                                                                              'functional '
                                                                              'groups, '
                                                                              'scaffold, or '
                                                                              'stereochemistry '
                                                                              'alter potency, '
                                                                              'selectivity, '
                                                                              'and ADME at the '
                                                                              'molecular '
                                                                              'target.',
                                                                         'B': 'Systemic '
                                                                              'absorption rate '
                                                                              'is a '
                                                                              'pharmacokinetic '
                                                                              'absorption '
                                                                              'parameter (Ka), '
                                                                              'not the '
                                                                              'medicinal '
                                                                              'chemistry '
                                                                              'acronym SAR.',
                                                                         'C': 'Sustained-action '
                                                                              'release '
                                                                              'describes '
                                                                              'formulation-controlled '
                                                                              'delivery, not '
                                                                              'structure–activity '
                                                                              'analysis of '
                                                                              'chemical '
                                                                              'series.',
                                                                         'D': 'Secondary amine '
                                                                              'rearrangement '
                                                                              'is a specific '
                                                                              'chemical '
                                                                              'reaction class, '
                                                                              'not the meaning '
                                                                              'of SAR in drug '
                                                                              'design.'}},
                                                {'question': 'Prodrug is?',
                                                 'options': ['A) Already active drug given at '
                                                             'higher dose',
                                                             'B) Inactive form converted in '
                                                             'vivo to active drug',
                                                             'C) Active metabolite formed '
                                                             'after therapeutic failure',
                                                             'D) Excipient that enhances '
                                                             'tablet hardness'],
                                                 'answer': 'B) Inactive form converted in vivo '
                                                           'to active drug',
                                                 'explanation': 'A prodrug is a '
                                                                'pharmacologically inactive or '
                                                                'less active derivative that '
                                                                'undergoes in vivo '
                                                                'biotransformation to release '
                                                                'the active parent drug. '
                                                                'Common goals include '
                                                                'improving solubility, '
                                                                'permeability, stability, or '
                                                                'targeted activation. Ester '
                                                                'and phosphate prodrugs, for '
                                                                'example, are cleaved by '
                                                                'hydrolases after absorption '
                                                                'or at the site of action.',
                                                 'choice_explanations': {'A': 'An already '
                                                                              'active drug '
                                                                              'given at higher '
                                                                              'dose is simply '
                                                                              'dose escalation '
                                                                              'of the active '
                                                                              'species, not a '
                                                                              'prodrug '
                                                                              'strategy.',
                                                                         'B': 'A prodrug is an '
                                                                              'inactive or '
                                                                              'less active '
                                                                              'derivative that '
                                                                              'undergoes in '
                                                                              'vivo '
                                                                              'biotransformation '
                                                                              '(e.g., '
                                                                              'hydrolysis, '
                                                                              'reduction) to '
                                                                              'release the '
                                                                              'active parent, '
                                                                              'often to '
                                                                              'improve '
                                                                              'solubility, '
                                                                              'permeability, '
                                                                              'or targeting.',
                                                                         'C': 'An active '
                                                                              'metabolite '
                                                                              'after '
                                                                              'therapeutic '
                                                                              'failure is a '
                                                                              'metabolic '
                                                                              'product, not '
                                                                              'the intentional '
                                                                              'inactive-to-active '
                                                                              'design of a '
                                                                              'prodrug.',
                                                                         'D': 'Excipients that '
                                                                              'harden tablets '
                                                                              'are formulation '
                                                                              'aids, not '
                                                                              'covalently '
                                                                              'modified latent '
                                                                              'drug forms.'}},
                                                {'question': 'pKa helps predict?',
                                                 'options': ['A) Crystal lattice energy of '
                                                             'polymorphs only',
                                                             'B) Tablet friability under '
                                                             'shipping stress',
                                                             'C) Ionization state at a given '
                                                             'pH',
                                                             'D) Exact hepatic blood flow in '
                                                             'adults'],
                                                 'answer': 'C) Ionization state at a given pH',
                                                 'explanation': 'The pKa of an ionizable group '
                                                                'determines the equilibrium '
                                                                'between protonated and '
                                                                'deprotonated forms at a given '
                                                                'pH via the '
                                                                'Henderson–Hasselbalch '
                                                                'relationship. Ionization '
                                                                'state strongly influences '
                                                                'aqueous solubility, membrane '
                                                                'permeation, and receptor '
                                                                'recognition. Predicting '
                                                                'charged versus uncharged '
                                                                'fractions at physiologic pH '
                                                                'is therefore central to '
                                                                'absorption design.',
                                                 'choice_explanations': {'A': 'Crystal lattice '
                                                                              'energy of '
                                                                              'polymorphs '
                                                                              'relates to '
                                                                              'solid-state '
                                                                              'packing and '
                                                                              'melting/solubility '
                                                                              'of crystals, '
                                                                              'not directly to '
                                                                              'solution '
                                                                              'ionization '
                                                                              'equilibria.',
                                                                         'B': 'Tablet '
                                                                              'friability is a '
                                                                              'mechanical '
                                                                              'strength test '
                                                                              'of compacts, '
                                                                              'unrelated to '
                                                                              'acid–base pKa.',
                                                                         'C': 'pKa of an '
                                                                              'ionizable '
                                                                              'group, via '
                                                                              'Henderson–Hasselbalch, '
                                                                              'predicts the '
                                                                              'ionized versus '
                                                                              'unionized '
                                                                              'fraction at a '
                                                                              'given pH, '
                                                                              'governing '
                                                                              'solubility, '
                                                                              'permeation, and '
                                                                              'binding.',
                                                                         'D': 'Hepatic blood '
                                                                              'flow is a '
                                                                              'physiologic '
                                                                              'clearance '
                                                                              'determinant, '
                                                                              'not predicted '
                                                                              "by a molecule's "
                                                                              'pKa.'}}],
                                       'medium': [{'question': 'Beta-lactam ring is essential '
                                                               'for?',
                                                   'options': ['A) Macrolide ribosomal binding '
                                                               'affinity',
                                                               'B) Aminoglycoside ototoxicity '
                                                               'risk only',
                                                               'C) Tetracycline chelation with '
                                                               'divalent metals',
                                                               'D) Antibacterial action of '
                                                               'many '
                                                               'penicillins/cephalosporins'],
                                                   'answer': 'D) Antibacterial action of many '
                                                             'penicillins/cephalosporins',
                                                   'explanation': 'The strained β-lactam ring '
                                                                  'acylates serine residues in '
                                                                  'bacterial '
                                                                  'penicillin-binding '
                                                                  'proteins, irreversibly '
                                                                  'inhibiting cell-wall '
                                                                  'transpeptidation. Ring '
                                                                  'integrity is therefore '
                                                                  'essential for antibacterial '
                                                                  'activity of penicillins and '
                                                                  'cephalosporins. β-Lactamase '
                                                                  'enzymes hydrolyze the amide '
                                                                  'bond of the ring, '
                                                                  'conferring resistance '
                                                                  'unless a β-lactamase '
                                                                  'inhibitor or stable analog '
                                                                  'is used.',
                                                   'choice_explanations': {'A': 'Macrolides '
                                                                                'bind the 50S '
                                                                                'ribosomal '
                                                                                'tunnel; their '
                                                                                'activity does '
                                                                                'not depend on '
                                                                                'a β-lactam '
                                                                                'ring.',
                                                                           'B': 'Aminoglycoside '
                                                                                'ototoxicity '
                                                                                'relates to '
                                                                                'irreversible '
                                                                                'hair-cell '
                                                                                'injury, not '
                                                                                'β-lactam ring '
                                                                                'chemistry.',
                                                                           'C': 'Tetracycline–metal '
                                                                                'chelation '
                                                                                'involves the '
                                                                                'polycarbonyl '
                                                                                'enol system, '
                                                                                'not a '
                                                                                'β-lactam '
                                                                                'warhead.',
                                                                           'D': 'The strained '
                                                                                'β-lactam ring '
                                                                                'acylates PBP '
                                                                                'active-site '
                                                                                'serines, '
                                                                                'irreversibly '
                                                                                'inhibiting '
                                                                                'peptidoglycan '
                                                                                'cross-linking—the '
                                                                                'core '
                                                                                'antibacterial '
                                                                                'mechanism of '
                                                                                'penicillins/cephalosporins.'}},
                                                  {'question': 'Chirality matters because?',
                                                   'options': ['A) Enantiomers can differ in '
                                                               'activity and toxicity',
                                                               'B) All enantiomers always have '
                                                               'identical ADME',
                                                               'C) Racemates cannot be '
                                                               'formulated as tablets',
                                                               'D) Optical rotation predicts '
                                                               'aqueous solubility alone'],
                                                   'answer': 'A) Enantiomers can differ in '
                                                             'activity and toxicity',
                                                   'explanation': 'Enantiomers are '
                                                                  'nonsuperimposable '
                                                                  'mirror-image stereoisomers '
                                                                  'that can interact '
                                                                  'differently with chiral '
                                                                  'biological targets such as '
                                                                  'receptors and enzymes. One '
                                                                  'enantiomer may provide most '
                                                                  'therapeutic activity while '
                                                                  'the other contributes '
                                                                  'little efficacy or distinct '
                                                                  'toxicity. Stereoselective '
                                                                  'metabolism and transport '
                                                                  'further differentiate '
                                                                  'clinical pharmacokinetics '
                                                                  'of many chiral drugs.',
                                                   'choice_explanations': {'A': 'Biological '
                                                                                'targets are '
                                                                                'chiral; '
                                                                                'enantiomers '
                                                                                'can show '
                                                                                'large '
                                                                                'differences '
                                                                                'in receptor '
                                                                                'affinity, '
                                                                                'metabolism '
                                                                                '(e.g., CYP '
                                                                                'stereoselectivity), '
                                                                                'and toxicity.',
                                                                           'B': 'Enantiomers '
                                                                                'frequently '
                                                                                'differ in '
                                                                                'ADME because '
                                                                                'enzymes and '
                                                                                'transporters '
                                                                                'are '
                                                                                'stereoselective; '
                                                                                'identical '
                                                                                'ADME is not '
                                                                                'generally '
                                                                                'true.',
                                                                           'C': 'Racemates are '
                                                                                'routinely '
                                                                                'formulated as '
                                                                                'tablets; '
                                                                                'chirality '
                                                                                'does not '
                                                                                'preclude '
                                                                                'solid oral '
                                                                                'dosage forms.',
                                                                           'D': 'Optical '
                                                                                'rotation '
                                                                                'measures '
                                                                                'chiral '
                                                                                'purity/identity '
                                                                                'in solution; '
                                                                                'it does not '
                                                                                'by itself '
                                                                                'predict '
                                                                                'aqueous '
                                                                                'solubility.'}},
                                                  {'question': 'Bioisostere replacement aims '
                                                               'to?',
                                                   'options': ['A) Destroy target binding to '
                                                               'reduce potency',
                                                               'B) Retain activity while '
                                                               'improving drug-like properties',
                                                               'C) Convert every drug into a '
                                                               'quaternary ammonium salt',
                                                               'D) Eliminate the need for any '
                                                               'metabolic soft spots'],
                                                   'answer': 'B) Retain activity while '
                                                             'improving drug-like properties',
                                                   'explanation': 'Bioisosteric replacement '
                                                                  'substitutes an atom or '
                                                                  'group with another of '
                                                                  'similar steric and '
                                                                  'electronic character to '
                                                                  'retain target affinity '
                                                                  'while modulating ADME or '
                                                                  'toxicity. Classic examples '
                                                                  'include replacing hydrogen '
                                                                  'with fluorine or a '
                                                                  'carboxylic acid with a '
                                                                  'tetrazole. The tactic is '
                                                                  'used to improve potency, '
                                                                  'selectivity, metabolic '
                                                                  'stability, or '
                                                                  'physicochemical properties.',
                                                   'choice_explanations': {'A': 'Destroying '
                                                                                'target '
                                                                                'binding would '
                                                                                'reduce '
                                                                                'potency; '
                                                                                'bioisosteres '
                                                                                'aim to '
                                                                                'preserve key '
                                                                                'interactions '
                                                                                'while tuning '
                                                                                'properties.',
                                                                           'B': 'Bioisosteric '
                                                                                'replacement '
                                                                                'swaps '
                                                                                'atoms/groups '
                                                                                'of similar '
                                                                                'steric/electronic '
                                                                                'character to '
                                                                                'retain '
                                                                                'activity '
                                                                                'while '
                                                                                'improving '
                                                                                'solubility, '
                                                                                'metabolic '
                                                                                'stability, '
                                                                                'selectivity, '
                                                                                'or safety.',
                                                                           'C': 'Converting '
                                                                                'every drug to '
                                                                                'a quaternary '
                                                                                'ammonium salt '
                                                                                'permanently '
                                                                                'ionizes the '
                                                                                'molecule and '
                                                                                'is not the '
                                                                                'general '
                                                                                'bioisostere '
                                                                                'goal.',
                                                                           'D': 'Soft '
                                                                                'metabolic '
                                                                                'spots may be '
                                                                                'modulated by '
                                                                                'bioisosteres, '
                                                                                'but '
                                                                                'eliminating '
                                                                                'all '
                                                                                'metabolism is '
                                                                                'neither '
                                                                                'necessary nor '
                                                                                'always '
                                                                                'desirable.'}}],
                                       'hard': [{'question': 'Log D differs from log P by?',
                                                 'options': ['A) Ignoring lipophilicity '
                                                             'entirely',
                                                             'B) Using only melting point as '
                                                             'the input',
                                                             'C) Accounting for ionization at '
                                                             'a specified pH',
                                                             'D) Measuring only solid-state '
                                                             'polymorphism'],
                                                 'answer': 'C) Accounting for ionization at a '
                                                           'specified pH',
                                                 'explanation': 'Log P describes partitioning '
                                                                'of the purely unionized '
                                                                'species, whereas log D is the '
                                                                'pH-dependent distribution '
                                                                'coefficient including all '
                                                                'ionized and unionized forms '
                                                                'present at that pH. At '
                                                                'physiologic pH, ionized '
                                                                'fractions often dominate for '
                                                                'acids and bases, so log D is '
                                                                'frequently more relevant to '
                                                                'membrane permeation. '
                                                                'Comparing log D across pH '
                                                                'values maps '
                                                                'ionization-sensitive '
                                                                'lipophilicity.',
                                                 'choice_explanations': {'A': 'Log D still '
                                                                              'reports '
                                                                              'lipophilicity/distribution '
                                                                              'behavior; it '
                                                                              'does not ignore '
                                                                              'lipophilicity—it '
                                                                              'incorporates '
                                                                              'ionization '
                                                                              'effects on '
                                                                              'apparent '
                                                                              'partitioning.',
                                                                         'B': 'Melting point '
                                                                              'is a '
                                                                              'solid-state '
                                                                              'thermal '
                                                                              'property; log D '
                                                                              'is measured as '
                                                                              'a '
                                                                              'partitioning/distribution '
                                                                              'coefficient in '
                                                                              'biphasic '
                                                                              'systems.',
                                                                         'C': 'Log D is the '
                                                                              'pH-dependent '
                                                                              'distribution '
                                                                              'coefficient '
                                                                              'including '
                                                                              'ionized and '
                                                                              'unionized '
                                                                              'species at a '
                                                                              'stated pH, '
                                                                              'whereas log P '
                                                                              'refers to the '
                                                                              'purely '
                                                                              'unionized form.',
                                                                         'D': 'Solid-state '
                                                                              'polymorphism '
                                                                              'concerns '
                                                                              'crystal forms; '
                                                                              'log D is a '
                                                                              'solution '
                                                                              'partitioning '
                                                                              'parameter at '
                                                                              'defined pH.'}},
                                                {'question': 'Suicide substrate / '
                                                             'mechanism-based inhibitor?',
                                                 'options': ['A) Binds reversibly without '
                                                             'chemical activation by the '
                                                             'enzyme',
                                                             'B) Competes only at an '
                                                             'allosteric site with no turnover',
                                                             'C) Induces CYP expression '
                                                             'without engaging the target '
                                                             'enzyme',
                                                             'D) Requires enzyme activation '
                                                             'then inactivates the enzyme'],
                                                 'answer': 'D) Requires enzyme activation then '
                                                           'inactivates the enzyme',
                                                 'explanation': 'A mechanism-based (suicide) '
                                                                'inhibitor is chemically '
                                                                'transformed by the target '
                                                                'enzyme into a reactive '
                                                                'species that then covalently '
                                                                'inactivates that enzyme. '
                                                                'Catalytic turnover is '
                                                                'therefore required before '
                                                                'irreversible inhibition '
                                                                'occurs. This distinguishes '
                                                                'suicide substrates from '
                                                                'simple reversible competitive '
                                                                'inhibitors that need no '
                                                                'enzymatic activation.',
                                                 'choice_explanations': {'A': 'Reversible '
                                                                              'binding without '
                                                                              'catalytic '
                                                                              'activation '
                                                                              'describes '
                                                                              'classical '
                                                                              'competitive/reversible '
                                                                              'inhibitors, not '
                                                                              'mechanism-based '
                                                                              'inactivation.',
                                                                         'B': 'Pure allosteric '
                                                                              'competition '
                                                                              'without '
                                                                              'turnover lacks '
                                                                              'the catalytic '
                                                                              'activation step '
                                                                              'that generates '
                                                                              'the reactive '
                                                                              'species in '
                                                                              'suicide '
                                                                              'inhibition.',
                                                                         'C': 'CYP induction '
                                                                              'increases '
                                                                              'enzyme '
                                                                              'expression via '
                                                                              'nuclear '
                                                                              'receptors; it '
                                                                              'is not '
                                                                              'mechanism-based '
                                                                              'covalent '
                                                                              'inactivation of '
                                                                              'the catalytic '
                                                                              'enzyme.',
                                                                         'D': 'A '
                                                                              'suicide/mechanism-based '
                                                                              'inhibitor is '
                                                                              'turned over by '
                                                                              'the target '
                                                                              'enzyme to a '
                                                                              'reactive '
                                                                              'intermediate '
                                                                              'that covalently '
                                                                              'inactivates '
                                                                              'that same '
                                                                              'enzyme, '
                                                                              'requiring '
                                                                              'catalytic '
                                                                              'activation.'}},
                                                {'question': 'Hansch analysis relates?',
                                                 'options': ['A) Physicochemical parameters to '
                                                             'biological activity',
                                                             'B) Tablet punch speed to content '
                                                             'uniformity only',
                                                             'C) NMR chemical shifts to '
                                                             'film-coat color only',
                                                             'D) Sterility assurance to '
                                                             'autoclave load size only'],
                                                 'answer': 'A) Physicochemical parameters to '
                                                           'biological activity',
                                                 'explanation': 'Hansch analysis is an early '
                                                                'quantitative '
                                                                'structure–activity '
                                                                'relationship (QSAR) approach '
                                                                'correlating biological '
                                                                'activity with physicochemical '
                                                                'descriptors such as '
                                                                'hydrophobic (π), electronic '
                                                                '(σ), and steric terms. '
                                                                'Regression models relate '
                                                                'these parameters to potency '
                                                                'across a congeneric series. '
                                                                'It provided a foundation for '
                                                                'modern computational QSAR and '
                                                                'property-based optimization.',
                                                 'choice_explanations': {'A': 'Hansch analysis '
                                                                              'correlates '
                                                                              'biological '
                                                                              'activity with '
                                                                              'physicochemical '
                                                                              'descriptors '
                                                                              '(e.g., log P, '
                                                                              'σ, steric '
                                                                              'parameters) in '
                                                                              'early QSAR '
                                                                              'models.',
                                                                         'B': 'Tablet punch '
                                                                              'speed versus '
                                                                              'content '
                                                                              'uniformity is a '
                                                                              'process '
                                                                              'pharmaceutical '
                                                                              'engineering '
                                                                              'relationship, '
                                                                              'not Hansch '
                                                                              'QSAR.',
                                                                         'C': 'NMR shifts '
                                                                              'versus '
                                                                              'film-coat color '
                                                                              'mixes '
                                                                              'analytical '
                                                                              'spectroscopy '
                                                                              'with '
                                                                              'formulation '
                                                                              'aesthetics, '
                                                                              'unrelated to '
                                                                              'Hansch '
                                                                              'analysis.',
                                                                         'D': 'Sterility '
                                                                              'assurance '
                                                                              'versus '
                                                                              'autoclave load '
                                                                              'is a '
                                                                              'sterilization '
                                                                              'validation '
                                                                              'topic, not '
                                                                              'physicochemical '
                                                                              'QSAR.'}}],
                                       'extreme': [{'question': 'Hard drug vs soft drug '
                                                                'concepts?',
                                                    'options': ['A) Hard drugs always lack any '
                                                                'metabolic pathway forever',
                                                                'B) Soft drugs are designed '
                                                                'for predictable metabolism to '
                                                                'inactive metabolites',
                                                                'C) Soft drugs cannot be given '
                                                                'orally under any circumstance',
                                                                'D) Hard drugs are defined '
                                                                'only by tablet crushing '
                                                                'strength'],
                                                    'answer': 'B) Soft drugs are designed for '
                                                              'predictable metabolism to '
                                                              'inactive metabolites',
                                                    'explanation': 'Soft drugs are active '
                                                                   'compounds deliberately '
                                                                   'designed to undergo rapid, '
                                                                   'predictable metabolism to '
                                                                   'inactive metabolites after '
                                                                   'exerting their effect, '
                                                                   'limiting systemic burden. '
                                                                   'Hard drugs, in contrast, '
                                                                   'are structurally resistant '
                                                                   'to metabolism or yield '
                                                                   'metabolites that remain '
                                                                   'active. Soft-drug design '
                                                                   'is a metabolism-based '
                                                                   'strategy to widen safety '
                                                                   'margins and control '
                                                                   'duration of action.',
                                                    'choice_explanations': {'A': 'Hard drugs '
                                                                                 'are '
                                                                                 'metabolically '
                                                                                 'resistant '
                                                                                 'relative to '
                                                                                 'soft drugs '
                                                                                 'but are not '
                                                                                 'defined as '
                                                                                 'having '
                                                                                 'literally no '
                                                                                 'metabolic '
                                                                                 'pathway '
                                                                                 'forever.',
                                                                            'B': 'Soft drugs '
                                                                                 'are '
                                                                                 'intentionally '
                                                                                 'designed for '
                                                                                 'rapid, '
                                                                                 'predictable '
                                                                                 'metabolism '
                                                                                 'to inactive '
                                                                                 'metabolites '
                                                                                 'after the '
                                                                                 'therapeutic '
                                                                                 'effect, '
                                                                                 'limiting '
                                                                                 'systemic '
                                                                                 'burden and '
                                                                                 'long-lived '
                                                                                 'metabolites.',
                                                                            'C': 'Soft drugs '
                                                                                 'can be '
                                                                                 'administered '
                                                                                 'by various '
                                                                                 'routes '
                                                                                 'including '
                                                                                 'oral when '
                                                                                 'the design '
                                                                                 'permits; '
                                                                                 'oral '
                                                                                 'exclusion is '
                                                                                 'not '
                                                                                 'definitional.',
                                                                            'D': 'Tablet '
                                                                                 'crushing '
                                                                                 'strength is '
                                                                                 'a mechanical '
                                                                                 'test and '
                                                                                 'does not '
                                                                                 'define '
                                                                                 'hard-drug '
                                                                                 'metabolic '
                                                                                 'concepts.'}},
                                                   {'question': 'Covalent warheads in targeted '
                                                                'covalent inhibitors need?',
                                                    'options': ['A) Random reactivity with '
                                                                'every nucleophile in plasma',
                                                                'B) Complete avoidance of any '
                                                                'electrophile forever',
                                                                'C) Careful selectivity to '
                                                                'limit off-target binding',
                                                                'D) Mandatory permanent '
                                                                'binding to albumin only'],
                                                    'answer': 'C) Careful selectivity to limit '
                                                              'off-target binding',
                                                    'explanation': 'Targeted covalent '
                                                                   'inhibitors use an '
                                                                   'electrophilic warhead to '
                                                                   'form a bond with a '
                                                                   'nucleophilic residue '
                                                                   '(often cysteine) near the '
                                                                   'binding site after '
                                                                   'reversible recognition. '
                                                                   'Selectivity depends on '
                                                                   'both noncovalent binding '
                                                                   'complementarity and '
                                                                   'warhead reactivity matched '
                                                                   'to the intended residue. '
                                                                   'Excessive reactivity '
                                                                   'increases off-target '
                                                                   'covalent modification and '
                                                                   'toxicity risk.',
                                                    'choice_explanations': {'A': 'Random high '
                                                                                 'reactivity '
                                                                                 'with plasma '
                                                                                 'nucleophiles '
                                                                                 'causes '
                                                                                 'off-target '
                                                                                 'covalent '
                                                                                 'adducts and '
                                                                                 'toxicity; '
                                                                                 'warheads '
                                                                                 'must be '
                                                                                 'tempered for '
                                                                                 'selective '
                                                                                 'engagement.',
                                                                            'B': 'Targeted '
                                                                                 'covalent '
                                                                                 'inhibitors '
                                                                                 'require a '
                                                                                 'controlled '
                                                                                 'electrophile; '
                                                                                 'complete '
                                                                                 'avoidance of '
                                                                                 'any '
                                                                                 'electrophile '
                                                                                 'precludes '
                                                                                 'the covalent '
                                                                                 'mechanism.',
                                                                            'C': 'After '
                                                                                 'reversible '
                                                                                 'recognition '
                                                                                 'of the '
                                                                                 'target '
                                                                                 'pocket, the '
                                                                                 'warhead '
                                                                                 'should react '
                                                                                 'selectively '
                                                                                 'with a '
                                                                                 'proximal '
                                                                                 'nucleophile '
                                                                                 '(often Cys) '
                                                                                 'while '
                                                                                 'minimizing '
                                                                                 'indiscriminate '
                                                                                 'off-target '
                                                                                 'covalent '
                                                                                 'binding.',
                                                                            'D': 'Mandatory '
                                                                                 'permanent '
                                                                                 'albumin '
                                                                                 'binding '
                                                                                 'would '
                                                                                 'sequester '
                                                                                 'drug '
                                                                                 'nonspecifically '
                                                                                 'and is not '
                                                                                 'the design '
                                                                                 'goal of '
                                                                                 'selective '
                                                                                 'target '
                                                                                 'covalent '
                                                                                 'inhibition.'}},
                                                   {'question': 'PROTACs act by?',
                                                    'options': ['A) Competitively blocking '
                                                                'only orthosteric agonists',
                                                                'B) Irreversibly alkylating '
                                                                'DNA in all cells',
                                                                'C) Inhibiting only '
                                                                'extracellular ligand '
                                                                'diffusion',
                                                                'D) Hijacking degradation '
                                                                'machinery to degrade target '
                                                                'proteins'],
                                                    'answer': 'D) Hijacking degradation '
                                                              'machinery to degrade target '
                                                              'proteins',
                                                    'explanation': 'Proteolysis-targeting '
                                                                   'chimeras (PROTACs) are '
                                                                   'bifunctional molecules '
                                                                   'that simultaneously bind a '
                                                                   'target protein and an E3 '
                                                                   'ubiquitin ligase. Induced '
                                                                   'proximity leads to '
                                                                   'ubiquitination and '
                                                                   'proteasomal degradation of '
                                                                   'the target rather than '
                                                                   'simple occupancy-based '
                                                                   'inhibition. Because '
                                                                   'degradation can be '
                                                                   'catalytic, PROTACs '
                                                                   'represent an event-driven '
                                                                   'pharmacology modality.',
                                                    'choice_explanations': {'A': 'Competitive '
                                                                                 'orthosteric '
                                                                                 'blockade is '
                                                                                 'classical '
                                                                                 'occupancy '
                                                                                 'pharmacology; '
                                                                                 'PROTACs '
                                                                                 'instead '
                                                                                 'induce '
                                                                                 'proximity '
                                                                                 'for '
                                                                                 'ubiquitination '
                                                                                 'and '
                                                                                 'degradation.',
                                                                            'B': 'Irreversible '
                                                                                 'DNA '
                                                                                 'alkylation '
                                                                                 'in all cells '
                                                                                 'describes '
                                                                                 'nonspecific '
                                                                                 'cytotoxic '
                                                                                 'alkylators, '
                                                                                 'not '
                                                                                 'bifunctional '
                                                                                 'degrader '
                                                                                 'pharmacology.',
                                                                            'C': 'Inhibiting '
                                                                                 'extracellular '
                                                                                 'ligand '
                                                                                 'diffusion is '
                                                                                 'not PROTAC '
                                                                                 'action; '
                                                                                 'PROTACs act '
                                                                                 'inside cells '
                                                                                 'on protein '
                                                                                 'targets via '
                                                                                 'the UPS.',
                                                                            'D': 'PROTACs bind '
                                                                                 'a target '
                                                                                 'protein and '
                                                                                 'an E3 ligase '
                                                                                 'simultaneously, '
                                                                                 'inducing '
                                                                                 'ubiquitination '
                                                                                 'and '
                                                                                 'proteasomal '
                                                                                 'degradation '
                                                                                 'of the '
                                                                                 'target '
                                                                                 'rather than '
                                                                                 'mere '
                                                                                 'occupancy '
                                                                                 'inhibition.'}}]},
                         'cases': {'easy': [{'title': 'Why Make a Prodrug?',
                                             'stem': 'A poorly soluble drug is redesigned as '
                                                     'an ester prodrug.',
                                             'question': 'Goal theme?',
                                             'answer': 'Improve absorption/stability then '
                                                       'release active drug.',
                                             'discussion': 'Metabolic activation required.',
                                             'book_hint': "Foye's Principles of Medicinal "
                                                          'Chemistry'}],
                                   'medium': [{'title': 'Single Enantiomer Switch',
                                               'stem': 'A racemic drug is replaced by a single '
                                                       'active enantiomer product.',
                                               'question': 'Rationale?',
                                               'answer': 'Potentially more '
                                                         'selective/predictable response.',
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
                                                        'unexpected organ toxicity. Avoid '
                                                        'harmful premature treatment while '
                                                        'catastrophic differentials remain '
                                                        'open.',
                                                'question': 'Medchem concept?',
                                                'answer': 'Off-target covalent binding — '
                                                          'redesign warhead/selectivity and '
                                                          'reassess safety.',
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
                                           'options': ['A) Only synthetic industrial dye '
                                                       'chemistry',
                                                       'B) Only hospital IV pump programming',
                                                       'C) Only clinical trial statistics '
                                                       'methods',
                                                       'D) Medicines derived from natural '
                                                       'sources'],
                                           'answer': 'D) Medicines derived from natural '
                                                     'sources',
                                           'explanation': 'Pharmacognosy is the pharmaceutical '
                                                          'science concerned with medicines '
                                                          'derived from natural sources, '
                                                          'including plants, microbes, fungi, '
                                                          'and marine organisms. It covers '
                                                          'identification, chemistry, '
                                                          'biosynthesis, quality, and '
                                                          'biological activity of natural '
                                                          'products. Many modern drugs '
                                                          'originated as purified or '
                                                          'semi-synthetic natural compounds.',
                                           'choice_explanations': {'A': 'Synthetic industrial '
                                                                        'dye chemistry is '
                                                                        'organic/industrial '
                                                                        'chemistry, not the '
                                                                        'study of medicines '
                                                                        'from natural sources.',
                                                                   'B': 'Hospital IV pump '
                                                                        'programming is '
                                                                        'clinical/device '
                                                                        'practice, outside '
                                                                        "pharmacognosy's "
                                                                        'natural-product '
                                                                        'medicine scope.',
                                                                   'C': 'Clinical trial '
                                                                        'statistics is '
                                                                        'biostatistics/methodology, '
                                                                        'not pharmacognosy.',
                                                                   'D': 'Pharmacognosy studies '
                                                                        'medicines derived '
                                                                        'from natural '
                                                                        'sources—plants, '
                                                                        'microbes, fungi, '
                                                                        'marine '
                                                                        'organisms—including '
                                                                        'identification, '
                                                                        'chemistry, and '
                                                                        'quality of crude '
                                                                        'drugs.'}},
                                          {'question': 'Digitalis historically relates to?',
                                           'options': ['A) Cardiac glycosides from foxglove',
                                                       'B) Opioid alkaloids from poppy latex',
                                                       'C) Antimalarial quinine from cinchona '
                                                       'only',
                                                       'D) Local anesthetic cocaine from coca '
                                                       'leaf only'],
                                           'answer': 'A) Cardiac glycosides from foxglove',
                                           'explanation': 'Digitalis species yield cardenolide '
                                                          'cardiac glycosides such as digoxin '
                                                          'and digitoxin that inhibit the '
                                                          'Na+/K+-ATPase. The resulting rise '
                                                          'in intracellular sodium reduces '
                                                          'calcium extrusion via NCX, '
                                                          'increasing cardiac contractile '
                                                          'force. Historically, foxglove '
                                                          'preparations were among the '
                                                          'earliest standardized natural '
                                                          'cardiac therapies.',
                                           'choice_explanations': {'A': 'Digitalis (foxglove) '
                                                                        'yields cardenolide '
                                                                        'cardiac glycosides '
                                                                        '(e.g., '
                                                                        'digoxin/digitoxin) '
                                                                        'that inhibit '
                                                                        'Na+/K+-ATPase, '
                                                                        'increasing cardiac '
                                                                        'contractility via '
                                                                        'Na+/Ca2+ exchange '
                                                                        'effects.',
                                                                   'B': 'Opioid alkaloids from '
                                                                        'Papaver somniferum '
                                                                        'are a different '
                                                                        'natural-product class '
                                                                        '(morphinan '
                                                                        'alkaloids), not '
                                                                        'digitalis glycosides.',
                                                                   'C': 'Quinine from Cinchona '
                                                                        'is an antimalarial '
                                                                        'alkaloid lineage '
                                                                        'distinct from '
                                                                        'Digitalis cardiac '
                                                                        'glycosides.',
                                                                   'D': 'Cocaine from '
                                                                        'Erythroxylum is a '
                                                                        'tropane local '
                                                                        'anesthetic/stimulant '
                                                                        'alkaloid, not the '
                                                                        'digitalis glycoside '
                                                                        'story.'}},
                                          {'question': 'Alkaloids are typically?',
                                           'options': ['A) Neutral polysaccharides without '
                                                       'nitrogen',
                                                       'B) Nitrogen-containing natural bases',
                                                       'C) Simple inorganic mineral salts only',
                                                       'D) Volatile hydrocarbon oils '
                                                       'exclusively'],
                                           'answer': 'B) Nitrogen-containing natural bases',
                                           'explanation': 'Alkaloids are typically basic, '
                                                          'nitrogen-containing secondary '
                                                          'metabolites produced by plants and '
                                                          'other organisms. The nitrogen often '
                                                          'resides in a heterocyclic ring and '
                                                          'confers characteristic solubility '
                                                          'and receptor activity. Morphine, '
                                                          'quinine, atropine, and caffeine '
                                                          'illustrate the pharmacologic '
                                                          'diversity of alkaloid natural '
                                                          'products.',
                                           'choice_explanations': {'A': 'Neutral '
                                                                        'polysaccharides '
                                                                        'without nitrogen '
                                                                        '(e.g., starch, '
                                                                        'cellulose) lack the '
                                                                        'defining basic '
                                                                        'nitrogen of '
                                                                        'alkaloids.',
                                                                   'B': 'Alkaloids are '
                                                                        'typically '
                                                                        'nitrogen-containing '
                                                                        'basic secondary '
                                                                        'metabolites, often '
                                                                        'heterocyclic, with '
                                                                        'pronounced '
                                                                        'pharmacologic '
                                                                        'activity.',
                                                                   'C': 'Simple inorganic '
                                                                        'mineral salts are not '
                                                                        'organic nitrogenous '
                                                                        'bases and fall '
                                                                        'outside the alkaloid '
                                                                        'definition.',
                                                                   'D': 'Volatile hydrocarbon '
                                                                        'oils (many terpenes '
                                                                        'without basic '
                                                                        'nitrogen) are '
                                                                        'essential oils, not '
                                                                        'classic alkaloids.'}}],
                                 'medium': [{'question': "St John's wort interaction theme?",
                                             'options': ['A) CYP inhibition raising all drug '
                                                         'levels equally',
                                                         'B) Complete blockade of renal drug '
                                                         'excretion',
                                                         'C) CYP induction reducing many '
                                                         'substrate drug levels',
                                                         'D) Neutralization of gastric acid '
                                                         'only'],
                                             'answer': 'C) CYP induction reducing many '
                                                       'substrate drug levels',
                                             'explanation': "Hypericum perforatum (St John's "
                                                            'wort) induces CYP3A4 and '
                                                            'P-glycoprotein via pregnane X '
                                                            'receptor activation, accelerating '
                                                            'clearance of many substrates. '
                                                            'Plasma concentrations of drugs '
                                                            'such as some oral contraceptives, '
                                                            'immunosuppressants, and '
                                                            'antiretrovirals can fall below '
                                                            'therapeutic levels. The '
                                                            'interaction is a classic '
                                                            'inductive herb–drug interaction '
                                                            'with loss-of-efficacy risk.',
                                             'choice_explanations': {'A': "St John's wort "
                                                                          'predominantly '
                                                                          'induces, rather '
                                                                          'than inhibits, '
                                                                          'CYP3A4/P-gp; '
                                                                          'induction '
                                                                          'lowers—not '
                                                                          'raises—many '
                                                                          'substrate levels.',
                                                                     'B': 'It does not '
                                                                          'completely block '
                                                                          'renal excretion; '
                                                                          'the major '
                                                                          'interaction theme '
                                                                          'is '
                                                                          'enzyme/transporter '
                                                                          'induction.',
                                                                     'C': 'Hypericum induces '
                                                                          'CYP3A4 and '
                                                                          'P-glycoprotein via '
                                                                          'PXR activation, '
                                                                          'accelerating '
                                                                          'clearance and '
                                                                          'reducing plasma '
                                                                          'levels of many '
                                                                          'substrates (e.g., '
                                                                          'immunosuppressants, '
                                                                          'oral '
                                                                          'contraceptives).',
                                                                     'D': 'Gastric acid '
                                                                          'neutralization is '
                                                                          'an antacid effect, '
                                                                          'not the '
                                                                          'PXR-mediated '
                                                                          'induction mechanism '
                                                                          "of St John's "
                                                                          'wort.'}},
                                            {'question': 'Secondary metabolites serve plants '
                                                         'often as?',
                                             'options': ['A) Primary energy stores like starch '
                                                         'only',
                                                         'B) Structural cellulose replacement '
                                                         'only',
                                                         'C) Photosynthetic pigments '
                                                         'exclusively',
                                                         'D) Defense or attraction chemicals; '
                                                         'humans may use as drugs'],
                                             'answer': 'D) Defense or attraction chemicals; '
                                                       'humans may use as drugs',
                                             'explanation': 'Secondary metabolites are organic '
                                                            'compounds not required for basic '
                                                            'plant growth and primary '
                                                            'metabolism but often mediating '
                                                            'defense, signaling, or pollinator '
                                                            'attraction. Humans exploit many '
                                                            'of these molecules—alkaloids, '
                                                            'terpenoids, phenolics, and '
                                                            'glycosides—as drugs or leads. '
                                                            'Their ecological roles help '
                                                            'explain the prevalence of potent '
                                                            'bioactivity in medicinal plants.',
                                             'choice_explanations': {'A': 'Primary energy '
                                                                          'stores like starch '
                                                                          'are primary '
                                                                          'metabolites for '
                                                                          'growth/energy, not '
                                                                          'the ecological '
                                                                          'secondary-metabolite '
                                                                          'role.',
                                                                     'B': 'Cellulose is a '
                                                                          'structural primary '
                                                                          'polymer; secondary '
                                                                          'metabolites are not '
                                                                          'mere cellulose '
                                                                          'replacements.',
                                                                     'C': 'Photosynthetic '
                                                                          'pigments support '
                                                                          'light capture as '
                                                                          'primary physiology; '
                                                                          'many bioactive '
                                                                          'secondary '
                                                                          'metabolites serve '
                                                                          'defense/attraction '
                                                                          'instead.',
                                                                     'D': 'Secondary '
                                                                          'metabolites often '
                                                                          'mediate plant '
                                                                          'defense or '
                                                                          'pollinator '
                                                                          'attraction; humans '
                                                                          'exploit many of '
                                                                          'these compounds as '
                                                                          'drugs (alkaloids, '
                                                                          'glycosides, '
                                                                          'etc.).'}},
                                            {'question': 'Standardization of herbal drugs aims '
                                                         'to?',
                                             'options': ['A) Consistent content of marker or '
                                                         'active constituents',
                                                         'B) Random seasonal variation without '
                                                         'assay',
                                                         'C) Maximum bitterness as the sole '
                                                         'quality metric',
                                                         'D) Elimination of all secondary '
                                                         'metabolites'],
                                             'answer': 'A) Consistent content of marker or '
                                                       'active constituents',
                                             'explanation': 'Herbal drug standardization seeks '
                                                            'reproducible levels of marker '
                                                            'compounds or known actives across '
                                                            'batches of crude drugs or '
                                                            'extracts. Chemical assays, '
                                                            'chromatographic fingerprints, and '
                                                            'botanical identification reduce '
                                                            'variability from species, season, '
                                                            'and processing. Consistent '
                                                            'constituent content is a '
                                                            'prerequisite for predictable '
                                                            'pharmacologic effect and quality '
                                                            'control.',
                                             'choice_explanations': {'A': 'Standardization '
                                                                          'seeks reproducible '
                                                                          'marker/active '
                                                                          'constituent levels '
                                                                          'across batches via '
                                                                          'chemical assays and '
                                                                          'chromatographic '
                                                                          'profiles for '
                                                                          'consistent '
                                                                          'pharmacologic '
                                                                          'exposure.',
                                                                     'B': 'Allowing random '
                                                                          'seasonal variation '
                                                                          'without assay '
                                                                          'defeats '
                                                                          'batch-to-batch '
                                                                          'consistency of '
                                                                          'herbal drug '
                                                                          'quality.',
                                                                     'C': 'Maximum bitterness '
                                                                          'is organoleptic and '
                                                                          'nonspecific; it is '
                                                                          'not a sole '
                                                                          'validated content '
                                                                          'standard for most '
                                                                          'herbals.',
                                                                     'D': 'Eliminating all '
                                                                          'secondary '
                                                                          'metabolites would '
                                                                          'remove the '
                                                                          'bioactive '
                                                                          'principles that '
                                                                          'herbal drugs rely '
                                                                          'on.'}}],
                                 'hard': [{'question': 'Microbial natural products gave us '
                                                       'many?',
                                           'options': ['A) Inhaled beta-agonist '
                                                       'bronchodilators',
                                                       'B) Antibiotics such as penicillins and '
                                                       'aminoglycosides',
                                                       'C) Synthetic ACE inhibitors only',
                                                       'D) Monoclonal antibodies from '
                                                       'hybridomas only'],
                                           'answer': 'B) Antibiotics such as penicillins and '
                                                     'aminoglycosides',
                                           'explanation': 'Microbial secondary metabolism has '
                                                          'supplied a large fraction of '
                                                          'clinical antibiotics, beginning '
                                                          'with penicillin from Penicillium '
                                                          'and extending to aminoglycosides, '
                                                          'macrolides, tetracyclines, and many '
                                                          'others. Actinomycetes and fungi '
                                                          'remain major sources of '
                                                          'antibacterial scaffolds. '
                                                          'Semi-synthesis from microbial '
                                                          'natural products continues to '
                                                          'expand spectrum and overcome '
                                                          'resistance.',
                                           'choice_explanations': {'A': 'Inhaled β-agonist '
                                                                        'bronchodilators are '
                                                                        'synthetic '
                                                                        'sympathomimetics, not '
                                                                        'classic microbial '
                                                                        'natural-product '
                                                                        'antibiotics.',
                                                                   'B': 'Microbial secondary '
                                                                        'metabolism yielded '
                                                                        'many '
                                                                        'antibiotics—penicillins '
                                                                        'from Penicillium, '
                                                                        'aminoglycosides from '
                                                                        'actinomycetes, and '
                                                                        'related '
                                                                        'scaffolds—that remain '
                                                                        'clinical mainstays.',
                                                                   'C': 'Synthetic ACE '
                                                                        'inhibitors (e.g., '
                                                                        'captopril lineage) '
                                                                        'were inspired partly '
                                                                        'by peptides but are '
                                                                        'not “many antibiotics '
                                                                        'from microbes” as a '
                                                                        'class answer.',
                                                                   'D': 'Monoclonal antibodies '
                                                                        'from hybridomas are '
                                                                        'biologic proteins '
                                                                        'from mammalian cell '
                                                                        'technology, not '
                                                                        'microbial '
                                                                        'natural-product '
                                                                        'antibiotics.'}},
                                          {'question': 'Adulteration of herbal products may '
                                                       'involve?',
                                           'options': ['A) Only improved drying under GMP',
                                                       'B) Only correct Latin binomial '
                                                       'labeling',
                                                       'C) Wrong species, heavy metals, or '
                                                       'undeclared drugs',
                                                       'D) Only validated marker assay '
                                                       'certificates'],
                                           'answer': 'C) Wrong species, heavy metals, or '
                                                     'undeclared drugs',
                                           'explanation': 'Herbal product adulteration may '
                                                          'substitute incorrect species, add '
                                                          'heavy metals from contaminated soil '
                                                          'or processing, or illegally spike '
                                                          'undeclared synthetic drugs. Such '
                                                          'practices create toxicity, '
                                                          'hypersensitivity, and unexpected '
                                                          'pharmacologic effects. '
                                                          'Authentication (macroscopy, '
                                                          'microscopy, DNA barcoding, '
                                                          'analytics) is therefore essential '
                                                          'for patient safety.',
                                           'choice_explanations': {'A': 'Improved GMP drying '
                                                                        'is quality '
                                                                        'improvement, not '
                                                                        'adulteration.',
                                                                   'B': 'Correct Latin '
                                                                        'binomial labeling is '
                                                                        'proper identification '
                                                                        'practice, opposite of '
                                                                        'adulteration.',
                                                                   'C': 'Adulteration includes '
                                                                        'substitution with '
                                                                        'wrong species, '
                                                                        'heavy-metal '
                                                                        'contamination, or '
                                                                        'illegal spiking with '
                                                                        'undeclared synthetic '
                                                                        'drugs, compromising '
                                                                        'safety and identity.',
                                                                   'D': 'Validated marker '
                                                                        'assay certificates '
                                                                        'support authenticity; '
                                                                        'they are quality '
                                                                        'assurance, not '
                                                                        'adulteration.'}},
                                          {'question': 'Phytochemical screening tests detect '
                                                       'classes like?',
                                           'options': ['A) Only elemental sodium and potassium',
                                                       'B) Only residual organic solvents',
                                                       'C) Only tablet hardness and friability',
                                                       'D) Alkaloids, flavonoids, saponins, '
                                                       'and related classes'],
                                           'answer': 'D) Alkaloids, flavonoids, saponins, and '
                                                     'related classes',
                                           'explanation': 'Phytochemical screening uses '
                                                          'colorimetric and precipitation '
                                                          'tests to detect major '
                                                          'natural-product classes such as '
                                                          'alkaloids, flavonoids, saponins, '
                                                          'tannins, and cardiac glycosides in '
                                                          'extracts. These assays provide '
                                                          'rapid preliminary characterization '
                                                          'before chromatographic isolation. '
                                                          'Positive screens guide subsequent '
                                                          'targeted extraction and structural '
                                                          'elucidation.',
                                           'choice_explanations': {'A': 'Elemental Na/K assays '
                                                                        'are inorganic '
                                                                        'analysis, not '
                                                                        'classical '
                                                                        'phytochemical class '
                                                                        'screening for organic '
                                                                        'secondary '
                                                                        'metabolites.',
                                                                   'B': 'Residual solvent '
                                                                        'testing is ICH '
                                                                        'impurity control for '
                                                                        'extracts/processes, '
                                                                        'not class detection '
                                                                        'of '
                                                                        'alkaloids/flavonoids.',
                                                                   'C': 'Tablet '
                                                                        'hardness/friability '
                                                                        'are pharmaceutic '
                                                                        'mechanical tests, not '
                                                                        'phytochemical '
                                                                        'screens.',
                                                                   'D': 'Phytochemical '
                                                                        'screening uses '
                                                                        'color/precipitation '
                                                                        'reactions to detect '
                                                                        'classes such as '
                                                                        'alkaloids, '
                                                                        'flavonoids, saponins, '
                                                                        'tannins, and related '
                                                                        'natural-product '
                                                                        'groups.'}}],
                                 'extreme': [{'question': 'Aristolochic acid concern?',
                                              'options': ['A) Nephrotoxicity and '
                                                          'carcinogenicity in some botanicals',
                                                          'B) Reversible anticholinergic '
                                                          'dryness as the main toxicity',
                                                          'C) Dose-dependent serotonin '
                                                          'syndrome from MAO inhibition',
                                                          'D) Beneficial CYP3A4 induction '
                                                          'raising digoxin effect'],
                                              'answer': 'A) Nephrotoxicity and carcinogenicity '
                                                        'in some botanicals',
                                              'explanation': 'Aristolochic acids from '
                                                             'Aristolochia and related '
                                                             'botanicals form DNA adducts '
                                                             'after nitroreduction and are '
                                                             'established nephrotoxins and '
                                                             'carcinogens. Exposure is linked '
                                                             'to aristolochic acid nephropathy '
                                                             'and urothelial carcinoma. '
                                                             'Regulatory bans and warnings '
                                                             'reflect this mechanism-based '
                                                             'genotoxic risk in certain '
                                                             'traditional preparations.',
                                              'choice_explanations': {'A': 'Aristolochic acids '
                                                                           'form DNA adducts '
                                                                           'after '
                                                                           'nitroreduction and '
                                                                           'cause aristolochic '
                                                                           'acid nephropathy '
                                                                           'and urothelial '
                                                                           'carcinoma—established '
                                                                           'nephrotoxicity and '
                                                                           'carcinogenicity.',
                                                                      'B': 'Reversible '
                                                                           'anticholinergic '
                                                                           'dryness is '
                                                                           'atropine-like '
                                                                           'muscarinic '
                                                                           'blockade, not '
                                                                           'aristolochic acid '
                                                                           'DNA-adduct '
                                                                           'toxicity.',
                                                                      'C': 'Serotonin syndrome '
                                                                           'from MAO '
                                                                           'inhibition is a '
                                                                           'monoamine toxicity '
                                                                           'syndrome, '
                                                                           'unrelated to '
                                                                           'aristolochic acid '
                                                                           'mechanisms.',
                                                                      'D': 'CYP3A4 induction '
                                                                           'lowering '
                                                                           'digoxin/P-gp '
                                                                           'substrates is a St '
                                                                           "John's wort theme; "
                                                                           'aristolochic acid '
                                                                           'is not beneficial '
                                                                           'induction raising '
                                                                           'digoxin effect.'}},
                                             {'question': 'Aflatoxins in crude drugs are?',
                                              'options': ['A) Plant primary metabolites '
                                                          'essential for growth',
                                                          'B) Fungal toxins posing '
                                                          'contamination risk',
                                                          'C) Inorganic heavy-metal antidotes',
                                                          'D) Sterile filtration validation '
                                                          'markers'],
                                              'answer': 'B) Fungal toxins posing contamination '
                                                        'risk',
                                              'explanation': 'Aflatoxins are difuranocoumarin '
                                                             'mycotoxins produced mainly by '
                                                             'Aspergillus flavus and A. '
                                                             'parasiticus contaminating '
                                                             'improperly stored plant '
                                                             'materials. Aflatoxin B1 is '
                                                             'metabolically activated to an '
                                                             'epoxide that binds DNA and is a '
                                                             'potent hepatocarcinogen. Crude '
                                                             'drug quality control therefore '
                                                             'includes limits and testing for '
                                                             'fungal toxin contamination.',
                                              'choice_explanations': {'A': 'Plant primary '
                                                                           'metabolites '
                                                                           'essential for '
                                                                           'growth (sugars, '
                                                                           'amino acids) are '
                                                                           'not aflatoxins; '
                                                                           'aflatoxins are '
                                                                           'fungal '
                                                                           'contaminants.',
                                                                      'B': 'Aflatoxins are '
                                                                           'difuranocoumarin '
                                                                           'mycotoxins from '
                                                                           'Aspergillus '
                                                                           'species '
                                                                           'contaminating '
                                                                           'poorly stored '
                                                                           'plant materials; '
                                                                           'aflatoxin B1 is a '
                                                                           'potent '
                                                                           'hepatocarcinogen '
                                                                           'via CYP activation '
                                                                           'to epoxides.',
                                                                      'C': 'Inorganic '
                                                                           'heavy-metal '
                                                                           'antidotes (e.g., '
                                                                           'chelators) are '
                                                                           'therapeutic '
                                                                           'agents, not '
                                                                           'mycotoxin '
                                                                           'contaminants.',
                                                                      'D': 'Sterile filtration '
                                                                           'validation markers '
                                                                           'monitor filter '
                                                                           'integrity; they '
                                                                           'are process '
                                                                           'controls, not '
                                                                           'aflatoxins.'}},
                                             {'question': 'Ethnopharmacology contributes by?',
                                              'options': ['A) Replacing all clinical trials '
                                                          'with folklore alone',
                                                          'B) Ignoring traditional use during '
                                                          'discovery',
                                                          'C) Studying traditional use to '
                                                          'guide drug discovery',
                                                          'D) Mandating synthetic routes for '
                                                          'every natural product'],
                                              'answer': 'C) Studying traditional use to guide '
                                                        'drug discovery',
                                              'explanation': 'Ethnopharmacology investigates '
                                                             'traditional medicinal uses of '
                                                             'organisms within cultural '
                                                             'contexts to generate hypotheses '
                                                             'for bioactive compound '
                                                             'discovery. Historical use can '
                                                             'prioritize species for '
                                                             'extraction and bioassay, but '
                                                             'traditional claims still require '
                                                             'chemical isolation, mechanistic '
                                                             'study, and clinical evidence. It '
                                                             'is a discovery guide, not proof '
                                                             'of efficacy or safety alone.',
                                              'choice_explanations': {'A': 'Folklore alone '
                                                                           'without '
                                                                           'clinical/scientific '
                                                                           'evaluation cannot '
                                                                           'replace controlled '
                                                                           'trials for '
                                                                           'efficacy and '
                                                                           'safety claims.',
                                                                      'B': 'Ignoring '
                                                                           'traditional use '
                                                                           'discards a '
                                                                           'historically '
                                                                           'productive '
                                                                           'discovery '
                                                                           'hypothesis source '
                                                                           'that '
                                                                           'ethnopharmacology '
                                                                           'systematically '
                                                                           'studies.',
                                                                      'C': 'Ethnopharmacology '
                                                                           'studies '
                                                                           'traditional '
                                                                           'medicinal uses '
                                                                           'within cultural '
                                                                           'contexts to '
                                                                           'prioritize '
                                                                           'organisms and '
                                                                           'bioassays for drug '
                                                                           'discovery (e.g., '
                                                                           'historical leads '
                                                                           'like artemisinin).',
                                                                      'D': 'Mandating '
                                                                           'synthetic routes '
                                                                           'for every natural '
                                                                           'product is process '
                                                                           'chemistry policy, '
                                                                           'not the '
                                                                           'ethnopharmacologic '
                                                                           'discovery '
                                                                           'contribution.'}}]},
                   'cases': {'easy': [{'title': 'Herbal Product Question',
                                       'stem': "A patient asks if 'natural' means always safe.",
                                       'question': 'Answer theme?',
                                       'answer': 'Natural ≠ harmless; interactions and '
                                                 'variability exist.',
                                       'discussion': 'Counsel evidence and quality.',
                                       'book_hint': 'Trease and Evans Pharmacognosy'}],
                             'medium': [{'title': 'Transplant Patient on Herbals',
                                         'stem': "A transplant patient starts St John's wort; "
                                                 'tacrolimus levels drop.',
                                         'question': 'Mechanism?',
                                         'answer': 'Induction interaction — stop herbal and '
                                                   'manage levels.',
                                         'discussion': 'Ask about OTCs/herbals always.',
                                         'book_hint': 'Trease and Evans Pharmacognosy'}],
                             'hard': [{'title': "Undeclared Sildenafil in 'Herbal' Capsule",
                                       'stem': 'A man develops severe hypotension after an '
                                               "'herbal' sexual enhancer with nitrate therapy. "
                                               'Choose the safest high-yield next concept '
                                               'before definitive results.',
                                       'question': 'Issue?',
                                       'answer': 'Adulteration with PDE5 inhibitor — dangerous '
                                                 'interaction.',
                                       'discussion': 'Report and counsel.',
                                       'book_hint': 'Trease and Evans Pharmacognosy'}],
                             'extreme': [{'title': 'Herbal Nephropathy Outbreak',
                                          'stem': 'Several patients using a weight-loss herb '
                                                  'develop renal failure; aristolochic acid '
                                                  'detected. Avoid harmful premature treatment '
                                                  'while catastrophic differentials remain '
                                                  'open.',
                                          'question': 'Pharmacy role?',
                                          'answer': 'Identify product, stop exposure, report '
                                                    'to authorities, support clinical care.',
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
                       'questions': {'easy': [{'question': 'Prescription validity checks '
                                                           'include?',
                                               'options': ['A) Patient, drug, dose, route, '
                                                           'frequency, and prescriber details',
                                                           'B) Only the drug name without '
                                                           'strength or directions',
                                                           'C) Only the pharmacy stamp date',
                                                           'D) Only the wholesaler invoice '
                                                           'number'],
                                               'answer': 'A) Patient, drug, dose, route, '
                                                         'frequency, and prescriber details',
                                               'explanation': 'Legal and clinical prescription '
                                                              'review confirms that the '
                                                              'patient identity, medicine, '
                                                              'strength, dose, route, '
                                                              'frequency, and prescriber '
                                                              'details are complete and '
                                                              'appropriate. Ambiguity or '
                                                              'missing elements can lead to '
                                                              'wrong-drug or wrong-dose '
                                                              'errors. Pharmacists also screen '
                                                              'for contraindications and '
                                                              'interactions as part of safe '
                                                              'dispensing.',
                                               'choice_explanations': {'A': 'Valid '
                                                                            'prescriptions '
                                                                            'require '
                                                                            'identifiable '
                                                                            'patient, '
                                                                            'drug/strength, '
                                                                            'dose, route, '
                                                                            'frequency/directions, '
                                                                            'and authorized '
                                                                            'prescriber '
                                                                            'details for legal '
                                                                            'and clinical '
                                                                            'safety checks.',
                                                                       'B': 'Drug name without '
                                                                            'strength or '
                                                                            'directions is '
                                                                            'incomplete and '
                                                                            'unsafe for '
                                                                            'dispensing '
                                                                            'accuracy.',
                                                                       'C': 'Pharmacy stamp '
                                                                            'date alone does '
                                                                            'not establish '
                                                                            'clinical '
                                                                            'completeness or '
                                                                            'legal validity of '
                                                                            'the order '
                                                                            'content.',
                                                                       'D': 'Wholesaler '
                                                                            'invoice numbers '
                                                                            'track '
                                                                            'procurement, not '
                                                                            'prescription '
                                                                            'clinical/legal '
                                                                            'validity for a '
                                                                            'patient.'}},
                                              {'question': 'OTC counseling should cover?',
                                               'options': ['A) Unlimited refill advice without '
                                                           'referral criteria',
                                                           'B) Indication limits, dose, '
                                                           'warnings, and when to refer',
                                                           'C) Encouraging use beyond labeled '
                                                           'maximum always',
                                                           'D) Sharing leftover packs with '
                                                           'family members'],
                                               'answer': 'B) Indication limits, dose, '
                                                         'warnings, and when to refer',
                                               'explanation': 'Over-the-counter counseling '
                                                              'defines the intended '
                                                              'self-limiting indication, '
                                                              'correct dose and duration, key '
                                                              'warnings, and red-flag symptoms '
                                                              'that require referral. This '
                                                              'ensures responsible self-care '
                                                              'and reduces delayed diagnosis '
                                                              'of serious disease. Product '
                                                              'selection should match symptom '
                                                              'pattern, comorbidities, and '
                                                              'interacting medicines.',
                                               'choice_explanations': {'A': 'Unlimited refill '
                                                                            'advice without '
                                                                            'referral criteria '
                                                                            'ignores red-flag '
                                                                            'symptoms and '
                                                                            'labeled duration '
                                                                            'limits for '
                                                                            'self-care.',
                                                                       'B': 'OTC counseling '
                                                                            'covers suitable '
                                                                            'self-limiting '
                                                                            'indications, '
                                                                            'correct '
                                                                            'dose/duration, '
                                                                            'key warnings, and '
                                                                            'when symptoms '
                                                                            'require referral '
                                                                            'to a clinician.',
                                                                       'C': 'Encouraging use '
                                                                            'beyond labeled '
                                                                            'maxima increases '
                                                                            'toxicity risk '
                                                                            'without '
                                                                            'therapeutic '
                                                                            'justification.',
                                                                       'D': 'Sharing leftover '
                                                                            'packs exposes '
                                                                            'others to '
                                                                            'inappropriate '
                                                                            'therapy and loses '
                                                                            'counseling/assessment '
                                                                            'safeguards.'}},
                                              {'question': 'Controlled drugs require?',
                                               'options': ['A) No special records beyond '
                                                           'ordinary OTC sales',
                                                           'B) Display on open self-selection '
                                                           'shelves only',
                                                           'C) Extra legal storage and record '
                                                           'controls per law',
                                                           'D) Verbal orders without any '
                                                           'documentation'],
                                               'answer': 'C) Extra legal storage and record '
                                                         'controls per law',
                                               'explanation': 'Controlled drugs are substances '
                                                              'with recognized abuse or '
                                                              'dependence potential and are '
                                                              'subject to heightened legal '
                                                              'controls on prescribing, '
                                                              'storage, recording, and '
                                                              'destruction. Requirements vary '
                                                              'by jurisdiction but typically '
                                                              'include secure custody and '
                                                              'auditable registers. Compliance '
                                                              'protects patients and limits '
                                                              'diversion into illicit supply.',
                                               'choice_explanations': {'A': 'Controlled drugs '
                                                                            'have '
                                                                            'abuse/dependence '
                                                                            'potential and '
                                                                            'legally require '
                                                                            'more than '
                                                                            'ordinary OTC sale '
                                                                            'records.',
                                                                       'B': 'Open '
                                                                            'self-selection '
                                                                            'shelves increase '
                                                                            'diversion risk; '
                                                                            'controlled drugs '
                                                                            'need secure '
                                                                            'storage per '
                                                                            'regulation.',
                                                                       'C': 'Controlled drugs '
                                                                            'require '
                                                                            'heightened legal '
                                                                            'controls on '
                                                                            'prescribing, '
                                                                            'secure storage, '
                                                                            'recording, and '
                                                                            'supply '
                                                                            'documentation '
                                                                            'beyond ordinary '
                                                                            'medicines.',
                                                                       'D': 'Verbal orders '
                                                                            'without '
                                                                            'documentation '
                                                                            'violate '
                                                                            'controlled-drug '
                                                                            'accountability '
                                                                            'and audit '
                                                                            'trails.'}}],
                                     'medium': [{'question': 'Near miss reporting helps?',
                                                 'options': ['A) Punish staff without system '
                                                             'analysis',
                                                             'B) Hide process weaknesses from '
                                                             'managers',
                                                             'C) Replace all incident reviews '
                                                             'with silence',
                                                             'D) System learning without '
                                                             'waiting for patient harm'],
                                                 'answer': 'D) System learning without waiting '
                                                           'for patient harm',
                                                 'explanation': 'A near miss is an error that '
                                                                'is intercepted before it '
                                                                'reaches the patient or causes '
                                                                'harm. Reporting near misses '
                                                                'reveals latent system '
                                                                'weaknesses—look-alike '
                                                                'packaging, workflow '
                                                                'interruptions, or unclear '
                                                                'protocols—without waiting for '
                                                                'injury. Analysis supports '
                                                                'corrective actions that '
                                                                'strengthen medication-safety '
                                                                'culture.',
                                                 'choice_explanations': {'A': 'Punitive '
                                                                              'responses '
                                                                              'without system '
                                                                              'analysis '
                                                                              'discourage '
                                                                              'reporting and '
                                                                              'miss latent '
                                                                              'process '
                                                                              'failures.',
                                                                         'B': 'Hiding '
                                                                              'weaknesses '
                                                                              'prevents '
                                                                              'organizational '
                                                                              'learning that '
                                                                              'near-miss data '
                                                                              'are meant to '
                                                                              'enable.',
                                                                         'C': 'Silence '
                                                                              'replaces '
                                                                              'learning; '
                                                                              'near-miss '
                                                                              'reporting '
                                                                              'exists to '
                                                                              'surface hazards '
                                                                              'before harm.',
                                                                         'D': 'Near misses are '
                                                                              'intercepted '
                                                                              'errors; '
                                                                              'reporting them '
                                                                              'reveals latent '
                                                                              'system '
                                                                              'weaknesses so '
                                                                              'defenses can be '
                                                                              'strengthened '
                                                                              'without waiting '
                                                                              'for patient '
                                                                              'injury.'}},
                                                {'question': 'Generic substitution depends on?',
                                                 'options': ['A) Local law/formulary and '
                                                             'clinical appropriateness',
                                                             'B) Patient preference for tablet '
                                                             'color only',
                                                             'C) Wholesaler stock photos alone',
                                                             'D) Always substituting '
                                                             'regardless of narrow therapeutic '
                                                             'index'],
                                                 'answer': 'A) Local law/formulary and '
                                                           'clinical appropriateness',
                                                 'explanation': 'Generic substitution replaces '
                                                                'a brand product with a '
                                                                'bioequivalent generic '
                                                                'containing the same active '
                                                                'substance when law and '
                                                                'formulary policy allow. '
                                                                'Clinical appropriateness '
                                                                'still matters for narrow '
                                                                'therapeutic-index drugs, '
                                                                'modified-release forms, and '
                                                                'patient-specific concerns. '
                                                                'Pharmacists apply local rules '
                                                                'while ensuring therapeutic '
                                                                'equivalence and continuity of '
                                                                'effect.',
                                                 'choice_explanations': {'A': 'Generic '
                                                                              'substitution '
                                                                              'depends on '
                                                                              'law/formulary '
                                                                              'policy plus '
                                                                              'clinical '
                                                                              'appropriateness '
                                                                              '(e.g., caution '
                                                                              'with some '
                                                                              'narrow '
                                                                              'therapeutic '
                                                                              'index drugs and '
                                                                              'patient-specific '
                                                                              'factors).',
                                                                         'B': 'Tablet color '
                                                                              'preference is '
                                                                              'not a '
                                                                              'scientific or '
                                                                              'legal basis for '
                                                                              'interchange '
                                                                              'decisions.',
                                                                         'C': 'Wholesaler '
                                                                              'stock photos do '
                                                                              'not establish '
                                                                              'bioequivalence '
                                                                              'or legal '
                                                                              'authority to '
                                                                              'substitute.',
                                                                         'D': 'Blind '
                                                                              'substitution '
                                                                              'regardless of '
                                                                              'narrow '
                                                                              'therapeutic '
                                                                              'index can cause '
                                                                              'clinically '
                                                                              'significant '
                                                                              'exposure shifts '
                                                                              'for some '
                                                                              'agents.'}},
                                                {'question': 'Privacy in pharmacy means?',
                                                 'options': ['A) Discussing therapy loudly at '
                                                             'the counter for teaching',
                                                             'B) Protecting patient '
                                                             'confidential information',
                                                             'C) Posting prescriptions on '
                                                             'social media for advice',
                                                             'D) Sharing full histories with '
                                                             'unrelated third parties'],
                                                 'answer': 'B) Protecting patient confidential '
                                                           'information',
                                                 'explanation': 'Pharmacy privacy obligations '
                                                                'protect confidential health '
                                                                'information from unauthorized '
                                                                'disclosure under professional '
                                                                'ethics and data-protection '
                                                                'law. Counseling should occur '
                                                                'with reasonable auditory '
                                                                'privacy, and records access '
                                                                'must be limited to legitimate '
                                                                'care needs. Breaches can harm '
                                                                'patients and undermine trust '
                                                                'in pharmaceutical care.',
                                                 'choice_explanations': {'A': 'Loud counter '
                                                                              'discussions '
                                                                              'expose '
                                                                              'confidential '
                                                                              'health '
                                                                              'information to '
                                                                              'bystanders, '
                                                                              'breaching '
                                                                              'privacy duties.',
                                                                         'B': 'Pharmacy '
                                                                              'privacy '
                                                                              'protects '
                                                                              'confidential '
                                                                              'patient health '
                                                                              'information '
                                                                              'from '
                                                                              'unauthorized '
                                                                              'disclosure '
                                                                              'under ethics '
                                                                              'and '
                                                                              'data-protection '
                                                                              'law.',
                                                                         'C': 'Posting '
                                                                              'prescriptions '
                                                                              'on social media '
                                                                              'is unauthorized '
                                                                              'disclosure of '
                                                                              'identifiable '
                                                                              'health data.',
                                                                         'D': 'Sharing full '
                                                                              'histories with '
                                                                              'unrelated third '
                                                                              'parties '
                                                                              'violates '
                                                                              'confidentiality '
                                                                              'without lawful '
                                                                              'basis or '
                                                                              'consent.'}}],
                                     'hard': [{'question': 'Emergency supply frameworks (where '
                                                           'legal) require?',
                                               'options': ['A) Dispensing any CD without '
                                                           'records if the patient asks',
                                                           'B) Ignoring all documentation to '
                                                           'save time',
                                                           'C) Professional judgment, legal '
                                                           'criteria, and documentation',
                                                           'D) Supplying unlimited quantities '
                                                           'for twelve months'],
                                               'answer': 'C) Professional judgment, legal '
                                                         'criteria, and documentation',
                                               'explanation': 'Where emergency supply without '
                                                              'a current prescription is '
                                                              'legally permitted, pharmacists '
                                                              'apply statutory criteria such '
                                                              'as prior treatment, appropriate '
                                                              'indication, and quantity '
                                                              'limits. Professional judgment '
                                                              'assesses clinical risk if '
                                                              'supply is deferred versus '
                                                              'provided. Documentation of '
                                                              'assessment and supply is '
                                                              'required for accountability and '
                                                              'continuity with the usual '
                                                              'prescriber.',
                                               'choice_explanations': {'A': 'Dispensing any '
                                                                            'controlled drug '
                                                                            'without required '
                                                                            'records because '
                                                                            'the patient asks '
                                                                            'violates '
                                                                            'controlled-drug '
                                                                            'law and '
                                                                            'accountability.',
                                                                       'B': 'Skipping '
                                                                            'documentation '
                                                                            'removes the audit '
                                                                            'trail legally '
                                                                            'required for '
                                                                            'emergency supply '
                                                                            'where permitted.',
                                                                       'C': 'Where emergency '
                                                                            'supply without a '
                                                                            'current '
                                                                            'prescription is '
                                                                            'allowed, '
                                                                            'pharmacists must '
                                                                            'apply statutory '
                                                                            'criteria, '
                                                                            'professional '
                                                                            'judgment on '
                                                                            'appropriateness, '
                                                                            'and complete '
                                                                            'required '
                                                                            'documentation.',
                                                                       'D': 'Unlimited '
                                                                            'twelve-month '
                                                                            'quantities exceed '
                                                                            'emergency-supply '
                                                                            'intent, which is '
                                                                            'typically limited '
                                                                            'interim supply '
                                                                            'pending '
                                                                            'prescriber '
                                                                            'contact.'}},
                                              {'question': 'Antimicrobial stewardship in '
                                                           'community includes?',
                                               'options': ['A) Recommending antibiotics for '
                                                           'all viral colds',
                                                           'B) Pressure to complete leftover '
                                                           'courses from prior illnesses',
                                                           'C) Automatic OTC antibiotic sales '
                                                           'without assessment',
                                                           'D) Avoiding unnecessary '
                                                           'antibiotics, counseling adherence, '
                                                           'referring appropriately'],
                                               'answer': 'D) Avoiding unnecessary antibiotics, '
                                                         'counseling adherence, referring '
                                                         'appropriately',
                                               'explanation': 'Community antimicrobial '
                                                              'stewardship reduces unnecessary '
                                                              'antibacterial exposure that '
                                                              'selects for resistant '
                                                              'organisms. Pharmacists counsel '
                                                              'on adherence when antibiotics '
                                                              'are indicated, avoid endorsing '
                                                              'antibiotics for viral '
                                                              'self-limiting illness, and '
                                                              'refer patients with red-flag '
                                                              'infections. These actions '
                                                              'preserve antibiotic '
                                                              'effectiveness at a population '
                                                              'level.',
                                               'choice_explanations': {'A': 'Antibiotics do '
                                                                            'not treat viral '
                                                                            'colds; '
                                                                            'unnecessary '
                                                                            'exposure selects '
                                                                            'resistant '
                                                                            'bacteria without '
                                                                            'clinical benefit.',
                                                                       'B': 'Pressuring use of '
                                                                            'leftover courses '
                                                                            'from prior '
                                                                            'illnesses '
                                                                            'mismatches '
                                                                            'spectrum/duration '
                                                                            'to the current '
                                                                            'syndrome and '
                                                                            'promotes '
                                                                            'resistance.',
                                                                       'C': 'OTC antibiotic '
                                                                            'sales without '
                                                                            'assessment bypass '
                                                                            'indication review '
                                                                            'and stewardship.',
                                                                       'D': 'Community '
                                                                            'stewardship '
                                                                            'avoids '
                                                                            'unnecessary '
                                                                            'antibacterials, '
                                                                            'counsels '
                                                                            'adherence when '
                                                                            'antibiotics are '
                                                                            'indicated, and '
                                                                            'refers red-flag '
                                                                            'or uncertain '
                                                                            'cases '
                                                                            'appropriately.'}},
                                              {'question': 'Health promotion role example?',
                                               'options': ['A) Smoking cessation support',
                                                           'B) Refusing all public-health '
                                                           'conversations',
                                                           'C) Promoting unproven detox kits '
                                                           'as first-line',
                                                           'D) Replacing vaccines with herbal '
                                                           'tonics routinely'],
                                               'answer': 'A) Smoking cessation support',
                                               'explanation': 'Smoking cessation support is a '
                                                              'core health-promotion role in '
                                                              'pharmacy practice, combining '
                                                              'behavioral advice with '
                                                              'evidence-based pharmacotherapy '
                                                              'such as nicotine replacement, '
                                                              'varenicline, or bupropion where '
                                                              'appropriate. Nicotine addiction '
                                                              'is mediated by dopaminergic '
                                                              'reinforcement pathways that '
                                                              'cessation medicines help '
                                                              'modulate. Reducing tobacco use '
                                                              'lowers cardiovascular, '
                                                              'pulmonary, and cancer risk.',
                                               'choice_explanations': {'A': 'Smoking cessation '
                                                                            'support combines '
                                                                            'behavioral '
                                                                            'counseling with '
                                                                            'evidence-based '
                                                                            'pharmacotherapy '
                                                                            '(NRT, '
                                                                            'varenicline, '
                                                                            'bupropion) to '
                                                                            'reduce nicotine '
                                                                            'dependence and '
                                                                            'tobacco harm.',
                                                                       'B': 'Refusing '
                                                                            'public-health '
                                                                            'conversations '
                                                                            'abandons a core '
                                                                            'preventive '
                                                                            'pharmacy role.',
                                                                       'C': 'Unproven detox '
                                                                            'kits lack outcome '
                                                                            'evidence and '
                                                                            'divert from '
                                                                            'proven cessation '
                                                                            'therapies.',
                                                                       'D': 'Replacing '
                                                                            'vaccines with '
                                                                            'herbal tonics '
                                                                            'removes proven '
                                                                            'immunization '
                                                                            'benefit and is '
                                                                            'not '
                                                                            'evidence-based '
                                                                            'health '
                                                                            'promotion.'}}],
                                     'extreme': [{'question': 'Suspected forged CD '
                                                              'prescription?',
                                                  'options': ['A) Dispense quickly to avoid '
                                                              'confrontation',
                                                              'B) Do not dispense; verify and '
                                                              'report per legal pathway',
                                                              'C) Alter the prescription to a '
                                                              'weaker opioid yourself',
                                                              'D) Give a partial supply '
                                                              'without any record'],
                                                  'answer': 'B) Do not dispense; verify and '
                                                            'report per legal pathway',
                                                  'explanation': 'Suspected forged or '
                                                                 'fraudulent controlled-drug '
                                                                 'prescriptions raise '
                                                                 'diversion and patient-safety '
                                                                 'risks if dispensed. '
                                                                 'Pharmacists must not supply '
                                                                 'when authenticity cannot be '
                                                                 'established and should '
                                                                 'verify with the purported '
                                                                 'prescriber and follow legal '
                                                                 'reporting pathways. This '
                                                                 'protects legitimate patients '
                                                                 'while interrupting illicit '
                                                                 'acquisition of controlled '
                                                                 'substances.',
                                                  'choice_explanations': {'A': 'Rapid '
                                                                               'dispensing of '
                                                                               'a suspected '
                                                                               'forged CD '
                                                                               'prescription '
                                                                               'facilitates '
                                                                               'diversion and '
                                                                               'potential '
                                                                               'overdose '
                                                                               'without '
                                                                               'authenticity '
                                                                               'verification.',
                                                                          'B': 'When '
                                                                               'forgery/fraud '
                                                                               'is suspected, '
                                                                               'do not '
                                                                               'dispense; '
                                                                               'verify with '
                                                                               'the purported '
                                                                               'prescriber/authorities '
                                                                               'and follow '
                                                                               'legal '
                                                                               'reporting '
                                                                               'pathways to '
                                                                               'prevent '
                                                                               'diversion.',
                                                                          'C': 'Altering the '
                                                                               'prescription '
                                                                               'yourself '
                                                                               'falsifies a '
                                                                               'controlled-drug '
                                                                               'order and does '
                                                                               'not resolve '
                                                                               'authenticity '
                                                                               'concerns.',
                                                                          'D': 'Partial supply '
                                                                               'without record '
                                                                               'still releases '
                                                                               'controlled '
                                                                               'substances '
                                                                               'without lawful '
                                                                               'documentation.'}},
                                                 {'question': 'Child dosing error risk '
                                                              'mitigation?',
                                                  'options': ['A) Estimate dose from adult '
                                                              'tablets by eye only',
                                                              'B) Ignore maximum dose caps if '
                                                              'the child is tall',
                                                              'C) mg/kg checks, max dose caps, '
                                                              'and double-checks when required',
                                                              'D) Use household spoons as the '
                                                              'only measuring device'],
                                                  'answer': 'C) mg/kg checks, max dose caps, '
                                                            'and double-checks when required',
                                                  'explanation': 'Pediatric doses are commonly '
                                                                 'calculated on a mg/kg (or '
                                                                 'mg/m²) basis because '
                                                                 'clearance and volume of '
                                                                 'distribution scale with size '
                                                                 'and maturation. Maximum dose '
                                                                 'caps prevent exceeding adult '
                                                                 'or product-labeled limits '
                                                                 'when weight-based math would '
                                                                 'overshoot. Independent '
                                                                 'double-checks reduce '
                                                                 'arithmetic and decimal-point '
                                                                 'errors that are especially '
                                                                 'hazardous in children.',
                                                  'choice_explanations': {'A': 'Estimating '
                                                                               'pediatric dose '
                                                                               'by eye from '
                                                                               'adult tablets '
                                                                               'ignores mg/kg '
                                                                               'scaling of '
                                                                               'clearance/Vd '
                                                                               'with size and '
                                                                               'maturation, '
                                                                               'risking '
                                                                               'overdose or '
                                                                               'underdose.',
                                                                          'B': 'Ignoring '
                                                                               'maximum dose '
                                                                               'caps in tall '
                                                                               'children can '
                                                                               'still exceed '
                                                                               'organ-limited '
                                                                               'ceilings and '
                                                                               'labeled '
                                                                               'maxima.',
                                                                          'C': 'Pediatric '
                                                                               'dosing uses '
                                                                               'mg/kg (or '
                                                                               'mg/m²) '
                                                                               'calculations, '
                                                                               'respects '
                                                                               'maximum dose '
                                                                               'caps, and '
                                                                               'employs '
                                                                               'independent '
                                                                               'double-checks '
                                                                               'for high-risk '
                                                                               'calculations '
                                                                               'to prevent '
                                                                               'dosing errors.',
                                                                          'D': 'Household '
                                                                               'spoons vary '
                                                                               'widely in '
                                                                               'volume; oral '
                                                                               'syringes '
                                                                               'provide '
                                                                               'accurate '
                                                                               'liquid '
                                                                               'measurement.'}},
                                                 {'question': 'Vaccine fridge excursion '
                                                              'requires?',
                                                  'options': ['A) Immediate use of all vials '
                                                              'without assessment',
                                                              'B) Discard silently without '
                                                              'documentation',
                                                              'C) Return to stock as soon as '
                                                              'the fridge feels cold',
                                                              'D) Quarantine stock and follow '
                                                              'cold-chain protocol before use'],
                                                  'answer': 'D) Quarantine stock and follow '
                                                            'cold-chain protocol before use',
                                                  'explanation': 'Vaccines are '
                                                                 'temperature-sensitive '
                                                                 'biologics; excursions '
                                                                 'outside the labeled '
                                                                 'cold-chain range can '
                                                                 'denature antigens and reduce '
                                                                 'potency. Affected stock is '
                                                                 'quarantined and evaluated '
                                                                 'against stability data and '
                                                                 'public-health protocols '
                                                                 'before any release or '
                                                                 'discard decision. Using '
                                                                 'compromised vaccine risks '
                                                                 'failed immunization and '
                                                                 'false reassurance of '
                                                                 'protection.',
                                                  'choice_explanations': {'A': 'Immediate use '
                                                                               'after '
                                                                               'excursion may '
                                                                               'administer '
                                                                               'denatured '
                                                                               'antigen with '
                                                                               'reduced '
                                                                               'immunogenicity '
                                                                               'without '
                                                                               'stability '
                                                                               'assessment.',
                                                                          'B': 'Silent discard '
                                                                               'without '
                                                                               'documentation '
                                                                               'breaks '
                                                                               'cold-chain '
                                                                               'accountability '
                                                                               'and '
                                                                               'inventory/recall '
                                                                               'traceability.',
                                                                          'C': 'Returning to '
                                                                               'stock when the '
                                                                               'fridge “feels '
                                                                               'cold” ignores '
                                                                               'validated '
                                                                               'temperature–time '
                                                                               'limits and '
                                                                               'stability '
                                                                               'data.',
                                                                          'D': 'Temperature '
                                                                               'excursions can '
                                                                               'denature '
                                                                               'vaccine '
                                                                               'antigens; '
                                                                               'quarantine '
                                                                               'affected stock '
                                                                               'and follow '
                                                                               'cold-chain '
                                                                               'protocol/manufacturer '
                                                                               'guidance '
                                                                               'before any '
                                                                               'release for '
                                                                               'use.'}}]},
                       'cases': {'easy': [{'title': 'OTC Request for Persistent Cough',
                                           'stem': 'Adult wants cough syrup for 4 weeks of '
                                                   'cough with weight loss.',
                                           'question': 'Action?',
                                           'answer': 'Refer — red flags, not simple OTC.',
                                           'discussion': 'Do not mask serious disease.',
                                           'book_hint': 'Community Pharmacy Practice texts / '
                                                        'RPS guidance themes'}],
                                 'medium': [{'title': 'Wrong Strength Almost Dispensed',
                                             'stem': 'Technician selects 100 mg instead of 10 '
                                                     'mg; pharmacist catches it.',
                                             'question': 'Next?',
                                             'answer': 'Correct, document near miss, review '
                                                       'look-alike storage.',
                                             'discussion': 'High-alert drugs need safeguards.',
                                             'book_hint': 'Community Pharmacy Practice texts / '
                                                          'RPS guidance themes'}],
                                 'hard': [{'title': "Request for Neighbor's Antibiotic",
                                           'stem': 'Someone asks for amoxicillin for a '
                                                   'neighbor without prescription. Choose the '
                                                   'safest high-yield next concept before '
                                                   'definitive results.',
                                           'question': 'Correct approach?',
                                           'answer': 'Do not supply illegally; explain and '
                                                     'advise appropriate care pathway.',
                                           'discussion': 'Legal + ethical boundary.',
                                           'book_hint': 'Community Pharmacy Practice texts / '
                                                        'RPS guidance themes'}],
                                 'extreme': [{'title': 'Opioid Prescription Red Flags',
                                              'stem': 'A cash-paying out-of-area patient '
                                                      'presents multiple early opioid requests '
                                                      'with inconsistent stories. Avoid '
                                                      'harmful premature treatment while '
                                                      'catastrophic differentials remain open.',
                                              'question': 'Response concept?',
                                              'answer': 'Professional vigilance for '
                                                        'diversion/misuse — verify, refuse '
                                                        'when appropriate, follow '
                                                        'controlled-drug and safeguarding '
                                                        'pathways.',
                                              'discussion': 'Patient care + legal duties.',
                                              'book_hint': 'Community Pharmacy Practice texts '
                                                           '/ RPS guidance themes'}]}},
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
                                                           'B) Reduce medication errors and '
                                                           'waste',
                                                           'C) Eliminate pharmacist review of '
                                                           'orders',
                                                           'D) Replace all oral meds with IV '
                                                           'formulations'],
                                               'answer': 'B) Reduce medication errors and '
                                                         'waste',
                                               'explanation': 'Unit-dose distribution '
                                                              'dispenses individually '
                                                              'packaged, ready-to-administer '
                                                              'doses labeled for a specific '
                                                              'patient and administration '
                                                              'time. This reduces ward stock '
                                                              'manipulation, wrong-dose '
                                                              'selection, and wastage from '
                                                              'unused multidose supplies. The '
                                                              'system supports nurse '
                                                              'verification against the '
                                                              'medication administration '
                                                              'record.',
                                               'choice_explanations': {'A': 'Increasing ward '
                                                                            'multidose '
                                                                            'stockpiles raises '
                                                                            'selection error '
                                                                            'and waste '
                                                                            'risk—the opposite '
                                                                            'of unit-dose '
                                                                            'aims.',
                                                                       'B': 'Unit-dose systems '
                                                                            'dispense '
                                                                            'individually '
                                                                            'packaged, '
                                                                            'patient- and '
                                                                            'time-specific '
                                                                            'doses, reducing '
                                                                            'selection errors, '
                                                                            'ward stock '
                                                                            'diversion/waste, '
                                                                            'and improving '
                                                                            'control.',
                                                                       'C': 'Eliminating '
                                                                            'pharmacist review '
                                                                            'removes a '
                                                                            'critical safety '
                                                                            'check that '
                                                                            'unit-dose '
                                                                            'workflows still '
                                                                            'rely on for order '
                                                                            'verification.',
                                                                       'D': 'Replacing all '
                                                                            'oral meds with IV '
                                                                            'formulations '
                                                                            'increases '
                                                                            'infection/cost '
                                                                            'risk and is '
                                                                            'unrelated to '
                                                                            'unit-dose '
                                                                            'packaging '
                                                                            'goals.'}},
                                              {'question': 'IV admixture service focuses on?',
                                               'options': ['A) Only outpatient OTC counseling',
                                                           'B) Only tablet repackaging into '
                                                           'bottles',
                                                           'C) Aseptic compounding of '
                                                           'injectable preparations',
                                                           'D) Only narcotic vault inventory '
                                                           'counting'],
                                               'answer': 'C) Aseptic compounding of injectable '
                                                         'preparations',
                                               'explanation': 'An IV admixture service '
                                                              'compounds sterile parenteral '
                                                              'preparations under controlled '
                                                              'aseptic conditions, verifying '
                                                              'calculations, diluents, and '
                                                              'compatibility. The aim is to '
                                                              'prevent microbial contamination '
                                                              'and particulate or chemical '
                                                              'incompatibility in intravenous '
                                                              'medicines. Centralized aseptic '
                                                              'compounding also standardizes '
                                                              'labeling and beyond-use dating.',
                                               'choice_explanations': {'A': 'Outpatient OTC '
                                                                            'counseling is '
                                                                            'community/ambulatory '
                                                                            'education, not '
                                                                            'sterile '
                                                                            'injectable '
                                                                            'compounding.',
                                                                       'B': 'Tablet bottle '
                                                                            'repackaging is '
                                                                            'oral solid '
                                                                            'handling, not '
                                                                            'aseptic IV '
                                                                            'admixture.',
                                                                       'C': 'IV admixture '
                                                                            'services '
                                                                            'aseptically '
                                                                            'compound '
                                                                            'injectable '
                                                                            'preparations '
                                                                            'under controlled '
                                                                            'conditions, '
                                                                            'verifying '
                                                                            'calculations, '
                                                                            'diluents, '
                                                                            'compatibility, '
                                                                            'and beyond-use '
                                                                            'dating.',
                                                                       'D': 'Narcotic vault '
                                                                            'counting is '
                                                                            'controlled-drug '
                                                                            'inventory '
                                                                            'control, not the '
                                                                            'focus of sterile '
                                                                            'admixture '
                                                                            'compounding.'}},
                                              {'question': 'Formulary manages?',
                                               'options': ['A) Nurse staffing ratios on '
                                                           'medical wards',
                                                           'B) Operating-room surgical '
                                                           'instrument trays',
                                                           'C) Ambulance response time targets',
                                                           'D) Which medicines are stocked and '
                                                           'approved for use'],
                                               'answer': 'D) Which medicines are stocked and '
                                                         'approved for use',
                                               'explanation': 'A formulary is the '
                                                              "institution's approved list of "
                                                              'medicines selected for '
                                                              'efficacy, safety, and '
                                                              'cost-effectiveness relative to '
                                                              'therapeutic alternatives. '
                                                              'Pharmacy and therapeutics '
                                                              'processes evaluate evidence and '
                                                              'restrict nonformulary use. '
                                                              'Formulary management shapes '
                                                              'prescribing patterns and '
                                                              'inventory control in the '
                                                              'hospital.',
                                               'choice_explanations': {'A': 'Nurse staffing '
                                                                            'ratios are '
                                                                            'workforce '
                                                                            'management, not '
                                                                            'medicine '
                                                                            'selection policy.',
                                                                       'B': 'Surgical '
                                                                            'instrument trays '
                                                                            'are '
                                                                            'operating-room '
                                                                            'logistics, '
                                                                            'outside pharmacy '
                                                                            'formulary scope.',
                                                                       'C': 'Ambulance '
                                                                            'response times '
                                                                            'are '
                                                                            'emergency-system '
                                                                            'metrics, not '
                                                                            'formulary '
                                                                            'content.',
                                                                       'D': 'A formulary is '
                                                                            "the institution's "
                                                                            'approved medicine '
                                                                            'list chosen for '
                                                                            'efficacy, safety, '
                                                                            'and '
                                                                            'cost-effectiveness, '
                                                                            'guiding which '
                                                                            'drugs are stocked '
                                                                            'and used.'}}],
                                     'medium': [{'question': 'TPN compounding requires?',
                                                 'options': ['A) Aseptic technique plus '
                                                             'stability and compatibility '
                                                             'checks',
                                                             'B) Open-bench mixing without '
                                                             'sterility controls',
                                                             'C) Ignoring calcium–phosphate '
                                                             'precipitation risk',
                                                             'D) Adding all vitamins before '
                                                             'autoclaving the bag'],
                                                 'answer': 'A) Aseptic technique plus '
                                                           'stability and compatibility checks',
                                                 'explanation': 'Total parenteral nutrition '
                                                                'admixtures combine amino '
                                                                'acids, dextrose, lipid '
                                                                'emulsions, electrolytes, '
                                                                'vitamins, and trace elements '
                                                                'in complex physicochemical '
                                                                'systems. Aseptic technique '
                                                                'prevents bloodstream '
                                                                'infection, while '
                                                                'compatibility and stability '
                                                                'checks avoid precipitation '
                                                                '(for example '
                                                                'calcium–phosphate) and '
                                                                'emulsion cracking. Order '
                                                                'review must also match '
                                                                'nutrient provision to '
                                                                'metabolic status.',
                                                 'choice_explanations': {'A': 'TPN combines '
                                                                              'amino acids, '
                                                                              'dextrose, '
                                                                              'lipids, '
                                                                              'electrolytes, '
                                                                              'vitamins, and '
                                                                              'trace elements; '
                                                                              'aseptic '
                                                                              'technique plus '
                                                                              'stability/compatibility '
                                                                              'checks (e.g., '
                                                                              'Ca–phosphate) '
                                                                              'prevent '
                                                                              'contamination '
                                                                              'and '
                                                                              'precipitation.',
                                                                         'B': 'Open-bench '
                                                                              'mixing without '
                                                                              'sterility '
                                                                              'controls risks '
                                                                              'microbial '
                                                                              'contamination '
                                                                              'of '
                                                                              'high-nutrient '
                                                                              'admixtures '
                                                                              'infused '
                                                                              'intravenously.',
                                                                         'C': 'Ignoring '
                                                                              'calcium–phosphate '
                                                                              'precipitation '
                                                                              'risk can form '
                                                                              'embolic '
                                                                              'precipitates in '
                                                                              'the bag/line.',
                                                                         'D': 'Autoclaving a '
                                                                              'finished TPN '
                                                                              'bag would '
                                                                              'degrade '
                                                                              'heat-labile '
                                                                              'vitamins/components '
                                                                              'and is not '
                                                                              'standard '
                                                                              'admixture '
                                                                              'practice; '
                                                                              'aseptic '
                                                                              'compounding is '
                                                                              'used instead.'}},
                                                {'question': 'Antimicrobial stewardship rounds '
                                                             'include pharmacists to?',
                                                 'options': ['A) Increase duration of every '
                                                             'empiric regimen',
                                                             'B) Optimize antimicrobial '
                                                             'choice, dose, and duration',
                                                             'C) Stop all cultures before '
                                                             'reviewing therapy',
                                                             'D) Switch all patients to the '
                                                             'broadest IV agent'],
                                                 'answer': 'B) Optimize antimicrobial choice, '
                                                           'dose, and duration',
                                                 'explanation': 'Antimicrobial stewardship '
                                                                'rounds use multidisciplinary '
                                                                'review to optimize drug '
                                                                'choice, dose, route, and '
                                                                'duration against culture data '
                                                                'and infection syndromes. '
                                                                'Pharmacists contribute '
                                                                'pharmacokinetic dosing, '
                                                                'IV-to-oral switch, and '
                                                                'de-escalation expertise. The '
                                                                'goals are improved clinical '
                                                                'outcomes and reduced '
                                                                'selection pressure for '
                                                                'antimicrobial resistance.',
                                                 'choice_explanations': {'A': 'Lengthening '
                                                                              'every empiric '
                                                                              'regimen '
                                                                              'increases '
                                                                              'resistance '
                                                                              'selection and '
                                                                              'toxicity '
                                                                              'without '
                                                                              'culture-driven '
                                                                              'de-escalation.',
                                                                         'B': 'Stewardship '
                                                                              'rounds optimize '
                                                                              'antimicrobial '
                                                                              'choice, dose, '
                                                                              'route, and '
                                                                              'duration '
                                                                              'against '
                                                                              'infection '
                                                                              'syndrome and '
                                                                              'microbiology to '
                                                                              'maximize cure '
                                                                              'and minimize '
                                                                              'resistance/toxicity.',
                                                                         'C': 'Stopping all '
                                                                              'cultures '
                                                                              'removes '
                                                                              'diagnostic data '
                                                                              'needed to '
                                                                              'narrow therapy '
                                                                              'safely.',
                                                                         'D': 'Defaulting all '
                                                                              'patients to the '
                                                                              'broadest IV '
                                                                              'agent maximizes '
                                                                              'collateral '
                                                                              'damage and '
                                                                              'resistance '
                                                                              'pressure.'}},
                                                {'question': 'Medication error disclosure '
                                                             'ethics?',
                                                 'options': ['A) Conceal errors to protect '
                                                             'institutional reputation',
                                                             'B) Blame only the most junior '
                                                             'staff member publicly',
                                                             'C) Be honest with patient and '
                                                             'team per policy',
                                                             'D) Alter charts so the error '
                                                             'cannot be traced'],
                                                 'answer': 'C) Be honest with patient and team '
                                                           'per policy',
                                                 'explanation': 'Ethical medication-error '
                                                                'disclosure requires honest '
                                                                'communication with the '
                                                                'patient and care team '
                                                                'according to institutional '
                                                                'policy once an error is '
                                                                'recognized. Transparency '
                                                                'enables timely clinical '
                                                                'mitigation and supports '
                                                                'learning systems rather than '
                                                                'individual blame alone. '
                                                                'Concealing errors undermines '
                                                                'autonomy, safety improvement, '
                                                                'and professional trust.',
                                                 'choice_explanations': {'A': 'Concealing '
                                                                              'errors blocks '
                                                                              'patient '
                                                                              'autonomy, '
                                                                              'learning, and '
                                                                              'timely harm '
                                                                              'mitigation.',
                                                                         'B': 'Publicly '
                                                                              'blaming only '
                                                                              'junior staff '
                                                                              'ignores system '
                                                                              'factors and '
                                                                              'violates '
                                                                              'just-culture '
                                                                              'ethics.',
                                                                         'C': 'Ethical '
                                                                              'disclosure '
                                                                              'requires honest '
                                                                              'communication '
                                                                              'with the '
                                                                              'patient and '
                                                                              'care team per '
                                                                              'institutional '
                                                                              'policy once an '
                                                                              'error is '
                                                                              'recognized, '
                                                                              'enabling '
                                                                              'monitoring and '
                                                                              'remediation.',
                                                                         'D': 'Altering charts '
                                                                              'is '
                                                                              'falsification '
                                                                              'that destroys '
                                                                              'the clinical '
                                                                              'record and '
                                                                              'legal '
                                                                              'accountability.'}}],
                                     'hard': [{'question': 'Clean room grades/air quality '
                                                           'matter for?',
                                               'options': ['A) Only outpatient waiting-room '
                                                           'comfort',
                                                           'B) Only tablet bottle labeling '
                                                           'speed',
                                                           'C) Only courier delivery '
                                                           'temperature logs',
                                                           'D) Aseptic preparation '
                                                           'contamination risk control'],
                                               'answer': 'D) Aseptic preparation contamination '
                                                         'risk control',
                                               'explanation': 'Cleanroom grade classifications '
                                                              'specify airborne particulate '
                                                              'limits and air-handling '
                                                              'performance for aseptic '
                                                              'preparation areas. Higher-grade '
                                                              'environments (with HEPA '
                                                              'filtration and pressure '
                                                              'cascades) reduce contamination '
                                                              'risk during sterile '
                                                              'compounding. Environmental '
                                                              'monitoring and gowning '
                                                              'discipline translate these '
                                                              'engineering controls into '
                                                              'microbial risk reduction for '
                                                              'parenteral products.',
                                               'choice_explanations': {'A': 'Waiting-room '
                                                                            'comfort HVAC is '
                                                                            'not classified '
                                                                            'cleanroom '
                                                                            'particulate '
                                                                            'control for '
                                                                            'aseptic prep.',
                                                                       'B': 'Labeling speed of '
                                                                            'tablet bottles is '
                                                                            'operational '
                                                                            'throughput, not '
                                                                            'air-quality grade '
                                                                            'for sterility '
                                                                            'assurance.',
                                                                       'C': 'Courier '
                                                                            'temperature logs '
                                                                            'monitor '
                                                                            'distribution cold '
                                                                            'chain, not '
                                                                            'cleanroom grade '
                                                                            'for compounding.',
                                                                       'D': 'Cleanroom grades '
                                                                            'specify airborne '
                                                                            'particulate/microbial '
                                                                            'limits and air '
                                                                            'handling so '
                                                                            'aseptic '
                                                                            'preparation '
                                                                            'contamination '
                                                                            'risk stays within '
                                                                            'validated '
                                                                            'sterility '
                                                                            'assurance.'}},
                                              {'question': 'Smart pump libraries reduce?',
                                               'options': ['A) Infusion programming and '
                                                           'dosing-limit errors',
                                                           'B) Need for any drug concentration '
                                                           'standardization',
                                                           'C) Pharmacist verification of '
                                                           'high-alert infusions',
                                                           'D) Use of soft and hard dose '
                                                           'alerts entirely'],
                                               'answer': 'A) Infusion programming and '
                                                         'dosing-limit errors',
                                               'explanation': 'Smart-pump drug libraries '
                                                              'encode standardized '
                                                              'concentrations, dosing units, '
                                                              'and soft/hard limits for '
                                                              'intravenous infusions. When '
                                                              'clinicians select a library '
                                                              'entry, the pump constrains '
                                                              'programming that would '
                                                              'otherwise allow 10-fold '
                                                              'overdoses or unit mismatches. '
                                                              'Technology thus reduces '
                                                              'infusion programming errors '
                                                              'when libraries are current and '
                                                              'used.',
                                               'choice_explanations': {'A': 'Smart-pump '
                                                                            'libraries encode '
                                                                            'standard '
                                                                            'concentrations, '
                                                                            'units, and '
                                                                            'soft/hard limits '
                                                                            'that intercept '
                                                                            'programming and '
                                                                            'dose-limit errors '
                                                                            'during IV '
                                                                            'infusion setup.',
                                                                       'B': 'Libraries work '
                                                                            'with—not '
                                                                            'replace—concentration '
                                                                            'standardization; '
                                                                            'eliminating '
                                                                            'standardization '
                                                                            'increases '
                                                                            'programming '
                                                                            'complexity and '
                                                                            'error.',
                                                                       'C': 'High-alert '
                                                                            'infusions still '
                                                                            'need pharmacist '
                                                                            'verification; '
                                                                            'pumps do not '
                                                                            'remove clinical '
                                                                            'double-checks.',
                                                                       'D': 'Soft/hard alerts '
                                                                            'are core library '
                                                                            'safety features; '
                                                                            'eliminating them '
                                                                            'removes the '
                                                                            'dosing-error '
                                                                            'interception '
                                                                            'mechanism.'}},
                                              {'question': 'Recall management requires?',
                                               'options': ['A) Continuing to dispense recalled '
                                                           'batches until empty',
                                                           'B) Quarantine affected batches and '
                                                           'trace patients if needed',
                                                           'C) Relabeling recalled stock with '
                                                           'a new expiry only',
                                                           'D) Ignoring supplier notices for '
                                                           'slow-moving items'],
                                               'answer': 'B) Quarantine affected batches and '
                                                         'trace patients if needed',
                                               'explanation': 'Medicine recalls remove or '
                                                              'restrict batches with quality '
                                                              'defects, contamination, or '
                                                              'safety signals. Hospital '
                                                              'pharmacy must quarantine '
                                                              'affected stock, stop further '
                                                              'dispensing, and trace patients '
                                                              'who already received implicated '
                                                              'packs when clinical risk '
                                                              'warrants. Timely quarantine and '
                                                              'communication are operational '
                                                              'pharmacovigilance duties.',
                                               'choice_explanations': {'A': 'Continuing to '
                                                                            'dispense recalled '
                                                                            'batches exposes '
                                                                            'patients to '
                                                                            'defective/contaminated/unsafe '
                                                                            'product.',
                                                                       'B': 'Recall management '
                                                                            'quarantines '
                                                                            'affected batches, '
                                                                            'stops further '
                                                                            'dispensing, and '
                                                                            'traces patients '
                                                                            'who received '
                                                                            'product when '
                                                                            'clinical '
                                                                            'follow-up is '
                                                                            'needed.',
                                                                       'C': 'Relabeling with a '
                                                                            'new expiry '
                                                                            'without '
                                                                            'addressing the '
                                                                            'defect falsifies '
                                                                            'quality status '
                                                                            'and does not '
                                                                            'remediate the '
                                                                            'recall cause.',
                                                                       'D': 'Ignoring supplier '
                                                                            'notices for slow '
                                                                            'movers leaves '
                                                                            'defective stock '
                                                                            'available for '
                                                                            'future '
                                                                            'dispensing.'}}],
                                     'extreme': [{'question': 'Intrathecal vincristine error '
                                                              'prevention?',
                                                  'options': ['A) Prepare vincristine in the '
                                                              'same syringe style as IT meds',
                                                              'B) Deliver IV vinca to the '
                                                              'theatre IT tray routinely',
                                                              'C) Never manage IV vinca like '
                                                              'IT medicines; use systemic '
                                                              'safeguards',
                                                              'D) Allow ward nurses to '
                                                              'reconstitute vinca at bedside '
                                                              'for IT use'],
                                                  'answer': 'C) Never manage IV vinca like IT '
                                                            'medicines; use systemic '
                                                            'safeguards',
                                                  'explanation': 'Intrathecal vincristine is '
                                                                 'almost uniformly fatal '
                                                                 'because vinca alkaloids '
                                                                 'cause severe neurotoxicity '
                                                                 'when injected into the CSF. '
                                                                 'Prevention relies on '
                                                                 'systemic safeguards: '
                                                                 'distinct packaging, never '
                                                                 'dispensing IV vinca in '
                                                                 'intrathecal sets, timing '
                                                                 'separation, and independent '
                                                                 'checks. Treating intrathecal '
                                                                 'and intravenous cytotoxics '
                                                                 'as interchangeable workflows '
                                                                 'is a recognized never-event '
                                                                 'pathway.',
                                                  'choice_explanations': {'A': 'Preparing '
                                                                               'vincristine in '
                                                                               'IT-similar '
                                                                               'syringes '
                                                                               'increases '
                                                                               'look-alike '
                                                                               'wrong-route '
                                                                               'risk for fatal '
                                                                               'intrathecal '
                                                                               'administration.',
                                                                          'B': 'Delivering IV '
                                                                               'vinca onto the '
                                                                               'theatre IT '
                                                                               'tray colocates '
                                                                               'a fatal '
                                                                               'wrong-route '
                                                                               'hazard with '
                                                                               'intended '
                                                                               'intrathecal '
                                                                               'drugs.',
                                                                          'C': 'Intrathecal '
                                                                               'vincristine '
                                                                               'causes '
                                                                               'devastating '
                                                                               'neurotoxicity; '
                                                                               'safeguards '
                                                                               'keep IV vinca '
                                                                               'physically and '
                                                                               'procedurally '
                                                                               'distinct from '
                                                                               'IT medicines '
                                                                               '(e.g., '
                                                                               'minibag-only, '
                                                                               'separate '
                                                                               'delivery, '
                                                                               'never syringe '
                                                                               'for IT).',
                                                                          'D': 'Bedside '
                                                                               'reconstitution '
                                                                               'of vinca for '
                                                                               'purported IT '
                                                                               'use is an '
                                                                               'extreme '
                                                                               'wrong-route '
                                                                               'pathway and '
                                                                               'must never '
                                                                               'occur.'}},
                                                 {'question': 'Disaster formulary planning '
                                                              'includes?',
                                                  'options': ['A) Stocking only luxury '
                                                              'nonessential cosmetics',
                                                              'B) Eliminating cold-chain '
                                                              'contingency plans',
                                                              'C) Relying solely on '
                                                              'just-in-time wholesale with no '
                                                              'buffer',
                                                              'D) Critical medicines '
                                                              'continuity and cold-chain '
                                                              'contingency'],
                                                  'answer': 'D) Critical medicines continuity '
                                                            'and cold-chain contingency',
                                                  'explanation': 'Disaster formulary planning '
                                                                 'identifies critical '
                                                                 'medicines whose interruption '
                                                                 'would immediately threaten '
                                                                 'life or continuity of '
                                                                 'essential therapy, including '
                                                                 'cold-chain–dependent '
                                                                 'products. Contingency '
                                                                 'stocks, alternative agents, '
                                                                 'and backup refrigeration or '
                                                                 'generator plans maintain '
                                                                 'supply during emergencies. '
                                                                 'Resilience planning links '
                                                                 'inventory science to '
                                                                 'public-health surge needs.',
                                                  'choice_explanations': {'A': 'Luxury '
                                                                               'cosmetics are '
                                                                               'nonessential '
                                                                               'and do not '
                                                                               'sustain '
                                                                               'life-saving '
                                                                               'therapy '
                                                                               'continuity in '
                                                                               'disasters.',
                                                                          'B': 'Eliminating '
                                                                               'cold-chain '
                                                                               'contingency '
                                                                               'abandons '
                                                                               'temperature-sensitive '
                                                                               'critical '
                                                                               'medicines '
                                                                               '(insulin, '
                                                                               'vaccines, some '
                                                                               'biologics).',
                                                                          'C': 'Sole '
                                                                               'just-in-time '
                                                                               'wholesale '
                                                                               'without buffer '
                                                                               'fails when '
                                                                               'supply chains '
                                                                               'break during '
                                                                               'disasters.',
                                                                          'D': 'Disaster '
                                                                               'formulary '
                                                                               'planning '
                                                                               'prioritizes '
                                                                               'critical '
                                                                               'medicine '
                                                                               'continuity and '
                                                                               'cold-chain '
                                                                               'contingency so '
                                                                               'essential '
                                                                               'therapies '
                                                                               'remain '
                                                                               'available when '
                                                                               'logistics '
                                                                               'fail.'}},
                                                 {'question': 'Cytotoxic spill response?',
                                                  'options': ['A) Evacuate/protect, use spill '
                                                              'kit, report, follow '
                                                              'hazardous-drug protocol',
                                                              'B) Wipe with bare hands and '
                                                              'continue compounding',
                                                              'C) Hose the area into general '
                                                              'drains without PPE',
                                                              'D) Ignore small spills if they '
                                                              'dry quickly'],
                                                  'answer': 'A) Evacuate/protect, use spill '
                                                            'kit, report, follow '
                                                            'hazardous-drug protocol',
                                                  'explanation': 'Cytotoxic spills aerosolize '
                                                                 'or deposit hazardous drug '
                                                                 'residues that can cause '
                                                                 'occupational exposure '
                                                                 'through skin contact or '
                                                                 'inhalation. Response '
                                                                 'protocols evacuate '
                                                                 'unprotected staff, contain '
                                                                 'the spill with a dedicated '
                                                                 'kit, use appropriate PPE, '
                                                                 'and report the incident. '
                                                                 'Hazardous-drug policies '
                                                                 'define decontamination, '
                                                                 'waste disposal, and medical '
                                                                 'follow-up.',
                                                  'choice_explanations': {'A': 'Cytotoxic '
                                                                               'spill response '
                                                                               'evacuates/protects '
                                                                               'personnel, '
                                                                               'uses '
                                                                               'designated '
                                                                               'spill kits '
                                                                               'with PPE, '
                                                                               'reports the '
                                                                               'event, and '
                                                                               'follows '
                                                                               'hazardous-drug '
                                                                               'decontamination '
                                                                               'protocols to '
                                                                               'limit '
                                                                               'occupational '
                                                                               'exposure.',
                                                                          'B': 'Wiping with '
                                                                               'bare hands '
                                                                               'causes dermal '
                                                                               'absorption of '
                                                                               'hazardous drug '
                                                                               'residues.',
                                                                          'C': 'Hosing into '
                                                                               'general drains '
                                                                               'without PPE '
                                                                               'spreads '
                                                                               'contamination '
                                                                               'and creates '
                                                                               'environmental/occupational '
                                                                               'exposure.',
                                                                          'D': 'Ignoring small '
                                                                               'spills leaves '
                                                                               'persistent '
                                                                               'cytotoxic '
                                                                               'residues that '
                                                                               'continue to '
                                                                               'expose '
                                                                               'staff.'}}]},
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
                                                     'despite sensitivities allowing narrow '
                                                     'agent.',
                                             'question': 'Pharmacy action?',
                                             'answer': 'Recommend de-escalation with team.',
                                             'discussion': 'Stewardship in action.',
                                             'book_hint': 'Hospital Pharmacy practice / ASHP '
                                                          'themes'}],
                                 'hard': [{'title': 'Batch Recall Mid-Shift',
                                           'stem': 'Urgent recall for a contaminated '
                                                   'injectable batch currently on wards. '
                                                   'Choose the safest high-yield next concept '
                                                   'before definitive results.',
                                           'question': 'Steps?',
                                           'answer': 'Stop use, quarantine, identify exposed '
                                                     'patients, coordinate clinical follow-up, '
                                                     'document.',
                                           'discussion': 'Speed + traceability.',
                                           'book_hint': 'Hospital Pharmacy practice / ASHP '
                                                        'themes'}],
                                 'extreme': [{'title': 'Vinca Near Intrathecal Tray',
                                              'stem': 'A vinca alkaloid syringe is found '
                                                      'placed with intrathecal medications. '
                                                      'Avoid harmful premature treatment while '
                                                      'catastrophic differentials remain open.',
                                              'question': 'Immediate actions?',
                                              'answer': 'Do not administer; quarantine; '
                                                        'root-cause; enforce never-event '
                                                        'barriers (different delivery '
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
                                        'answer': 'C) Opioid toxicity with respiratory '
                                                  'depression',
                                        'explanation': 'Naloxone is a competitive antagonist '
                                                       'at μ-opioid receptors and rapidly '
                                                       'reverses opioid-induced respiratory '
                                                       'depression and sedation. Because many '
                                                       "opioids outlast naloxone's effect, "
                                                       'repeated dosing or infusion may be '
                                                       'required. Supportive airway and '
                                                       'ventilation care remain foundational '
                                                       'while antagonism restores respiratory '
                                                       'drive.',
                                        'choice_explanations': {'A': 'Benzodiazepine sedation '
                                                                     'is reversed by '
                                                                     'flumazenil at the GABA-A '
                                                                     'benzodiazepine site, not '
                                                                     'by naloxone at opioid '
                                                                     'receptors.',
                                                                'B': 'Paracetamol '
                                                                     'hepatotoxicity is '
                                                                     'treated with '
                                                                     'N-acetylcysteine to '
                                                                     'replenish glutathione '
                                                                     'against NAPQI, not with '
                                                                     'opioid-receptor '
                                                                     'antagonism.',
                                                                'C': 'Naloxone is a '
                                                                     'competitive μ-opioid '
                                                                     'receptor antagonist that '
                                                                     'rapidly reverses '
                                                                     'opioid-induced '
                                                                     'respiratory depression '
                                                                     'and sedation.',
                                                                'D': 'Organophosphate '
                                                                     'cholinergic crisis is '
                                                                     'managed with atropine '
                                                                     'and pralidoxime (AChE '
                                                                     'regeneration), not '
                                                                     'naloxone.'}},
                                       {'question': 'Activated charcoal useful when?',
                                        'options': ['A) Iron overdose as first-line binder '
                                                    'always',
                                                    'B) Lithium ingestion where adsorption is '
                                                    'reliable',
                                                    'C) Corrosive alkali ingestion to '
                                                    'neutralize pH',
                                                    'D) Selected recent ingestions if the '
                                                    'airway is protected'],
                                        'answer': 'D) Selected recent ingestions if the airway '
                                                  'is protected',
                                        'explanation': 'Activated charcoal adsorbs many toxins '
                                                       'in the gut, reducing systemic '
                                                       'absorption if given soon after '
                                                       'ingestion when the airway is '
                                                       'protected. It is ineffective for '
                                                       'alcohols, metals, and corrosives and '
                                                       'is contraindicated when aspiration '
                                                       'risk is high or bowel integrity is '
                                                       'compromised. Benefit depends on '
                                                       'timing, charcoal–toxin binding, and '
                                                       'clinical stability.',
                                        'choice_explanations': {'A': 'Iron binds poorly to '
                                                                     'activated charcoal; '
                                                                     'whole-bowel '
                                                                     'irrigation/chelation '
                                                                     'strategies are used '
                                                                     'instead for significant '
                                                                     'iron overdose.',
                                                                'B': 'Lithium is a small '
                                                                     'hydrophilic ion with '
                                                                     'poor charcoal '
                                                                     'adsorption, so charcoal '
                                                                     'is not reliable '
                                                                     'decontamination for '
                                                                     'lithium.',
                                                                'C': 'Corrosive alkali '
                                                                     'ingestion damages '
                                                                     'mucosa; charcoal does '
                                                                     'not neutralize pH and '
                                                                     'can obscure '
                                                                     'endoscopy—contraindicated.',
                                                                'D': 'Activated charcoal '
                                                                     'adsorbs many organic '
                                                                     'toxins in the gut if '
                                                                     'given promptly when the '
                                                                     'airway is protected, '
                                                                     'reducing systemic '
                                                                     'absorption for selected '
                                                                     'ingestions.'}},
                                       {'question': 'ABC approach in poisoning means?',
                                        'options': ['A) Airway, Breathing, Circulation '
                                                    'prioritized first',
                                                    'B) Antidote before any supportive care '
                                                    'always',
                                                    'C) Arterial blood gas as the only '
                                                    'assessment',
                                                    'D) Activated charcoal for every '
                                                    'unconscious patient'],
                                        'answer': 'A) Airway, Breathing, Circulation '
                                                  'prioritized first',
                                        'explanation': 'In acute poisoning, the ABC approach '
                                                       'prioritizes airway patency, adequate '
                                                       'breathing/ventilation, and circulatory '
                                                       'support before toxin-specific '
                                                       'antidotes. Hypoxia, hypoventilation, '
                                                       'and shock cause immediate death '
                                                       'independent of the intoxicant. '
                                                       'Stabilization creates the physiologic '
                                                       'window in which decontamination and '
                                                       'antidotes can work.',
                                        'choice_explanations': {'A': 'In poisoning, airway '
                                                                     'patency, '
                                                                     'ventilation/oxygenation, '
                                                                     'and circulatory support '
                                                                     'are prioritized because '
                                                                     'hypoxia and shock kill '
                                                                     'faster than delayed '
                                                                     'antidote delivery.',
                                                                'B': 'Giving antidote before '
                                                                     'any supportive care can '
                                                                     'leave an unprotected '
                                                                     'airway or inadequate '
                                                                     'perfusion unaddressed; '
                                                                     'ABCs come first.',
                                                                'C': 'ABG is useful for '
                                                                     'acid–base/ventilation '
                                                                     'assessment but is not '
                                                                     'the exclusive initial '
                                                                     'priority over airway and '
                                                                     'circulation.',
                                                                'D': 'Charcoal in every '
                                                                     'unconscious patient '
                                                                     'risks aspiration unless '
                                                                     'the airway is secured; '
                                                                     'it is not universal ABC '
                                                                     'care.'}}],
                              'medium': [{'question': 'Paracetamol toxicity antidote?',
                                          'options': ['A) Flumazenil as routine first-line '
                                                      'therapy',
                                                      'B) N-acetylcysteine to replenish '
                                                      'glutathione defenses',
                                                      'C) Naloxone infusion for hepatocyte '
                                                      'protection',
                                                      'D) Deferoxamine chelation of NAPQI'],
                                          'answer': 'B) N-acetylcysteine to replenish '
                                                    'glutathione defenses',
                                          'explanation': 'In paracetamol overdose, a fraction '
                                                         'of the drug is oxidized by CYP2E1 to '
                                                         'NAPQI, which depletes hepatic '
                                                         'glutathione and binds hepatocyte '
                                                         'proteins. N-acetylcysteine '
                                                         'replenishes glutathione and improves '
                                                         'NAPQI detoxification, preventing or '
                                                         'limiting centrilobular necrosis. '
                                                         'Efficacy is greatest when started '
                                                         'early after significant overdose '
                                                         'according to nomogram-guided risk '
                                                         'assessment.',
                                          'choice_explanations': {'A': 'Flumazenil reverses '
                                                                       'benzodiazepines at '
                                                                       'GABA-A; it does not '
                                                                       'detoxify NAPQI or '
                                                                       'restore hepatic '
                                                                       'glutathione in '
                                                                       'paracetamol overdose.',
                                                                  'B': 'N-acetylcysteine '
                                                                       'replenishes '
                                                                       'glutathione and '
                                                                       'enhances nontoxic '
                                                                       'paracetamol '
                                                                       'metabolism, '
                                                                       'detoxifying NAPQI '
                                                                       'formed via CYP2E1 '
                                                                       'oxidation after '
                                                                       'overdose.',
                                                                  'C': 'Naloxone antagonizes '
                                                                       'opioids; it does not '
                                                                       'protect hepatocytes '
                                                                       'from NAPQI binding.',
                                                                  'D': 'Deferoxamine chelates '
                                                                       'iron; it does not '
                                                                       'chelate NAPQI in '
                                                                       'paracetamol '
                                                                       'toxicity.'}},
                                         {'question': 'Methanol toxicity visual threat treated '
                                                      'with?',
                                          'options': ['A) Physostigmine to increase '
                                                      'acetylcholine',
                                                      'B) Naloxone to reverse optic nerve '
                                                      'effects',
                                                      'C) Fomepizole or ethanol, with dialysis '
                                                      'when indicated',
                                                      'D) Atropine as the primary antidote '
                                                      'always'],
                                          'answer': 'C) Fomepizole or ethanol, with dialysis '
                                                    'when indicated',
                                          'explanation': 'Methanol is metabolized by alcohol '
                                                         'dehydrogenase to formaldehyde and '
                                                         'then to formic acid, which causes '
                                                         'metabolic acidosis and optic nerve '
                                                         'injury. Fomepizole or ethanol '
                                                         'competitively inhibit alcohol '
                                                         'dehydrogenase, blocking formation of '
                                                         'toxic metabolites. Hemodialysis '
                                                         'removes methanol and formate when '
                                                         'acidosis or high levels indicate '
                                                         'extracorporeal elimination.',
                                          'choice_explanations': {'A': 'Physostigmine '
                                                                       'increases '
                                                                       'acetylcholine and is '
                                                                       'used in selected '
                                                                       'anticholinergic '
                                                                       'delirium, not '
                                                                       'methanol’s formate '
                                                                       'optic toxicity.',
                                                                  'B': 'Naloxone does not '
                                                                       'reverse '
                                                                       'formate-mediated optic '
                                                                       'nerve injury from '
                                                                       'methanol metabolism.',
                                                                  'C': 'Alcohol dehydrogenase '
                                                                       'converts methanol to '
                                                                       'formaldehyde/formic '
                                                                       'acid causing acidosis '
                                                                       'and optic injury; '
                                                                       'fomepizole or ethanol '
                                                                       'block ADH, with '
                                                                       'hemodialysis for '
                                                                       'severe '
                                                                       'toxicity/formate '
                                                                       'clearance.',
                                                                  'D': 'Atropine treats '
                                                                       'cholinergic excess; it '
                                                                       'is not the primary '
                                                                       'antidote for '
                                                                       'methanol.'}},
                                         {'question': 'Tricyclic antidepressant overdose ECG '
                                                      'clue?',
                                          'options': ['A) Shortened PR interval as the '
                                                      'hallmark',
                                                      'B) Peaked T waves from hyperkalemia '
                                                      'only',
                                                      'C) Isolated sinus bradycardia without '
                                                      'QRS change',
                                                      'D) Wide QRS reflecting sodium-channel '
                                                      'blockade'],
                                          'answer': 'D) Wide QRS reflecting sodium-channel '
                                                    'blockade',
                                          'explanation': 'Tricyclic antidepressants block '
                                                         'cardiac fast sodium channels, '
                                                         'slowing phase-0 depolarization and '
                                                         'widening the QRS complex on ECG. '
                                                         'Sodium channel blockade promotes '
                                                         'ventricular arrhythmias and seizures '
                                                         'in severe overdose. Intravenous '
                                                         'sodium bicarbonate provides sodium '
                                                         'loading and alkalinization that '
                                                         'partially overcome channel block and '
                                                         'stabilize the membrane.',
                                          'choice_explanations': {'A': 'Shortened PR interval '
                                                                       'is not the TCA '
                                                                       'overdose ECG hallmark; '
                                                                       'sodium-channel '
                                                                       'blockade widens QRS.',
                                                                  'B': 'Peaked T waves suggest '
                                                                       'hyperkalemia (e.g., '
                                                                       'digoxin or renal '
                                                                       'failure contexts), not '
                                                                       'the primary TCA '
                                                                       'membrane-stabilizing '
                                                                       'ECG clue.',
                                                                  'C': 'Isolated sinus '
                                                                       'bradycardia without '
                                                                       'QRS widening is '
                                                                       'atypical; TCAs more '
                                                                       'characteristically '
                                                                       'slow phase-0 '
                                                                       'depolarization and '
                                                                       'widen QRS.',
                                                                  'D': 'TCAs block cardiac '
                                                                       'fast Na+ channels, '
                                                                       'slowing phase-0 '
                                                                       'upstroke, widening '
                                                                       'QRS, and promoting '
                                                                       'ventricular '
                                                                       'arrhythmias—the key '
                                                                       'ECG toxicity clue.'}}],
                              'hard': [{'question': 'Physostigmine sometimes considered in?',
                                        'options': ['A) Severe anticholinergic delirium in '
                                                    'selected cases',
                                                    'B) TCA overdose with wide-complex '
                                                    'arrhythmias as first-line',
                                                    'C) Organophosphate poisoning instead of '
                                                    'atropine',
                                                    'D) Opioid coma when naloxone is '
                                                    'unavailable'],
                                        'answer': 'A) Severe anticholinergic delirium in '
                                                  'selected cases',
                                        'explanation': 'Physostigmine is a reversible '
                                                       'acetylcholinesterase inhibitor that '
                                                       'increases synaptic acetylcholine and '
                                                       'can temporarily reverse central '
                                                       'anticholinergic delirium from agents '
                                                       'such as atropine or certain '
                                                       'antihistamines. It crosses the '
                                                       'blood–brain barrier unlike '
                                                       'neostigmine. Use is reserved for '
                                                       'selected severe cases because '
                                                       'bradycardia, seizures, and cholinergic '
                                                       'excess are risks, especially with '
                                                       'tricyclic co-ingestion.',
                                        'choice_explanations': {'A': 'Physostigmine, a '
                                                                     'reversible AChE '
                                                                     'inhibitor, can '
                                                                     'temporarily reverse '
                                                                     'central anticholinergic '
                                                                     'delirium in selected, '
                                                                     'carefully monitored '
                                                                     'cases by raising '
                                                                     'synaptic acetylcholine.',
                                                                'B': 'In TCA overdose with '
                                                                     'wide-complex '
                                                                     'arrhythmias, '
                                                                     'physostigmine can worsen '
                                                                     'conduction block; sodium '
                                                                     'bicarbonate is preferred '
                                                                     'for Na-channel toxicity.',
                                                                'C': 'Organophosphate '
                                                                     'poisoning already has '
                                                                     'excess acetylcholine; '
                                                                     'atropine/oximes are '
                                                                     'used—physostigmine would '
                                                                     'worsen cholinergic '
                                                                     'crisis.',
                                                                'D': 'Opioid coma is reversed '
                                                                     'at opioid receptors with '
                                                                     'naloxone; physostigmine '
                                                                     'does not antagonize '
                                                                     'μ-opioid effects.'}},
                                       {'question': 'Hydrofluoric acid burn systemic risk?',
                                        'options': ['A) Hypernatremia from fluoride absorption',
                                                    'B) Hypocalcemia from fluoride binding '
                                                    'cations',
                                                    'C) Isolated hyperkalemia without calcium '
                                                    'shifts',
                                                    'D) Methemoglobinemia as the dominant '
                                                    'effect'],
                                        'answer': 'B) Hypocalcemia from fluoride binding '
                                                  'cations',
                                        'explanation': 'Hydrofluoric acid penetrates tissue '
                                                       'and avidly binds cations, depleting '
                                                       'ionized calcium and magnesium and '
                                                       'disrupting cellular metabolism. '
                                                       'Systemic hypocalcemia can trigger '
                                                       'tetany, QT prolongation, and '
                                                       'life-threatening arrhythmias after '
                                                       'significant burns or inhalational '
                                                       'exposure. Local and systemic calcium '
                                                       'therapy is used to chelate fluoride '
                                                       'and restore calcium homeostasis.',
                                        'choice_explanations': {'A': 'Fluoride from HF does '
                                                                     'not primarily cause '
                                                                     'hypernatremia; it binds '
                                                                     'Ca2+/Mg2+ and disrupts '
                                                                     'cellular ion '
                                                                     'homeostasis.',
                                                                'B': 'HF penetrates tissue and '
                                                                     'avidly binds cations, '
                                                                     'depleting ionized '
                                                                     'calcium (and magnesium), '
                                                                     'producing local injury '
                                                                     'and systemic '
                                                                     'hypocalcemia with '
                                                                     'cardiac risk.',
                                                                'C': 'Although potassium '
                                                                     'shifts can occur, '
                                                                     'isolated hyperkalemia '
                                                                     'without calcium binding '
                                                                     'is not the dominant '
                                                                     'systemic HF mechanism '
                                                                     'emphasized clinically.',
                                                                'D': 'Methemoglobinemia (Fe3+ '
                                                                     'hemoglobin) is classic '
                                                                     'for oxidants like '
                                                                     'nitrites/aniline, not HF '
                                                                     'cation chelation.'}},
                                       {'question': 'Body packer rupture risk management?',
                                        'options': ['A) Routine endoscopy to retrieve all '
                                                    'packets immediately',
                                                    'B) Discharge home after one dose of '
                                                    'charcoal',
                                                    'C) Urgent surgical/toxicology pathways; '
                                                    'avoid unsafe endoscopy themes',
                                                    'D) Induce vomiting repeatedly until '
                                                    'packets appear'],
                                        'answer': 'C) Urgent surgical/toxicology pathways; '
                                                  'avoid unsafe endoscopy themes',
                                        'explanation': 'Body packers conceal drug-filled '
                                                       'packets in the gastrointestinal tract; '
                                                       'packet rupture can release massive '
                                                       'opioid or cocaine doses with '
                                                       'catastrophic toxicity. Management '
                                                       'centers on urgent toxicology and '
                                                       'surgical pathways when obstruction, '
                                                       'rupture, or severe poisoning occurs. '
                                                       'Blind endoscopic retrieval is '
                                                       'generally avoided because of rupture '
                                                       'risk to remaining packets.',
                                        'choice_explanations': {'A': 'Routine endoscopy to '
                                                                     'retrieve body-packer '
                                                                     'packets risks rupture '
                                                                     'and massive drug dump; '
                                                                     'it is generally avoided.',
                                                                'B': 'Early discharge after '
                                                                     'one charcoal dose is '
                                                                     'unsafe while intact '
                                                                     'packets remain and '
                                                                     'rupture risk persists.',
                                                                'C': 'Suspected packet rupture '
                                                                     'or obstruction requires '
                                                                     'urgent '
                                                                     'surgical/toxicology '
                                                                     'pathways; unsafe '
                                                                     'endoscopic retrieval '
                                                                     'themes are avoided '
                                                                     'because rupture can '
                                                                     'release lethal '
                                                                     'opioid/cocaine doses.',
                                                                'D': 'Induced vomiting can '
                                                                     'increase '
                                                                     'rupture/aspiration risk '
                                                                     'and does not reliably '
                                                                     'clear packets.'}}],
                              'extreme': [{'question': 'Cyanide antidote kits may include?',
                                           'options': ['A) N-acetylcysteine as the primary '
                                                       'cyanide binder',
                                                       'B) Deferoxamine to chelate cyanide '
                                                       'ions',
                                                       'C) Naloxone to reverse histotoxic '
                                                       'hypoxia',
                                                       'D) Hydroxocobalamin and other protocol '
                                                       'options'],
                                           'answer': 'D) Hydroxocobalamin and other protocol '
                                                     'options',
                                           'explanation': 'Cyanide inhibits mitochondrial '
                                                          'cytochrome c oxidase (complex IV), '
                                                          'halting oxidative phosphorylation '
                                                          'and causing histotoxic hypoxia. '
                                                          'Hydroxocobalamin binds cyanide to '
                                                          'form cyanocobalamin, which is '
                                                          'renally excreted, rapidly restoring '
                                                          'aerobic metabolism in many '
                                                          'protocols. Smoke inhalation victims '
                                                          'may have concurrent cyanide and '
                                                          'carbon monoxide poisoning requiring '
                                                          'combined management.',
                                           'choice_explanations': {'A': 'N-acetylcysteine '
                                                                        'targets '
                                                                        'NAPQI/glutathione '
                                                                        'pathways in '
                                                                        'paracetamol toxicity, '
                                                                        'not cyanide–complex '
                                                                        'IV inhibition.',
                                                                   'B': 'Deferoxamine chelates '
                                                                        'iron, not cyanide ion '
                                                                        'at cytochrome '
                                                                        'oxidase.',
                                                                   'C': 'Naloxone reverses '
                                                                        'opioids; it does not '
                                                                        'restore oxidative '
                                                                        'phosphorylation '
                                                                        'blocked by cyanide.',
                                                                   'D': 'Cyanide inhibits '
                                                                        'cytochrome c oxidase '
                                                                        '(complex IV); '
                                                                        'hydroxocobalamin '
                                                                        'binds cyanide to form '
                                                                        'cyanocobalamin, and '
                                                                        'other protocol '
                                                                        'options (e.g., '
                                                                        'nitrites/thiosulfate '
                                                                        'historically) are '
                                                                        'used per kits.'}},
                                          {'question': 'Serotonin syndrome vs NMS distinction '
                                                       'matters because?',
                                           'options': ['A) Different triggers and management '
                                                       'nuances',
                                                       'B) Both are treated identically with '
                                                       'bromocriptine only',
                                                       'C) Neither ever involves hyperthermia '
                                                       'or rigidity',
                                                       'D) ECG QRS widening defines both '
                                                       'syndromes equally'],
                                           'answer': 'A) Different triggers and management '
                                                     'nuances',
                                           'explanation': 'Serotonin syndrome is typically '
                                                          'precipitated by serotonergic drug '
                                                          'combinations and features clonus, '
                                                          'hyperreflexia, and rapid onset '
                                                          'hyperthermia, whereas neuroleptic '
                                                          'malignant syndrome follows dopamine '
                                                          'antagonists with severe rigidity '
                                                          'and slower onset. Distinguishing '
                                                          'them matters because management '
                                                          'differs: cyproheptadine and '
                                                          'withdrawal of serotonergics versus '
                                                          'dopaminergic support and '
                                                          'antipsychotic cessation. '
                                                          'Misclassification can delay '
                                                          'toxin-specific therapy.',
                                           'choice_explanations': {'A': 'Serotonin syndrome '
                                                                        '(serotonergic drugs, '
                                                                        'clonus/hyperreflexia, '
                                                                        'rapid onset) versus '
                                                                        'NMS (dopamine '
                                                                        'blockade, lead-pipe '
                                                                        'rigidity, slower '
                                                                        'onset) differ in '
                                                                        'triggers and '
                                                                        'treatments (e.g., '
                                                                        'cyproheptadine vs '
                                                                        'bromocriptine/dantrolene '
                                                                        'contexts).',
                                                                   'B': 'Treating both '
                                                                        'identically with '
                                                                        'bromocriptine only is '
                                                                        'incorrect; serotonin '
                                                                        'syndrome management '
                                                                        'differs and '
                                                                        'bromocriptine is '
                                                                        'aimed at NMS '
                                                                        'dopaminergic '
                                                                        'deficits.',
                                                                   'C': 'Both can involve '
                                                                        'hyperthermia and '
                                                                        'motor findings; '
                                                                        'claiming neither does '
                                                                        'is false and '
                                                                        'dangerous.',
                                                                   'D': 'QRS widening defines '
                                                                        'TCA Na-channel '
                                                                        'toxicity, not a '
                                                                        'shared defining '
                                                                        'feature of SS and '
                                                                        'NMS.'}},
                                          {'question': 'Extracorporeal removal considered for?',
                                           'options': ['A) All highly protein-bound drugs '
                                                       'regardless of toxicity',
                                                       'B) Selected dialyzable toxins with '
                                                       'severe toxicity',
                                                       'C) Only topical exposures without '
                                                       'systemic absorption',
                                                       'D) Every OTC analgesic overdose '
                                                       'without exception'],
                                           'answer': 'B) Selected dialyzable toxins with '
                                                     'severe toxicity',
                                           'explanation': 'Extracorporeal removal '
                                                          '(hemodialysis or related '
                                                          'techniques) is considered when a '
                                                          'toxin has suitable physicochemical '
                                                          'properties—low molecular weight, '
                                                          'low protein binding, small volume '
                                                          'of distribution—and severe clinical '
                                                          'toxicity or failing endogenous '
                                                          'clearance. Examples include severe '
                                                          'lithium, salicylate, and '
                                                          'toxic-alcohol poisoning. Guidance '
                                                          'groups such as EXTRIP summarize '
                                                          'evidence for when extracorporeal '
                                                          'treatment adds benefit.',
                                           'choice_explanations': {'A': 'Highly protein-bound '
                                                                        'toxins with large Vd '
                                                                        'are poorly '
                                                                        'dialyzable; '
                                                                        'extracorporeal '
                                                                        'removal is not '
                                                                        'indicated for all '
                                                                        'such drugs merely '
                                                                        'because of binding.',
                                                                   'B': 'Extracorporeal '
                                                                        'removal is considered '
                                                                        'for selected toxins '
                                                                        'with favorable '
                                                                        'properties (low MW, '
                                                                        'low binding, small '
                                                                        'Vd) plus severe '
                                                                        'toxicity or organ '
                                                                        'failure impairing '
                                                                        'clearance (e.g., '
                                                                        'toxic alcohols, '
                                                                        'severe lithium, '
                                                                        'salicylate).',
                                                                   'C': 'Topical exposures '
                                                                        'without systemic '
                                                                        'absorption do not '
                                                                        'need dialysis for '
                                                                        'systemic toxin '
                                                                        'removal.',
                                                                   'D': 'Not every OTC '
                                                                        'analgesic overdose is '
                                                                        'dialyzable or severe '
                                                                        'enough; decisions are '
                                                                        'toxin- and '
                                                                        'severity-specific.'}}]},
                'cases': {'easy': [{'title': 'Pinpoint Pupils + Bradypnea',
                                    'stem': 'Unresponsive patient with pinpoint pupils and '
                                            'slow breathing; empty opioid bottles nearby.',
                                    'question': 'First steps + antidote theme?',
                                    'answer': 'Support ventilation and give naloxone per '
                                              'protocol.',
                                    'discussion': 'Watch for renarcotization.',
                                    'book_hint': "Goldfrank's Toxicologic Emergencies themes / "
                                                 'Casarett & Doull'}],
                          'medium': [{'title': 'Paracetamol Overdose 8 Hours Ago',
                                      'stem': 'Staggered paracetamol overdose; levels timing '
                                              'complex.',
                                      'question': 'Concept?',
                                      'answer': 'Do not delay NAC when significant risk; '
                                                'follow toxicology protocol.',
                                      'discussion': 'Staggered ingestions are tricky.',
                                      'book_hint': "Goldfrank's Toxicologic Emergencies themes "
                                                   '/ Casarett & Doull'}],
                          'hard': [{'title': 'Wide-Complex Tachycardia After TCA',
                                    'stem': 'Overdose patient has wide QRS and hypotension. '
                                            'Choose the safest high-yield next concept before '
                                            'definitive results.',
                                    'question': 'Therapy theme?',
                                    'answer': 'Sodium bicarbonate for TCA sodium-channel '
                                              'toxicity per ACLS/tox guidance.',
                                    'discussion': 'Avoid class Ia/Ic empiric habits.',
                                    'book_hint': "Goldfrank's Toxicologic Emergencies themes / "
                                                 'Casarett & Doull'}],
                          'extreme': [{'title': 'Smoke Inhalation Collapse',
                                       'stem': 'Fire victim with soot, lactic acidosis, and '
                                               'coma; CO treated but remains severely '
                                               'acidotic. Avoid harmful premature treatment '
                                               'while catastrophic differentials remain open.',
                                       'question': 'Consider?',
                                       'answer': 'Cyanide toxicity — protocol antidotes + '
                                                 'supportive care.',
                                       'discussion': 'Do not miss dual toxicity.',
                                       'book_hint': "Goldfrank's Toxicologic Emergencies "
                                                    'themes / Casarett & Doull'}]}},
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
                                                            'B) Killing vegetative bacteria '
                                                            'but never spores',
                                                            'C) Disinfecting skin before '
                                                            'venipuncture only',
                                                            'D) Validated killing/removal of '
                                                            'viable microorganisms including '
                                                            'spores'],
                                                'answer': 'D) Validated killing/removal of '
                                                          'viable microorganisms including '
                                                          'spores',
                                                'explanation': 'Sterilization is a validated '
                                                               'process that destroys or '
                                                               'removes all viable '
                                                               'microorganisms, including '
                                                               'bacterial spores, to a '
                                                               'specified sterility assurance '
                                                               'level. Methods include moist '
                                                               'heat, dry heat, filtration, '
                                                               'ethylene oxide, and radiation, '
                                                               'chosen for product '
                                                               'compatibility. Injectable '
                                                               'medicines depend on '
                                                               'sterilization or aseptic '
                                                               'processing to prevent '
                                                               'contamination.',
                                                'choice_explanations': {'A': 'Removing visible '
                                                                             'dirt is '
                                                                             'cleaning; it '
                                                                             'does not achieve '
                                                                             'validated '
                                                                             'kill/removal of '
                                                                             'all viable '
                                                                             'microbes '
                                                                             'including '
                                                                             'spores.',
                                                                        'B': 'Killing '
                                                                             'vegetative '
                                                                             'bacteria but '
                                                                             'sparing spores '
                                                                             'is '
                                                                             'disinfection/sanitization '
                                                                             'at best, not '
                                                                             'full '
                                                                             'sterilization.',
                                                                        'C': 'Skin '
                                                                             'disinfection '
                                                                             'before '
                                                                             'venipuncture '
                                                                             'reduces '
                                                                             'transient flora '
                                                                             'on living '
                                                                             'tissue; it is '
                                                                             'antisepsis, not '
                                                                             'product '
                                                                             'sterilization.',
                                                                        'D': 'Sterilization is '
                                                                             'a validated '
                                                                             'process that '
                                                                             'destroys or '
                                                                             'removes all '
                                                                             'viable '
                                                                             'microorganisms '
                                                                             'including '
                                                                             'bacterial spores '
                                                                             'to a specified '
                                                                             'sterility '
                                                                             'assurance '
                                                                             'level.'}},
                                               {'question': 'Gram-positive bacteria stain?',
                                                'options': ['A) Purple/blue after Gram '
                                                            'staining',
                                                            'B) Pink/red because of thin '
                                                            'peptidoglycan',
                                                            'C) Green due to endospore stain '
                                                            'carryover',
                                                            'D) Colorless because they lack '
                                                            'cell walls'],
                                                'answer': 'A) Purple/blue after Gram staining',
                                                'explanation': 'Gram-positive bacteria retain '
                                                               'crystal violet–iodine complex '
                                                               'within a thick peptidoglycan '
                                                               'cell wall and appear '
                                                               'purple/blue after Gram '
                                                               'staining. Gram-negative '
                                                               'organisms have a thin '
                                                               'peptidoglycan layer and outer '
                                                               'membrane that allow '
                                                               'decolorization and take up '
                                                               'safranin counterstain '
                                                               '(pink/red). The stain thus '
                                                               'reflects fundamental '
                                                               'cell-envelope structure.',
                                                'choice_explanations': {'A': 'Gram-positive '
                                                                             'organisms retain '
                                                                             'the crystal '
                                                                             'violet–iodine '
                                                                             'complex in thick '
                                                                             'peptidoglycan '
                                                                             'and appear '
                                                                             'purple/blue '
                                                                             'after Gram '
                                                                             'staining.',
                                                                        'B': 'Pink/red after '
                                                                             'counterstain '
                                                                             'describes '
                                                                             'Gram-negative '
                                                                             'bacteria with '
                                                                             'thin '
                                                                             'peptidoglycan '
                                                                             'and outer '
                                                                             'membrane that '
                                                                             'lose crystal '
                                                                             'violet.',
                                                                        'C': 'Green endospore '
                                                                             'staining is a '
                                                                             'separate '
                                                                             'Schaeffer–Fulton '
                                                                             'method, not the '
                                                                             'Gram primary '
                                                                             'result for '
                                                                             'Gram-positives.',
                                                                        'D': 'Colorless '
                                                                             'wall-less '
                                                                             'microbes (e.g., '
                                                                             'mycoplasma) are '
                                                                             'not classic '
                                                                             'Gram-positive '
                                                                             'staining '
                                                                             'organisms with '
                                                                             'thick '
                                                                             'peptidoglycan.'}},
                                               {'question': 'Disinfection differs from '
                                                            'sterilization by?',
                                                'options': ['A) Always destroying bacterial '
                                                            'spores reliably',
                                                            'B) Reducing microbes on '
                                                            'surfaces/objects without '
                                                            'necessarily sterilizing',
                                                            'C) Guaranteeing SAL of 10^-6 for '
                                                            'every surface wipe',
                                                            'D) Applying only to injectable '
                                                            'drug products'],
                                                'answer': 'B) Reducing microbes on '
                                                          'surfaces/objects without '
                                                          'necessarily sterilizing',
                                                'explanation': 'Disinfection reduces '
                                                               'pathogenic microorganisms on '
                                                               'inanimate surfaces or objects '
                                                               'to a level judged safe for '
                                                               'use, but it does not reliably '
                                                               'eliminate all spores or '
                                                               'achieve sterilization. Agent '
                                                               'selection depends on spectrum, '
                                                               'concentration, contact time, '
                                                               'and material compatibility. '
                                                               'Sterilization is required when '
                                                               'absolute absence of viable '
                                                               'microbes is needed, as for '
                                                               'critical injectables.',
                                                'choice_explanations': {'A': 'Reliable spore '
                                                                             'destruction is '
                                                                             'the hallmark of '
                                                                             'sterilization; '
                                                                             'many '
                                                                             'disinfectants do '
                                                                             'not achieve it.',
                                                                        'B': 'Disinfection '
                                                                             'reduces '
                                                                             'pathogenic '
                                                                             'microbes on '
                                                                             'inanimate '
                                                                             'surfaces/objects '
                                                                             'to a safe use '
                                                                             'level but does '
                                                                             'not necessarily '
                                                                             'eliminate all '
                                                                             'spores or '
                                                                             'achieve '
                                                                             'sterility '
                                                                             'assurance.',
                                                                        'C': 'SAL of 10^-6 is '
                                                                             'a sterilization '
                                                                             'assurance target '
                                                                             'for sterile '
                                                                             'products, not '
                                                                             'guaranteed by '
                                                                             'routine surface '
                                                                             'disinfection '
                                                                             'wipes.',
                                                                        'D': 'Disinfection '
                                                                             'applies broadly '
                                                                             'to '
                                                                             'surfaces/equipment; '
                                                                             'it is not '
                                                                             'limited to '
                                                                             'injectable drug '
                                                                             'products (which '
                                                                             'require '
                                                                             'sterility).'}}],
                                      'medium': [{'question': 'Endotoxin (LPS) risk is mainly '
                                                              'from?',
                                                  'options': ['A) Gram-positive spore-forming '
                                                              'rods only',
                                                              'B) Fungi that produce '
                                                              'aflatoxins in grains',
                                                              'C) Gram-negative bacteria '
                                                              'outer-membrane LPS',
                                                              'D) Viruses lacking any lipid '
                                                              'envelope'],
                                                  'answer': 'C) Gram-negative bacteria '
                                                            'outer-membrane LPS',
                                                  'explanation': 'Bacterial endotoxin is '
                                                                 'lipopolysaccharide (LPS) '
                                                                 'from the outer membrane of '
                                                                 'Gram-negative bacteria and '
                                                                 'is a potent pyrogen. Even '
                                                                 'sterile solutions can cause '
                                                                 'fever and septic-like '
                                                                 'reactions if LPS remains. '
                                                                 'Pharmaceutical water and '
                                                                 'parenteral products are '
                                                                 'therefore controlled with '
                                                                 'bacterial endotoxin tests '
                                                                 'such as LAL/recombinant '
                                                                 'factor C assays.',
                                                  'choice_explanations': {'A': 'Gram-positive '
                                                                               'spore-formers '
                                                                               'produce '
                                                                               'proteinaceous '
                                                                               'toxins/spores '
                                                                               'but not '
                                                                               'classic LPS '
                                                                               'endotoxin of '
                                                                               'Gram-negatives.',
                                                                          'B': 'Aflatoxins are '
                                                                               'fungal '
                                                                               'mycotoxins, '
                                                                               'chemically '
                                                                               'distinct from '
                                                                               'bacterial LPS '
                                                                               'endotoxin.',
                                                                          'C': 'Endotoxin is '
                                                                               'lipopolysaccharide '
                                                                               'from the '
                                                                               'Gram-negative '
                                                                               'outer '
                                                                               'membrane—a '
                                                                               'potent pyrogen '
                                                                               'that can '
                                                                               'remain even '
                                                                               'after bacteria '
                                                                               'are killed.',
                                                                          'D': 'Viruses lack '
                                                                               'LPS; '
                                                                               'non-enveloped '
                                                                               'or enveloped '
                                                                               'viral '
                                                                               'structures are '
                                                                               'not bacterial '
                                                                               'endotoxin.'}},
                                                 {'question': 'Autoclaving typical condition '
                                                              'theme?',
                                                  'options': ['A) Dry heat at 60°C for five '
                                                              'minutes',
                                                              'B) UV light exposure of sealed '
                                                              'vials only',
                                                              'C) Membrane filtration as the '
                                                              'autoclave method',
                                                              'D) Moist heat under pressure '
                                                              '(e.g., 121°C hold)'],
                                                  'answer': 'D) Moist heat under pressure '
                                                            '(e.g., 121°C hold)',
                                                  'explanation': 'Autoclaving uses saturated '
                                                                 'steam under pressure to '
                                                                 'achieve moist-heat '
                                                                 'sterilization, classically '
                                                                 'exemplified by 121 °C for a '
                                                                 'validated hold time (often '
                                                                 'about 15 minutes for many '
                                                                 'loads). Steam kills '
                                                                 'microorganisms by '
                                                                 'coagulating proteins and is '
                                                                 'highly effective against '
                                                                 'spores when air removal and '
                                                                 'heat penetration are '
                                                                 'assured. Cycle parameters '
                                                                 'must be validated for load '
                                                                 'configuration.',
                                                  'choice_explanations': {'A': 'Dry heat at '
                                                                               '60°C for five '
                                                                               'minutes does '
                                                                               'not achieve '
                                                                               'moist-heat '
                                                                               'sterilization '
                                                                               'conditions '
                                                                               'capable of '
                                                                               'killing '
                                                                               'resistant '
                                                                               'spores.',
                                                                          'B': 'UV exposure of '
                                                                               'sealed vials '
                                                                               'has poor '
                                                                               'penetration '
                                                                               'and is not '
                                                                               'equivalent to '
                                                                               'saturated-steam '
                                                                               'autoclaving.',
                                                                          'C': 'Membrane '
                                                                               'filtration is '
                                                                               'a physical '
                                                                               'removal '
                                                                               'sterilization/ '
                                                                               'aseptic method '
                                                                               'for '
                                                                               'heat-labile '
                                                                               'solutions, not '
                                                                               'autoclaving.',
                                                                          'D': 'Autoclaving '
                                                                               'uses saturated '
                                                                               'steam under '
                                                                               'pressure—classically '
                                                                               '~121°C for a '
                                                                               'validated '
                                                                               'hold—to '
                                                                               'achieve '
                                                                               'moist-heat '
                                                                               'sterilization '
                                                                               'including '
                                                                               'spores.'}},
                                                 {'question': 'Preservatives in multi-dose '
                                                              'vials help?',
                                                  'options': ['A) Inhibit microbial growth '
                                                              'after repeated entries',
                                                              'B) Replace the need for aseptic '
                                                              'manufacturing',
                                                              'C) Sterilize the vial contents '
                                                              'after contamination',
                                                              'D) Neutralize bacterial '
                                                              'endotoxin in solution'],
                                                  'answer': 'A) Inhibit microbial growth after '
                                                            'repeated entries',
                                                  'explanation': 'Antimicrobial preservatives '
                                                                 'in multi-dose vials suppress '
                                                                 'growth of microbes '
                                                                 'introduced during repeated '
                                                                 'needle entries after first '
                                                                 'opening. They do not '
                                                                 'sterilize a grossly '
                                                                 'contaminated product and are '
                                                                 'not a substitute for aseptic '
                                                                 'handling. Preservative '
                                                                 'efficacy testing supports '
                                                                 'their inclusion within '
                                                                 'labeled beyond-use '
                                                                 'constraints.',
                                                  'choice_explanations': {'A': 'Antimicrobial '
                                                                               'preservatives '
                                                                               'in multi-dose '
                                                                               'vials suppress '
                                                                               'growth of '
                                                                               'microbes '
                                                                               'introduced '
                                                                               'during '
                                                                               'repeated '
                                                                               'needle entries '
                                                                               'after first '
                                                                               'puncture.',
                                                                          'B': 'Preservatives '
                                                                               'do not replace '
                                                                               'aseptic '
                                                                               'manufacturing '
                                                                               'and initial '
                                                                               'sterility '
                                                                               'assurance of '
                                                                               'the filled '
                                                                               'product.',
                                                                          'C': 'They inhibit '
                                                                               'growth; they '
                                                                               'are not '
                                                                               'validated to '
                                                                               're-sterilize a '
                                                                               'heavily '
                                                                               'contaminated '
                                                                               'vial to SAL '
                                                                               'standards.',
                                                                          'D': 'Preservatives '
                                                                               'do not '
                                                                               'neutralize LPS '
                                                                               'endotoxin, '
                                                                               'which is '
                                                                               'non-living '
                                                                               'pyrogen not '
                                                                               'killed by '
                                                                               'antimicrobials.'}}],
                                      'hard': [{'question': 'HEPA filters in cleanrooms '
                                                            'remove?',
                                                'options': ['A) Only dissolved endotoxin from '
                                                            'WFI loops',
                                                            'B) Airborne particles/microbes to '
                                                            'specified efficiency',
                                                            'C) Only volatile organic solvent '
                                                            'vapors',
                                                            'D) Only chlorine residual from '
                                                            'tap water'],
                                                'answer': 'B) Airborne particles/microbes to '
                                                          'specified efficiency',
                                                'explanation': 'High-efficiency particulate '
                                                               'air (HEPA) filters remove '
                                                               'airborne particles by '
                                                               'interception, impaction, and '
                                                               'diffusion with defined '
                                                               'efficiency (typically ≥99.97% '
                                                               'for 0.3 μm challenge '
                                                               'particles). In cleanrooms they '
                                                               'supply particle-controlled air '
                                                               'that reduces microbial and '
                                                               'particulate contamination risk '
                                                               'during aseptic work. Filter '
                                                               'integrity and airflow patterns '
                                                               'are critical environmental '
                                                               'controls.',
                                                'choice_explanations': {'A': 'Dissolved '
                                                                             'endotoxin in WFI '
                                                                             'is controlled by '
                                                                             'distillation/ultrafiltration '
                                                                             'and Limulus '
                                                                             'testing—not '
                                                                             'removed by HEPA '
                                                                             'air filters.',
                                                                        'B': 'HEPA filters '
                                                                             'remove airborne '
                                                                             'particles and '
                                                                             'associated '
                                                                             'microbes by '
                                                                             'interception, '
                                                                             'impaction, and '
                                                                             'diffusion at '
                                                                             'defined '
                                                                             'efficiency '
                                                                             '(typically '
                                                                             '≥99.97% for 0.3 '
                                                                             'μm), protecting '
                                                                             'cleanroom air.',
                                                                        'C': 'Volatile organic '
                                                                             'vapors require '
                                                                             'activated carbon '
                                                                             'or other '
                                                                             'gas-phase '
                                                                             'controls; HEPA '
                                                                             'targets '
                                                                             'particles, not '
                                                                             'gases.',
                                                                        'D': 'Chlorine '
                                                                             'residual in tap '
                                                                             'water is a '
                                                                             'water-chemistry '
                                                                             'parameter, '
                                                                             'unrelated to '
                                                                             'HEPA particulate '
                                                                             'filtration.'}},
                                               {'question': 'Biological indicator for '
                                                            'autoclave often uses?',
                                                'options': ['A) Escherichia coli vegetative '
                                                            'cells only',
                                                            'B) Candida albicans yeast '
                                                            'suspensions',
                                                            'C) Geobacillus stearothermophilus '
                                                            'spores',
                                                            'D) Influenza virus cultured in '
                                                            'eggs'],
                                                'answer': 'C) Geobacillus stearothermophilus '
                                                          'spores',
                                                'explanation': 'Biological indicators for '
                                                               'steam sterilization commonly '
                                                               'use spores of Geobacillus '
                                                               'stearothermophilus, which are '
                                                               'highly heat resistant. '
                                                               'Survival or kill of the spore '
                                                               'challenge after a cycle '
                                                               'provides a direct measure of '
                                                               'lethality beyond physical '
                                                               'parametric readouts alone. BI '
                                                               'results support validation and '
                                                               'routine monitoring of '
                                                               'autoclave performance.',
                                                'choice_explanations': {'A': 'Escherichia coli '
                                                                             'vegetative cells '
                                                                             'are far less '
                                                                             'heat-resistant '
                                                                             'than Geobacillus '
                                                                             'spores and are '
                                                                             'poor steam BI '
                                                                             'challenges.',
                                                                        'B': 'Candida yeast is '
                                                                             'not the standard '
                                                                             'biological '
                                                                             'indicator '
                                                                             'organism for '
                                                                             'moist-heat '
                                                                             'autoclave '
                                                                             'validation.',
                                                                        'C': 'Biological '
                                                                             'indicators for '
                                                                             'steam '
                                                                             'sterilization '
                                                                             'commonly use '
                                                                             'Geobacillus '
                                                                             'stearothermophilus '
                                                                             'spores because '
                                                                             'of high '
                                                                             'moist-heat '
                                                                             'resistance; kill '
                                                                             'confirms cycle '
                                                                             'lethality.',
                                                                        'D': 'Influenza virus '
                                                                             'in eggs is a '
                                                                             'vaccine '
                                                                             'production '
                                                                             'system, not an '
                                                                             'autoclave BI.'}},
                                               {'question': 'Biofilm on equipment causes?',
                                                'options': ['A) Improved sterilant penetration '
                                                            'every cycle',
                                                            'B) Guaranteed sterility without '
                                                            'cleaning',
                                                            'C) Faster drying of stainless '
                                                            'surfaces only',
                                                            'D) Persistent contamination that '
                                                            'is hard to eradicate'],
                                                'answer': 'D) Persistent contamination that is '
                                                          'hard to eradicate',
                                                'explanation': 'Biofilms are '
                                                               'surface-associated microbial '
                                                               'communities embedded in '
                                                               'extracellular polymeric '
                                                               'substance that impede biocide '
                                                               'penetration and slow '
                                                               'metabolism. Once established '
                                                               'on pharmaceutical equipment, '
                                                               'they shed planktonic cells and '
                                                               'cause persistent contamination '
                                                               'hard to eradicate by ordinary '
                                                               'rinsing. Cleaning validation '
                                                               'and hygienic design aim to '
                                                               'prevent biofilm niches.',
                                                'choice_explanations': {'A': 'Biofilm EPS '
                                                                             'matrices impede '
                                                                             'sterilant/biocide '
                                                                             'penetration '
                                                                             'rather than '
                                                                             'improve it.',
                                                                        'B': 'Biofilms '
                                                                             'undermine '
                                                                             'sterility '
                                                                             'assurance; '
                                                                             'cleaning is '
                                                                             'required before '
                                                                             'disinfection/sterilization '
                                                                             'can succeed.',
                                                                        'C': 'Faster drying of '
                                                                             'stainless steel '
                                                                             'is unrelated to '
                                                                             'the '
                                                                             'contamination '
                                                                             'persistence '
                                                                             'caused by '
                                                                             'biofilms.',
                                                                        'D': 'Biofilms are '
                                                                             'surface-adherent '
                                                                             'microbial '
                                                                             'communities in '
                                                                             'extracellular '
                                                                             'polymeric '
                                                                             'substance that '
                                                                             'resist cleaning '
                                                                             'and '
                                                                             'disinfection, '
                                                                             'causing '
                                                                             'persistent '
                                                                             'equipment '
                                                                             'contamination.'}}],
                                      'extreme': [{'question': 'Aseptic process simulation '
                                                               '(media fill) demonstrates?',
                                                   'options': ['A) Operator/process capability '
                                                               'to maintain sterility',
                                                               'B) Potency assay of the '
                                                               'finished active ingredient',
                                                               'C) Endotoxin destruction by '
                                                               'dry heat tunnels only',
                                                               'D) Tablet content uniformity '
                                                               'across a batch'],
                                                   'answer': 'A) Operator/process capability '
                                                             'to maintain sterility',
                                                   'explanation': 'Aseptic process simulation '
                                                                  '(media fill) replaces '
                                                                  'product with sterile growth '
                                                                  'medium processed through '
                                                                  'the full aseptic '
                                                                  'manufacturing train by '
                                                                  'operators under routine '
                                                                  'conditions. Subsequent '
                                                                  'incubation tests whether '
                                                                  'contamination was '
                                                                  'introduced, thereby '
                                                                  'demonstrating process and '
                                                                  'operator capability to '
                                                                  'maintain sterility. Media '
                                                                  'fills are a GMP expectation '
                                                                  'for validating aseptic '
                                                                  'operations.',
                                                   'choice_explanations': {'A': 'Aseptic '
                                                                                'process '
                                                                                'simulation '
                                                                                '(media fill) '
                                                                                'runs sterile '
                                                                                'growth medium '
                                                                                'through the '
                                                                                'full aseptic '
                                                                                'process with '
                                                                                'operators to '
                                                                                'show the '
                                                                                'process can '
                                                                                'maintain '
                                                                                'sterility '
                                                                                'without '
                                                                                'contamination '
                                                                                'growth.',
                                                                           'B': 'Potency assay '
                                                                                'of API '
                                                                                'measures '
                                                                                'strength/content, '
                                                                                'not aseptic '
                                                                                'contamination '
                                                                                'control '
                                                                                'capability.',
                                                                           'C': 'Dry-heat '
                                                                                'tunnels for '
                                                                                'depyrogenation '
                                                                                'are a '
                                                                                'different '
                                                                                'validation; '
                                                                                'media fills '
                                                                                'specifically '
                                                                                'challenge '
                                                                                'aseptic '
                                                                                'assembly/filling '
                                                                                'sterility.',
                                                                           'D': 'Tablet '
                                                                                'content '
                                                                                'uniformity is '
                                                                                'an oral solid '
                                                                                'quality '
                                                                                'attribute, '
                                                                                'not aseptic '
                                                                                'process '
                                                                                'simulation.'}},
                                                  {'question': 'Mycoplasma contamination is '
                                                               'problematic in?',
                                                   'options': ['A) Terminal steam '
                                                               'sterilization of glass vials '
                                                               'only',
                                                               'B) Cell culture and biologic '
                                                               'production systems',
                                                               'C) Dry-powder inhaler capsule '
                                                               'filling only',
                                                               'D) Sugar-coating pans for oral '
                                                               'tablets only'],
                                                   'answer': 'B) Cell culture and biologic '
                                                             'production systems',
                                                   'explanation': 'Mycoplasmas are '
                                                                  'cell-wall–deficient '
                                                                  'bacteria that pass many '
                                                                  'sterilizing filters and do '
                                                                  'not produce turbidity '
                                                                  'typical of ordinary '
                                                                  'bacterial contamination. In '
                                                                  'cell-culture and biologic '
                                                                  'manufacturing systems they '
                                                                  'alter metabolism, reduce '
                                                                  'yield, and can contaminate '
                                                                  'products. Dedicated '
                                                                  'nucleic-acid or '
                                                                  'culture-based mycoplasma '
                                                                  'tests are required because '
                                                                  'standard microscopy often '
                                                                  'misses them.',
                                                   'choice_explanations': {'A': 'Terminal '
                                                                                'steam '
                                                                                'sterilization '
                                                                                'of glass '
                                                                                'vials kills '
                                                                                'mycoplasma if '
                                                                                'present in '
                                                                                'sterilizable '
                                                                                'loads, but '
                                                                                'the classic '
                                                                                'problem is '
                                                                                'contamination '
                                                                                'of living '
                                                                                'cell cultures '
                                                                                'where '
                                                                                'terminal '
                                                                                'sterilization '
                                                                                'is '
                                                                                'impossible.',
                                                                           'B': 'Mycoplasmas '
                                                                                'are '
                                                                                'wall-deficient '
                                                                                'bacteria that '
                                                                                'pass many '
                                                                                '0.22 μm '
                                                                                'filters and '
                                                                                'silently '
                                                                                'contaminate '
                                                                                'cell '
                                                                                'culture/biologic '
                                                                                'production, '
                                                                                'altering '
                                                                                'growth, '
                                                                                'yields, and '
                                                                                'product '
                                                                                'quality.',
                                                                           'C': 'DPI capsule '
                                                                                'filling is '
                                                                                'dry powder '
                                                                                'oral/inhalation '
                                                                                'manufacturing, '
                                                                                'not the '
                                                                                'primary '
                                                                                'mycoplasma '
                                                                                'cell-culture '
                                                                                'contamination '
                                                                                'niche.',
                                                                           'D': 'Sugar-coating '
                                                                                'pans for '
                                                                                'tablets are '
                                                                                'non-sterile '
                                                                                'oral '
                                                                                'processes '
                                                                                'outside '
                                                                                'mycoplasma '
                                                                                'biologics '
                                                                                'risk.'}},
                                                  {'question': 'Parametric release concepts '
                                                               'rely on?',
                                                   'options': ['A) Skipping all process '
                                                               'validation indefinitely',
                                                               'B) Visual inspection as the '
                                                               'sole release criterion',
                                                               'C) Validated process data in '
                                                               'lieu of finished testing in '
                                                               'defined cases',
                                                               'D) Customer complaints as the '
                                                               'primary batch-release signal'],
                                                   'answer': 'C) Validated process data in '
                                                             'lieu of finished testing in '
                                                             'defined cases',
                                                   'explanation': 'Parametric release '
                                                                  'authorizes batch release '
                                                                  'based on demonstrated '
                                                                  'control of validated '
                                                                  'critical process parameters '
                                                                  'instead of awaiting '
                                                                  'finished-product sterility '
                                                                  'test results in defined '
                                                                  'regulatory frameworks. It '
                                                                  'requires robust process '
                                                                  'understanding, monitoring, '
                                                                  'and documentation—commonly '
                                                                  'applied to terminally '
                                                                  'sterilized products. '
                                                                  'Without that validated '
                                                                  'evidence package, '
                                                                  'traditional end-product '
                                                                  'testing remains required.',
                                                   'choice_explanations': {'A': 'Skipping '
                                                                                'process '
                                                                                'validation '
                                                                                'indefinitely '
                                                                                'removes the '
                                                                                'evidence base '
                                                                                'parametric '
                                                                                'release '
                                                                                'requires.',
                                                                           'B': 'Visual '
                                                                                'inspection '
                                                                                'alone cannot '
                                                                                'assure '
                                                                                'sterility '
                                                                                'SAL; '
                                                                                'parametric '
                                                                                'release needs '
                                                                                'validated '
                                                                                'critical '
                                                                                'process '
                                                                                'parameter '
                                                                                'control.',
                                                                           'C': 'Parametric '
                                                                                'release '
                                                                                'authorizes '
                                                                                'batch release '
                                                                                'from '
                                                                                'demonstrated '
                                                                                'control of '
                                                                                'validated '
                                                                                'critical '
                                                                                'process '
                                                                                'parameters in '
                                                                                'lieu of '
                                                                                'finished '
                                                                                'sterility '
                                                                                'testing in '
                                                                                'defined '
                                                                                'regulatory '
                                                                                'cases (often '
                                                                                'terminally '
                                                                                'sterilized '
                                                                                'products).',
                                                                           'D': 'Customer '
                                                                                'complaints '
                                                                                'are '
                                                                                'post-market '
                                                                                'signals, not '
                                                                                'a primary '
                                                                                'validated '
                                                                                'batch-release '
                                                                                'criterion '
                                                                                'replacing '
                                                                                'process '
                                                                                'evidence.'}}]},
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
                                              'stem': 'Patient spikes fever/chills soon after '
                                                      'IV infusion; cultures negative.',
                                              'question': 'Possible cause?',
                                              'answer': 'Endotoxin contamination — investigate '
                                                        'product/process.',
                                              'discussion': 'Not all fevers are infection in '
                                                            'patient.',
                                              'book_hint': "Hugo and Russell's Pharmaceutical "
                                                           'Microbiology'}],
                                  'hard': [{'title': 'Repeated Environmental Excursions',
                                            'stem': 'Cleanroom settle plates keep failing near '
                                                    'a sink. Choose the safest high-yield next '
                                                    'concept before definitive results.',
                                            'question': 'Approach?',
                                            'answer': 'Root-cause '
                                                      '(water/splash/people/process), '
                                                      'corrective actions, requalify.',
                                            'discussion': 'Trend environmental data.',
                                            'book_hint': "Hugo and Russell's Pharmaceutical "
                                                         'Microbiology'}],
                                  'extreme': [{'title': 'Media Fill Failures After Shift '
                                                        'Change',
                                               'stem': 'Media fills fail only on night shift. '
                                                       'Avoid harmful premature treatment '
                                                       'while catastrophic differentials '
                                                       'remain open.',
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
