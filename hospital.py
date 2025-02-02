from doctor import Doctor
from patient import Patient

class Hospital:
  def __init__(self,name, location):
    self.name = name
    self.doctors = []
    self.patients = []

  def add_doctor(self, doctor):
      self.doctors.append(doctor)

  def add_patient(self, patient):
      self.patients.append(patient)

  def show_doctors(self):
        print(f"Doctors at {self.name}:")
        for doctor in self.doctors:
          print(doctor)
        print("\n") 

  def show_patients(self):
        print(f"Patients at {self.name}:")
        for patient in self.patients:
          print(patient)
          

          
  def assign_patient_to_doctor(self, patient_name, doctor_name):
      # find a pateint 
      patient = next((p for p in self.patients if p.name == patient_name), None)
      # find doctor
      doctor = next((d for d in self.doctors if d.name == doctor_name), None)
      if patient and doctor:
          print(f"{patient_name} has been assigned to Dr. {doctor_name}")
      else:
          print('Either patient or doctor not found')  
      print("\n")
          
          
          
  def show_assignment(self):
      # show the assignment of patients to doctors
      if self.assignments:
          print(f"Assignments at [self.name]:")
          for doctor_name, patient_name in self.assignments.items():
              print(f"Dr. {doctor_name} is assigned to {patient_name}")
      else:
          print("No assignments yet.")  
          
                
      
  