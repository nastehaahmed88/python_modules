from doctor import Doctor
from patient import Patient
from hospital import Hospital

# create hospital
hospital = Hospital("Croydon Hospital", "London")

#create doctor and add doctors
doc1 = Doctor('Alice Smith', 'Cardiology')
doc2 = Doctor('Bob Jones', 'Hepatology')
doc3 = Doctor('Salma Farah', 'Neurology')
doc4 = Doctor('Naima Hassan', 'Oncology')
doc5 = Doctor('Sadam Ahmed', 'Pediatrics')


hospital.add_doctor(doc1)
hospital.add_doctor(doc2)
hospital.add_doctor(doc3)
hospital.add_doctor(doc4)
hospital.add_doctor(doc5)


#create and add patient
pat1 = Patient('Fatuma Sheikh', 50, 'Heart Disease')
pat2 = Patient('Hawa Ali', 35, 'Liver Disease')
pat3 = Patient('Amina Hassan', 25, 'Brain Tumor')
pat4 = Patient('Nur Hassan', 40, 'Cancer')
pat5 = Patient('Sadia Ahmed', 30, 'Asthma')

hospital.add_patient(pat1)
hospital.add_patient(pat2)
hospital.add_patient(pat3)
hospital.add_patient(pat4)
hospital.add_patient(pat5)

# assign a patient to a doctor
hospital.assign_patient_to_doctor(pat1.name, doc1.name)
hospital.assign_patient_to_doctor(pat2.name, doc2.name)
hospital.assign_patient_to_doctor(pat3.name, doc3.name)
hospital.assign_patient_to_doctor(pat4.name, doc4.name)
hospital.assign_patient_to_doctor(pat5.name, doc5.name)


#display hospital information
hospital.show_doctors()
hospital.show_patients()
