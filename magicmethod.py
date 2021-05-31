from turtle import Vec2D


number = 100

print(number + 100)
print(number.__add__(200))
print(number.__doc__)
print(number.__bool__(), bool(number))
print('--------------------------------------------------magic method start--------------------------------------------------')


# class1
class Student:
    def __init__(self, name, height):
        self._name = name
        self._height = height
        
    def __str__(self):
        return 'Student Class Info : {}, {}'.format(self._name, self._height)
    
    def __ge__(self, x):
        print('Called >> __ge__ method')
        if self._height >= x._height:
            return True
        else:
            return False
        
    def __le__(self, x):
        print('Called >> __le__ method')
        if self._height <= x._height:
            return True
        else:
            return False
        
    def __sub__(self, x):
        print('Called >> __sub__ method')
        return self._height - x._height
    
    
s1 = Student('James', 181)
s2 = Student('Steve', 170)

print(s1 >= s2)
print(s1 <= s2)
print(s1 - s2)
print(s2 - s1)
print(s1)
print(s2)


# class2
class Vector:
    def __init__(self, *args):
        "Create a Vector, example : v = Vector(1,2)"
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args
            
    def __repr__(self):
        "Returns the vector informations"
        return "Vector(%r, %r)" % (self._x, self._y)
    
    def __add__(self, other):
        "Returns the vector addition of self and other"
        return Vector(self._x + other._x, self._y + other._y)
    
    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)
    
    def __bool__(self):
        return bool(self._x, self._y)
    
        
v1 = Vector(3, 5)
v2 = Vector(15, 20)
v3 = Vector()
print()


print(Vector.__init__.__doc__)
print()
print(Vector.__repr__.__doc__)
print()
print(Vector.__add__.__doc__)
print()

print(v1, v2, v3)
print(v1 + v2)
print(v1 * 4)

