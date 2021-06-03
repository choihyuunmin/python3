chars = '!@#$%^&*()_+'
codes1 = []

for s in chars:
    codes1.append(ord(s))
    
print(codes1)


# List comprehension
codes2 = [ord(s) for s in chars]
print(codes2)

codes3 = [ord(s) for s in chars if ord(s) > 40]
codes4 = list(filter(lambda x : x > 40, map(ord, chars)))
print(codes3)
print(codes4)


# generator
import array
# Generator : 한 번에 한 개의 항목을 생성 (메모리 절약)
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))
print(tuple_g)
print(array_g)
print(type(tuple_g))
print(type(array_g))
print(next(tuple_g))
print(array_g.tolist())
print()

print(('%s' % c + str(n) for c in ['A','B','C','D'] for n in range(1,11)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)):
    print(s)





marks1 = [['~'] * 3 for n in range(3)]
marks2 = [['~'] * 3] * 3

print(marks1)
print(marks2)


marks1[0][1] = 'X'
marks2[0][1] = 'X'

print(marks1)
print(marks2)
print([id(i) for i in marks1])
print([id(i) for i in marks2])



# Unpacking
print(divmod(100,9))
print(divmod(*(100,9)))
print(*(divmod(100,9)))


x, y, *rest = range(10)
print(x,y,rest)

x, y, *rest = range(2)
print(x,y,rest)


l = (10,15,20)
m = [10,15,20]
print(id(l))
print(id(m))

l = l * 2
print(l) 
l *= 2
print(l)