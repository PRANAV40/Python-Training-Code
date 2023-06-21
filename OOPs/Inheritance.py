# Base class
class Person:
    def __init__(self, firstname, lastname):
        self.f_name = firstname
        self.l_name = lastname

    def print_name(self):
        print("The name of student is", self.f_name, self.l_name)


# Derived class 1
class Student(Person):
    def __init__(self, firstname, lastname, year):
        Person.__init__(self, firstname, lastname)
# super().__init__(firstname, lastname)
        self.graduation_year = year

    def welcome(self):
        print("Welcome, in Post Graduation,the graduation passing year of this student is", self.graduation_year)


# Single inheritance
student1 = Student("Ritu", "Raj", 2021)
student1.print_name()
student1.welcome()


# Derived class 2
class Exam(Student):

    def __init__(self, roll_nos, firstname, lastname, year):
        super().__init__(firstname, lastname, year)
        self.roll_no = roll_nos

    def paper(self):
        print("The roll no of student is ", self.roll_no)

# Multilevel inheritance


# s1 = Exam(131, "Ritu","Raj",2021)
# s1.paper()
# s1.f_name = "Ritu"
# s1.l_name = "Raj"
# s1.graduation_year = 2021
# s1.print_name()
# s1.welcome()


