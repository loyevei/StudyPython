# 변수 -  파이썬의 변수에는 제약이 거의 없다.
a = '헬로우'
print(a)

a = 3.141592
print(a)

a = 10
print(10)

a = 12324354545233
print(a)

a = 1/ 10
print(a)

# 변수값을 지정(할당) - assign 하는 방법
b = 3.141592
c = 'python'
d = (1, 2, 3)          # 튜플
e = [1, 2, 3, 4]       # 리스트
f = [7, '8', '$', a]   # 파이썬의 장점

# 변수명 지정 불가 (특수문자는 _ 빼고 다 안 됨)
val = 10
val2 = 20
val4 = 30
# 4val = 40
# -val = 50
# *val = 60
val_of_change = 99
chain_reaction = 108
chainReaction = 109
# chain Reaction = 1099
# val- = 111
# val$ = 99
val_ = 999
Val_ = 9999
print(val_)
print(Val_)

MyAccountOfBank = 1
은행계좌금액 = 1

# 변수에 지정되는 id값 확인
print(id(val_))
print(id(Val_))

# 변수 타입 확인
print(type(val_))  # int
print(type(c))     # string
print(type(d))     # tuple
print(type(e))     # list
print(type(f))     # list
print(type(a))     # float

