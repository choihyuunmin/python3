import email


class Student(object):
    '''
    Student Class
    Author : CHOI
    DATE : 2021.05.24
    '''
    
    # 클래스 변수
    student_count = 0
    
    def __init__(self, name, number, grade, details, email=None):
        # 인스턴스 변수
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email
        
        Student.student_count += 1
        
        
    def __str__(self):
        return 'str : {}'.format(self._name)
    
    def __repr__(self):
        return 'repr {}'.format(self._name)
    
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Student Detail Info : {} {} {}'.format(self._name, self._email, self._details))
        
    def __del__(self):
        Student.student_count -= 1
        
        
studt1 = Student('Choi', 5, 4, {'gender':'male', 'score1':100, 'score2':95})
studt2 = Student('Cho', 1, 2, {'gender':'male', 'score1':80, 'score2':90}, 'cho@naver.com')


print(dir(studt1))
print()
print(dir(studt2))
print()
print(studt1.__dict__)
print()
print(Student.__doc__)
print()
print(id(studt1))
print(id(studt2))


studt1.detail_info()
studt2.detail_info()
Student.detail_info(studt1)

# ※ 인스턴스 변수는 직접 접근 X
print(studt1.student_count)
print(studt2.student_count)

print(Student.__dict__)
print(studt1.__dict__)



# delete studt2
del studt2

print(studt1.student_count)
print(Student.student_count)
