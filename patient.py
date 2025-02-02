class Patient:
  def __init__(self, name, age, ailment):
    self.name = name
    self.age = age
    self.ailment = ailment
    

  def __str__(self):
      return f"Patient {self.name.upper()}, Age {self.age}, Ailment: {self.ailment.upper()}"