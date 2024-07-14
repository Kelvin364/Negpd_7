# models/bmi.py

class BMI:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.bmi_value = self.calculate_bmi()

    def calculate_bmi(self):
        return round(self.weight / (self.height/100)**2, 2)
