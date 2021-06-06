# Dictionary : Key의 중복 허용 X
# Set : 값 중복 허용 X

# print(__builtins__.__dict__)

t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40 ,50])
print(hash(t1))
# print(hash(t2)) # 리스트는 unhashable



# Dict Setdefault
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]
        
print(new_dict1)


# Use setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)
    
print(new_dict2)


print()
print()


# 사용자 정의 Dict 상속
class UserDict(dict):
    def __missing__(self, key):
        print("Called : __missing__")
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key ,default=None):
        print('Called : __getitem__')
        try:
            return self[key]
        except KeyError:
            return default
        
    def __contains__(self, key):
        print('Called : __contains__')
        return key in self.keys() or str(key) in self.keys()
    
    
    
user_dict1 = UserDict(one=1, two=2)
user_dict2 = UserDict({'one':1, 'two':2})
user_dict3 = UserDict([('one',1),('two',2)])

print(user_dict1)
print(user_dict2)
print(user_dict3)

# print(user_dict2[2])
print(user_dict1['one'])
print('one' in user_dict3)
# print(user_dict3['three'])
print(user_dict3.get('three'))
        
        
        
        
# immutable dict
from types import MappingProxyType

d = {'key1':'TEST1'}

# Read Only
d_frozen = MappingProxyType(d)
print(d, id(d))
print(d_frozen, id(d_frozen))
print(d is d_frozen, d == d_frozen)


# MappingProxyType 은 수정이 안됨X
# d_frozen['key2'] == "TEST2"



# 집합 자료형
s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set()
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})


print(s1)
s1.add('Melon')
print(s1)

# 추가 불가!
# s5.add('Melon')

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))