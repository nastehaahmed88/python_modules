class Doctor:
  def __init__(self, name, specialty):
    self.name = name
    self.specialty = specialty
  
  def __str__(self):
    return f"Dr.{self.name.upper()}, Specialist in {self.specialty.upper()}"