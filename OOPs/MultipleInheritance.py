class Person:
    def __init__(self, firstname, lastname):
        self.f_name = firstname
        self.l_name = lastname

    def print_name(self):
        print("The name of student is", self.f_name, self.l_name)


class Result:

    def __init__(self, result):
        self.results = result

    def show_result(self):
        print("The student is pass with good marks in Graduation: ", self.results, "%")

# Multiple Inheritance


class PostGraduation(Person, Result):
    def welcome_student(self):
        print("Welcome, in Post Graduation")


p1 = PostGraduation("Ritu", "Raj")
p1.print_name()
p1.results = 78
p1.show_result()
p1.welcome_student()
