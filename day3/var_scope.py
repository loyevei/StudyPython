# 변수 라이프스코프

# a = 10    # 여기 a는 전역변수
# res = 0

# def vartest(x):    
#     x = x + 1      # 여기 x는 지역변수 (함수 내에서만 사용 가능)
#     return x

# res = vartest(a)   # 여기 a는 전역변수
# print(res)

a = 10    # 여기 a는 전역변수

def vartest(a):    
    a = a + 1     # 여기 a는 지역변수 (함수 내에서만 사용 가능) 
    return a

a = vartest(a)    # 여기 a는 전역변수
print(a)

