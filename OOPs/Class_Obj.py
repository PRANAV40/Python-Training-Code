class Student:

    # define an attribute
    "Learning Python....."
    marks = 0
    total_score = 0

    # Parameterized Constructor in Python
    print("This is parametrized constructor")

    def __init__(self, name, ids):
        self.name = name
        self.ids = ids

    # Methods in Python
    def display(self):
        print("The name of student is: ", self.name, ", and the ID number is: ", self.ids)

    def calculate_marks(self):
        print("The number is two subject is: ", self.marks + self.marks)
        print("The total score is:", self.total_score, "%")

# Creating the object of class


students = Student("Raj", 1001)
students1 = Student("Ajay", 1002)

# accessing the class attribute using object
students.marks = 85
students.total_score = 85
students1.marks = 75
students1.total_score = 75

# Accessing the methods of class using objects
students.display()
students.calculate_marks()
students1.display()
students1.calculate_marks()


