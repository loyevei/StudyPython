# 자료형
print(None)
print(type(None))   # Nonetype

print( 0 == None)
a = None            # False

print(a)
print(type(a))      # Nonetype

# 숫지형
금액 = 12_345_666
print(금액)

# 문자열
bruce_eckel = 'Life is short, You need Python'
print(bruce_eckel)

print('---------------------')
bruce_eckel = 'Life is short. \nYou need Python'
print(bruce_eckel)

print('---------------------')
bruce_eckel = '''Life is short. \n
You need Python
난 필요없는데... 파이썬'''
# ''' ''' 은 이미 한 줄 한 줄 다른 줄로 만들어주니까 \n을 굳이 쓸 필요 없다
print(bruce_eckel)

print('---------------------')
# 불형 (boolean)
val_sum = 1000
print(val_sum == 1000)
print(val_sum == 999)
# print(val_sum = 10)

bl_true = True
print(type(bl_true))
print(bl_true == True)      # True
print(bl_true is True)      # True

print(a is None)            # True
print(val_sum is 1000)      # True

# 의미가 있는 bool
print(bool(1))              # True   1은 참이다
print(bool(0))              # False  0은 거짓이다 

# list
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(b)

b = [i for i in range(10)]
print(b)

arr2 = ['Life', 'is', 'short', 'U', 'need', 'Python', 3]
print(arr2)

# 2차원 배열
arr3 = [[1,2,3],[4,5,6]]
print(arr3)

# 빈 리스트 생성 이건 None이 아님
arr4 = list()
print(arr4)

# 튜플
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)

# 딕셔너리
spiderman = { 'name' : 'Peter Parker', 
              'age' : '18', 
              'weapon' : 'web shooter'}
print(spiderman)

# 집합 -> 중복 제거해줌
set_int = set([1,2,3,4,5,6,1,2,2])
print(set_int)             # {1, 2, 3, 4, 5, 6}

# 