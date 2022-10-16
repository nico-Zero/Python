class Student:
    def __init__(self, name, age, gender, gpa, is_on_probation):
        self.name = name
        self.age = age
        self.gender = gender
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def get_name(self):
        return self.name

    def get_gpa(self):
        return self.gpa
