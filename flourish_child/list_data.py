from edc_constants.constants import NONE, NOT_APPLICABLE, OTHER
from edc_list_data import PreloadData

list_data = {
    'flourish_child.childdiseases': [
        ('chosp_pneumo', 'Pneumonia'),
        ('chosp_tb', 'Tuberculosis'),
        ('chosp_bronch', 'Bronchiolitis'),
        ('chosp_croup', 'Laryngotracheobronchitis / Croup'),
        ('chosp_diarr', 'Acute diarrheal disease '),
        ('chosp_persisdiarr', 'Persistent diarrheal disease'),
        ('chosp_meningitis', 'Meningitis'),
        ('chosp_malaria', 'Malaria'),
        ('chosp_measle', 'Measles'),
        ('chosp_trauma', 'Trauma'),
        ('chosp_seizure', 'Febrile seizure '),
        ('chosp_malnutrition', 'Malnutrition'),
        ('chosp_anemia', 'Anemia'),
        ('chosp_surgical', 'Surgical reason'),
        ('chosp_other', 'Other'),
    ],
    'flourish_child.chronicconditions': [
        ('chist_asthma', 'Asthma'),
        ('chist_headache', 'Headache (includes migraines, tension headaches)'),
        ('chist_anemia', 'Anemia'),
        ('chist_murmur', 'Cardiac murmur'),
        ('chist_seizure', 'Seizure disorder or other epilepsy'),
        ('chist_diab', 'Diabetes'),
        ('chist_hbp', 'High Blood Pressure'),
        ('chist_cholest', 'High Cholesterol'),
        ('chist_depress', 'Depression'),
        ('chist_lupus', 'Systemic Lupus'),
        ('chist_arthrit ', 'Juvenile rheumatoid arthritis'),
        ('chist_nephrotic ', 'Nephrotic syndrome'),
        ('chist_renal', 'Renal insufficiency'),
        ('chist_nephrol', 'Nephrolithiasis (kidney stones)'),
        ('chist_canc_tumor', 'Cancer (Solid tumor)'),
        ('chist_canc_leuk', 'Cancer (Leukemia, lymphoma related) '),
        ('chist_arrhyt ', 'Cardiac arrhythmia'),
        ('chist_thyroid ', 'Thyroid disorder'),
        ('chist_ibs', 'Inflammatory bowel disease (Crohn’s, ulcerative colitis)'),
        ('chist_other', 'Other, Specify'),
        ('chist_na', 'Not Applicable')
    ],
    'flourish_child.childmedications': [
        (NOT_APPLICABLE, 'Not Applicable'),
        ('cholesterol_meds', 'Cholesterol medication'),
        ('vitamin_d_supp', 'Vitamin D supplement'),
        (NONE, 'None'),
        ('traditional_meds', 'Traditional medications'),
        ('hypertensive_meds', 'Hypertensive medications'),
        ('prenatal_vitamins', 'Prenatal Vitamins')
    ],
    'flourish_child.emosupporttype': [
        ('adherence_counselling', 'Adherence counseling'),
        ('grief_counselling', 'Grief counseling'),
        ('chronic_illness_diagnosis', 'Dealing with diagnosis of chronic illness'),
        ('financial_advice', 'Financial advice'),
        ('relationship_therapy', 'Relationship therapy (family, partner)'),
        ('social_welfare_support', 'Social welfare support (food basket)'),
        ('emo_trauma_therapy', 'Emotional Trauma therapy'),
        (OTHER, 'Other, specify')
    ],
    'flourish_child.emohealthimproved': [
        ('difficult_to_tell',
         'Difficult to tell because I am still receiving emotional support'),
        ('mood_has_improved', 'My mood has improved'),
        ('not_able_to_relax', 'I am now able to relax'),
        ('relationship_with_other_improved',
         'My relationship with other people/family members/partner has improved'),
        ('able_to_manage_emotions',
         'I am now able to manage my thoughts, feelings and emotions'),
        ('accepted_medical_condition',
         'I have accepted my medical condition and I have learnt to stay positive'),
        ('accepted_loved_one_loss', 'I have now accepted the loss of my loved one'),
        ('feeling_fine', 'Emotional support received and feeling fine now'),
        ('no_longer_suicidal', 'I am no longer suicidal'),
        ('defaulted', 'Gave up and defaulted (No difference)'),
        (OTHER, 'Other, specify')
    ],
    'flourish_child.wcsdxadult': [
        ('wmhist_asympt', 'Asymptomatic'),
        ('wmhist_lymphadeno', 'Persistent generalized lymphadeno'),
        ('wmhist_mod_wloss', 'Unexplained moderate weight loss'),
        ('wmhist_resptract', 'Recurrent resp tract infection'),
        ('wmhist_herpeszost', 'Herpes zoster'),
        ('wmhist_cheilitis', 'Angular cheilitis'),
        ('wmhist_oral_ulcer', 'Recurrent oral ulceration'),
        ('wmhist_papular_pruri', 'Papular pruritic eruptions'),
        ('wmhist_dermatit', 'Seborrhoeic dermatitis'),
        ('wmhist_fungal', 'Fungal nail infections'),
        ('wmhist_sev_wloss', 'Unexplained* severe weight loss'),
        ('wmhist_fev', 'Unexplained persistent fever'),
        ('wmhist_diarr', 'Unexplained chronic diarrhoea'),
        ('wmhist_oral_candid', 'Persistent oral candidiasis'),
        ('wmhist_leukoplakia', 'Oral hairy leukoplakia'),
        ('wmhist_pulm_tb', 'Pulmonary tuberculosis'),
        ('wmhist_bactinfect', 'Severe bacterial infections'),
        ('wmhist_stomatit', 'Stomatitis/gingivitis/periodontis'),
        ('wmhist_anemia', 'Anaemia/neutropaenia/thrombocytopa'),
        ('wmhist_hivwaste', 'HIV wasting syndrome'),
        ('wmhist_pneumonia', 'Pneumocystis pneumonia'),
        ('wmhist_bact_pneumo', 'Recurrent severe bacterial pneumo'),
        ('wmhist_herpesinfec', 'Chronic herpes simplex infection'),
        ('wmhist_oeso_candid', 'Oesophageal candidiasis'),
        ('wmhist_extpulm_tb', 'Extrapulmonary tuberculosis'),
        ('wmhist_kaposi_carc', 'Kaposi\u2019s sarcoma'),
        ('wmhist_cytomeg', 'Cytomegalovirus infection'),
        ('wmhist_cns', 'CNS toxoplasmosis'),
        ('wmhist_hivenceph', 'HIV encephalopathy'),
        ('wmhist_meningitis', 'Exp cryptococcosis/meningitis'),
        ('wmhist_dissnon_tb', 'Diss non-TB mycobacterial infection'),
        ('wmhist_leukoence', 'Prog multifocal leukoencephalopathy'),
        ('wmhist_crypto', 'Chronic cryptosporidiosis'),
        ('wmhist_isospor', 'Chronic isosporiasis'),
        ('wmhist_mycosis', 'Disseminated mycosis'),
        ('wmhist_septica', 'Recurrent septicaemia'),
        ('wmhist_lymphoma', 'Lymphoma'),
        ('wmhist_cerv_carc', 'Invasive cervical carcinoma'),
        ('wmhist_leishman', 'Atypical disseminated leishmaniasis'),
        ('wmhist_cardiomy', 'Sympt nephropathy/cardiomyopathy'),
        ('wmhist_na', 'Not Applicable'),
    ],
    'flourish_child.childcovidsymptoms': [
        ('c19c_iso_chestpain', 'Chest pain'),
        ('c19c_iso_chills', 'Chills'),
        ('c19c_iso_cough', 'Cough'),
        ('c19c_iso_diarr ', 'Diarrhea '),
        ('c19c_iso_fev', 'Fever > 37.5 Degree Celsius'),
        ('c19c_iso_aches', 'Muscle aches'),
        ('c19c_iso_nasal', 'Nasal Congestion/Runny Nose'),
        ('c19c_iso_nausea  ', 'Nausea/vomiting'),
        ('c19c_iso_sob', 'Shortness of breath'),
        ('c19c_iso_throat', 'Sore throat'),
        ('c19c_iso_headache', 'Headache'),
        ('c19c_iso_losssmell', 'Loss of Smell'),
        ('c19c_iso_losstaste', 'Loss of Taste'),
        ('c19c_iso_nosympt', 'No Symptoms'),
    ],
    'flourish_child.childcovidsymptomsafter14days': [
        ('c19c_14d_chestpain', 'Chest pain'),
        ('c19c_14d_chills', 'Chills'),
        ('c19c_14d_cough', 'Cough'),
        ('c19c_14d_diarr ', 'Diarrhea '),
        ('c19c_14d_fev', 'Fever > 37.5 Degree Celsius'),
        ('c19c_14d_aches', 'Muscle aches'),
        ('c19c_14d_nasal', 'Nasal Congestion'),
        ('c19c_14d_nausea  ', 'Nausea/vomiting'),
        ('c19c_14d_sob', 'Shortness of breath'),
        ('c19c_14d_throat', 'Sore throat'),
        ('c19c_14d_headache', 'Headache'),
        ('c19c_14d_losssmell', 'Loss of Smell'),
        ('c19c_14d_losstaste', 'Loss of Taste'),
        ('c19c_14d_nosympt', 'No Symptoms'),
    ],
    'flourish_child.solidfoods': [
        ('food_grains', 'Grains, roots and tubers'),
        ('food_legume', 'Legumes and nuts'),
        ('food_dairy', 'Dairy products (milk, yogurt, cheese)'),
        ('food_flesh', 'Flesh foods (meat, fish, poultry and liver/organ meat)'),
        ('food_eggs', 'Eggs'),
        ('food_porridge', 'Porridge'),
        ('food_vita',
         'Vitamin A rich fruits and vegetables (carrots, pumpkin, sweet potato)'),
        ('food_fruitsvege', 'Other fruits and vegetables'),
        ('food_othersolid', 'Other solid foods'),
    ],
    'flourish_child.hivknowledgemedium': [
        ('family', 'Family'),
        ('friends', 'Friends'),
        ('neighbors', 'Neigbors'),
        ('colleagues', 'Colleagues'),
        ('medical_staff', 'Medical Staff'),
        ('school', 'School'),
        ('I_do_not_recall', 'I do not recall'),
        (OTHER, 'Other')
    ],
    'flourish_child.tbknowledgemedium': [
        ('family', 'Family'),
        ('friends', 'Friends'),
        ('neighbors', 'Neigbors'),
        ('colleagues', 'Colleagues'),
        ('medical_staff', 'Medical Staff'),
        ('school', 'School'),
        ('I_do_not_recall', 'I do not recall'),
        (OTHER, 'Other')
    ],
    'flourish_child.TbRoutineScreenAdolMedium': [
        ('government_health_center', 'Government health center'),
        ('private_clinic', 'Private clinic'),
        ('hospital', 'Hospital'),
        ('school_health_clinic', 'school health clinic'),
        (OTHER, 'Other')
    ],
    'flourish_child.staffmember': [
        ('samuel', 'Samuel'),
        ('gosego', 'Gosego'),
        ('martha', 'Martha'),
        ('boitshepo', 'Boitshepo'),
        ('gaontebale', 'Gaontebale'),
        ('olebogeng', 'Olebogeng'),
        ('pearl', 'Pearl'),
        ('kago','Kago'),
        ('fanta','Fanta'),
        ('lebogang','Lebogang'),

    ],
    'flourish_child.tbdiagnostics': [
        ('sputum', 'Sputum sample'),
        ('chest_xray', 'Chest XRay'),
        ('gene_xpert', 'Gene Xpert'),
        ('tst_mantoux', 'TST/Mantoux'),
        ('covid_19_test', 'COVID-19 test'),
        (OTHER, 'Other, specify')
    ],
    'flourish_child.outpatientsymptoms': [
        ('op_cough', 'Cough'),
        ('op_fever', 'Fever'),
        ('op_vomiting', 'Vomiting'),
        ('op_diarrhea', 'Diarrhea'),
        ('op_headache', 'Headache'),
        ('op_fatigue', 'Fatigue'),
        ('op_congestion', 'Congestion'),
        ('op_enlarged_lymph_nodes', 'Enlarged Lymph nodes'),
        ('op_unknown', 'Unknown'),
        ('op_other', 'Other, specify'),
    ],
    'flourish_child.medications': [
        ('child_med_inhaler', 'Inhaler/Albuterol'),
        ('child_med_antibiotics', 'Antibiotics'),
        ('child_med_anxiety', 'Anti-anxiety drugs'),
        ('child_med_asthmatic', 'Anti-asthmatic drugs'),
        ('child_med_depressent', 'Antidepressant drugs'),
        ('child_med_cholesterol', 'Cholesterol medications'),
        ('child_med_diabetes', 'Diabetic medications'),
        ('child_med_heart', 'Heart disease medications'),
        ('child_med_hypertens', 'Hypertensive medications'),
        ('child_med_pk', 'Pain killers'),
        ('child_med_tb', 'TB Treatment'),
        ('child_med_tpt', 'TPT (TB preventive therapy)'),
        ('child_med_traditional', 'Traditional medications'),
        ('child_med_vitd', 'Vitamin D supplement'),
        ('child_med_unknown', 'Unknown'),
        ('child_med_other', 'Other'),
    ],
    'flourish_child.generalsymptoms': [
        ('child_sx_cough', 'Cough'),
        ('child_sx_fever', 'Fever'),
        ('child_sx_headache', 'Headache'),
        ('child_sx_vomiting', 'Vomiting'),
        ('child_sx_diarrhea', 'Diarrhea'),
        ('child_sx_fatigue', 'Fatigue'),
        ('child_sx_congest', 'Congestion'),
        ('child_sx_nodes', 'Enlarged Lymph nodes'),
        ('child_sx_other', 'Other'),
    ],
    'flourish_child.outpatientmedications': [
        ('opmeds_antibiotic', 'Antibiotic'),
        ('opmeds_paracetamol', 'Paracetamol'),
        ('opmeds_bufen', 'Bufen'),
        ('opmeds_multivitamin', 'Multivitamin'),
        ('opmeds_ferrous_sulfate', 'Ferrous Sulfate'),
        ('opmeds_unknown', 'Unknown'),
        ('opmeds_other', 'Other, specify'),
    ],
    'flourish_child.childsocialworkreferrallist': [
        ('refer_c_argument', 'Arguments with partner/spouse'),
        ('refer_c_violence', 'Violence with partner/spouse'),
        ('refer_c_distrust', 'Distrust with partner/spouse'),
        ('refer_c_finances', 'Financial challenges'),
        ('refer_c_diagnosis',
         'Difficultly dealing with diagnoses of chronic illness or infectious disease'),
        ('refer_c_grief', 'Grief counseling (for loss of loved one)'),
        ('refer_c_adherence', 'Adherence counseling'),
        ('refer_c_facility', 'Local medical facility (add details under Comments)'),
        ('refer_c_pedi_support', 'Pediatrician support'),
        ('refer_c_sch_support', 'Schooling support'),
        ('refer_c_eye_care', 'Ophthalmology/Eye care support'),
        ('refer_c_substance_abuse', 'Substance abuse counselling'),
        ('refer_c_other', 'Other, specify')
    ],
    'flourish_child.childtbtests': [
        ('chest_xray', 'Chest Xray'),
        ('sputum_sample', 'Sputum sample'),
        ('stool_sample', 'Stool sample'),
        ('urine_test', 'Urine test (LAM)'),
        ('skin_test', 'Skin test (TST/Mantoux)'),
        ('blood_test', 'Blood test (quantiferon)'),
        (NONE, 'None'),
        (OTHER, 'other')
    ],
    'flourish_child.childhivtestvisits': [
        ('birth', 'Birth '),
        ('6_to_8_weeks', '6 to 8 weeks'),
        ('9_months', '9-months'),
        ('18_months', '18-months'),
        ('after_breastfeeding', '6 weeks after cessation of breastfeeding'),
        (OTHER, 'Other, specify')
    ],
    'flourish_child.childhivnottestedreason': [
        ('missed_visit', 'Missed clinic visit due to time constraints'),
        ('no_transport', 'Did not have transport fare to clinic visit '),
        ('not_offered', 'When at the clinic, the healthcare worker did not offer HIV '
                        'testing'),
        ('formula_fed', 'I did not think further testing was needed because I formula '
                        'fed from birth and my child had a negative test at birth'),
        ('neg_at_birth', 'I did not think further testing was needed because my child '
                         'had a negative test at birth and they have been healthy'),
        ('due_18_months', 'I did not think my child was due for further testing until 18 '
                          'months'),
        ('no_test_kits', 'Test kits out of stock '),
        ('unknown', 'Unknown'),
        (OTHER, 'Other, specify')
    ],
}

preload_data = PreloadData(
    list_data=list_data)
