# class method, instance method, static method

from inspect import isdatadescriptor
from lzma import is_check_supported
from turtle import st


class Student(object):
    """
    Student Class
    Author : hmchoi
    Date : 2021.05.27
    """
    # Class variable
    tuition_per = 1.0
    
    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa
        
        
    # Instance method
    def full_name(self):
        return '{} {}'.format(self._first_name, self._last_name)
    
    # Instance method
    def detail_info(self):
        return 'INFO : {} / {} / {} / {} / {} / {}'.format(self._id, self.full_name(), self._email, self._grade, self._tuition, self._gpa)
    
    # Instance method
    def get_fee(self):
        return 'Before tuition -> id : {}, fee : {}'.format(self._id, self._tuition)
    
    # Instance method
    def get_fee_culc(self):
        return 'After tuition -> id : {}, fee : {}'.format(self._id, self._tuition * Student.tuition_per)
    
    
    
    # Class method
    @classmethod
    def raise_fee(cls, per):
        if per <= 1:
            print('Please enter 1 or more')
            return
        cls.tuition_per = per
        print("//Tuition increased//")
        
    @classmethod
    def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
        return cls(id, first_name, last_name, email, grade, tuition * cls.tuition_per, gpa)
    
    
    # Static method
    def is_scholarship_static(inst):
        if inst._gpa >= 4.3:
            return '{} is scholarship recipient'.format(inst._last_name)
        return 'Sorry. Not a scholarship recipent'
    
    def __str__(self):
        return 'INFO -> name : {}, grade : {}, email : {}'.format(self.full_name(), self._grade, self._email)
    
    
    
student1 = Student(1, 'choi', 'hm', 'choi@abc.com', '1', 400, 3.5)
student2 = Student(2, 'choi', 'jm', 'choi2@abc.com', '2', 500, 4.5)

print(student1)
print(student2)
print()

print(student1.detail_info())
print(student2.detail_info())
print(student1.get_fee())
print(student2.get_fee())

# Non-use class method (change Class variable)
Student.tuition_per = 1.2

print(student1.get_fee_culc())
print(student2.get_fee_culc())
print()

student1.raise_fee(1.6)
print()
print(Student.tuition_per)
print(student1.get_fee_culc())
print()


# make class methods' instance
student3 = Student.student_const(3, 'Park', 'hj', 'park@abc.com', '3', 550, 4.0)
student4 = Student.student_const(4, 'Park', 'mj', 'park2@abc.com', '4', 300, 4.2)


print(student3._tuition)
print(student4._tuition)

print(student3.detail_info())
print(student4.detail_info())


print(student3._tuition)
print(student4._tuition)

# Non-use static method
def is_scholarship(inst):
    if inst._gpa >= 4.3:
        return '{} is a scholarship recipient'.format(inst._last_name)
    return 'Sorry. Not a scholarship recipient'


print(is_scholarship(student1))
print(is_scholarship(student2))
print(is_scholarship(student3))
print(is_scholarship(student4))


# Use static method
print(Student.is_scholarship_static(student1))
print(Student.is_scholarship_static(student2))
print(Student.is_scholarship_static(student3))
print(Student.is_scholarship_static(student4))

print('or')

print(student1.is_scholarship_static())
print(student2.is_scholarship_static())
print(student3.is_scholarship_static())
print(student4.is_scholarship_static())