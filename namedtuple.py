# tuple
pt1 = (1.0, 2.0)
pt2 = (4.5, 5.5)

from math import sqrt
from unicodedata import name


# 두 점 사이의 거리
length = sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)
print(length)

# Named tuple
from collections import namedtuple

Point = namedtuple('아무거나', 'x y')

pt1 = Point(1.0, 2.0)
pt2 = Point(4.5, 5.5)

length2 = sqrt((pt2.x - pt1.x)**2 + (pt2.y - pt1.y)**2)
print(length2)

print(length2 == length)


print(pt1)
print()
print()
print()

# namedtuple declare
Way1 = namedtuple('way1', ['x','y'])
Way2 = namedtuple('way2', 'x, y')
Way3 = namedtuple('way3', 'x y')
Way4 = namedtuple('way4', 'x y x class', rename=True)  # Default=False
print(Way1,Way2,Way3,Way4)
print()
print()

# Dict to unpacking
temp_dict = {'x':75, 'y':55}
test1 = Way1(x=10, y=35)
test2 = Way2(20, 40)
test3 = Way3(30, y=50)   # 앞에는 안됨, 뒤에만(모든 파라미터 해당)
test4 = Way4(10, 20, 30, 40)
test5 = Way3(**temp_dict)
print(test1,test2,test3,test4,test5)



# Unpacking
x, y = test3
print(x+y)

## Namedtuple method
# _make()
temp = [10,100]
test6 = Way1._make(temp)
print(test6)

# _fields : 필드 이름 확인
print(test1._fields)
print(test2._fields)
print(test3._fields)
print(test4._fields)
print(test5._fields)

# _asdict() : OrderdDict 반환
print(test1._asdict())

# _replace() : 수정된 새로운 객체 반환
print(test2._replace(y= 1000))