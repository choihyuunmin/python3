# LIST
# Student 1
student_name_1 = 'Kim'
student_number_1 = 1
student_grade_1 = 1
student_detail_1 = [
                    {'gender':'male',
                     'score1':95,
                     'score2':88}
                    ]

# Student 2
student_name_1 = 'Lee'
student_number_1 = 2
student_grade_1 = 2
student_detail_1 = [
                    {'gender':'female',
                     'score1':70,
                     'score2':92}
                    ]

# Student 3
student_name_1 = 'Park'
student_number_1 = 3
student_grade_1 = 3
student_detail_1 = [
                    {'gender':'female',
                     'score1':90,
                     'score2':100}
                    ]


# 리스트 구조 관리하기 불편 , 데이터의 정확한 위치 매핑해서 사용
student_names_list = ['Kim', 'Lee', 'Park']
student_numbers_list = [1, 2, 3]
student_grades_list = [1, 2, 3]
student_details_list = [
    {'gender' : 'male', 'score1': 95, 'score2': 88},
    {'gender' : 'female', 'score1': 70, 'score2': 92},
    {'gender' : 'male', 'score1': 90, 'score2': 100}
]

# delete student 
del student_names_list[0]
del student_numbers_list[0]
del student_grades_list[0]
del student_details_list[0]

print(student_names_list)
print(student_numbers_list)
print(student_grades_list)
print(student_details_list)

print()
print()

# DICT
# 코드 반복, 중첩
students_dicts = [
    {'student_name': 'Kim', 'student_number': 1, 'student_grade': 1, 'student_detail': {'gender': 'male', 'score1': 95, 'score2': 88}},
    {'student_name': 'Lee', 'student_number': 2, 'student_grade': 2, 'student_detail': {'gender': 'Female', 'score1': 70, 'score2': 92}},
    {'student_name': 'Park', 'student_number': 3, 'student_grade': 3, 'student_detail': {'gender': 'male', 'score1': 90, 'score2': 100}}
]
# delete student
del students_dicts[1]
print(students_dicts)
print()
print()

# CLASS
class Student:
    def __init__(self, name, number, grade, details):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
    
    def __str__(self):
        return 'str : {} - {}'.format(self._name, self._number)
    
    def __repr__(self):
        return 'repr : {} - {}'.format(self._name, self._number)
    
    
student1 = Student('Kim', 1, 1, {'gender': 'male', 'score1': 95, 'score2': 88})
student2 = Student('Lee', 2, 2, {'gender': 'female', 'score1': 70, 'score2': 92})
student3 = Student('Park', 3, 3, {'gender': 'male', 'score1': 90, 'score2': 100})

print(student1.__dict__)
print(student2.__dict__)
print(student3.__dict__)

print()
students_list = []
students_list.append(student1)
students_list.append(student2)
students_list.append(student3)
print()

# 반복문 작동 시 str 메소드 호출(str 없으면 repr)
for x in students_list:
    print(x)
    print(repr(x))
    
print(students_list) # 리스트 append 시 repr이 호출됨

  
  
    
    
 