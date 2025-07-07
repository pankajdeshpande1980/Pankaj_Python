# name = "Santhosh"
# age = 32

# print(type(name))
# print(type(age))

# class => template/blue print
# object => copy of the template

class Student:

    def __init__(self, name, standard, id_no):
        self.name = name
        self.standard = standard
        self.identification_number = id_no


    
student_1 = Student(name="xyz", standard="5", id_no="123") # object 1
student_2 = Student(name="abc", standard="5", id_no="124") # object 2

print(type(student_1))
print(type(student_2))

print(type(Student))

# type => metaclass


class Stock:

    def __init__(self, symbol, company_name):
        self.symbol = symbol
        self.company_name = company_name
    
    def get_52_week_min(self, minimum_date, max_date):
        "generates minimum values from last 52 weeks"
        ... 

    def get_global_max(self):
        "generates maximum value from listed day"
    
    def __repr__(self):
        return f"Company Name = {self.company_name}, Symbol = {self.symbol}"

bse = Stock(symbol="BSE", company_name="Bombay Stock Exchange")
reliance = Stock(symbol="REL", company_name="Reliancet Industries")

print(bse)
print(reliance)

class Employee:
    def __init__(self, salary):
        self.name = ""
        self.joining_date = ""
        self.designation = ""
        self.manager = ""
        self.location = ""
        self.salary = salary

    def appraisal(self, appraisal_amount):
        self.salary = self.salary+appraisal_amount
        # store new salary in database
        # return new_salary
    
new_employee = Employee(salary=1000)
print(new_employee.salary)
print("after appraisal")
new_employee.appraisal(1000)
print(new_employee.salary)

