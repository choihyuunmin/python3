fresh_fruit = {
    '사과' : 10,
    '바나나' : 8,
    '레몬' : 5
}



# 1

def make_lemonade(count):
    print(count, "make lemonade")

def out_of_stock():
    print("out of stock")

count = fresh_fruit.get('레몬', 0)

# 기존
# if count:
#     make_lemonade(count)
# else:
#     out_of_stock()


# Walrus
if count := fresh_fruit.get('레몬', 0):
    make_lemonade(count)
else:
    out_of_stock()
    

# 2
    
def make_cider(count):
    print(count, "make cider")
    
# 기존
count = fresh_fruit.get('사과', 0)

# if count >= 4:
#     make_cider(count)
# else:
#     out_of_stock()
    
# Walrus
if (count := fresh_fruit.get('사과', 0)) >= 4:
    make_cider(count)
else:
    out_of_stock()
    
    
# 3

def slice_bananas(count):
    pass

class OutOfBananas(Exception):
    pass

def make_smoothies(count):
    pass

#1)
pieces = 0
count = fresh_fruit.get('바나나', 0)
if count >= 2:
    pieces = slice_bananas(count)
    
try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()
    
#2)
count = fresh_fruit.get('바나나', 0)
if count >= 2:
    pieces = slice_bananas(count)
else:
    pieces = 0
    
try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()
    
    
# Walrus 1
pieces = 0
if (count := fresh_fruit.get('바나나', 0)) >= 2:
    pieces = slice_bananas(count)
    
try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()
    
# Walrus 2
if (count := fresh_fruit.get('바나나', 0)) >= 2:
    pieces = slice_bananas(count)
else:
    pieces = 0
    
try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()