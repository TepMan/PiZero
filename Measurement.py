class Measurement(object):
    Temperature = 0
    Co2Value = 0

    # The class "constructor" - It's actually an initializer
    def __init__(self, temperature, co2value):
        self.Temperature = temperature
        self.Co2Value = co2value
#
# def make_student(name, age, major):
#     student = Student(name, age, major)
#     return student
