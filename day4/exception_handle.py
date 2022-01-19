# exception_handle.py
# 예외처리 가장 중요

def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiple(a, b):
    return a * b

def divide(a, b):
    return a / b

print('사칙연산 시작')
a, b = 4, 1
numbers = [3, 6, 9]  # 리스트 생성

# try :
#     print(f'나누기 결과 : {divide(a, b)}')
#     res = int(numbers[3]) * 8
#     print(f'곱하기 결과 : {multiple(a, b)}')
#     print(f'  빼기 결과 : {minus(a, b)}')
#     print(f'더하기 결과 : {add(a, b)}')
# except ZeroDivisionError as e:
#     print(f'나누기 예외. 추가 처리1 {e}')
# except IndexError as e:
#     print(f'인덱스 예외. 추가 처리2 {e}')
# except Exception as e:
#     print(f'알 수 없는 예외. 추가 처리5 {e}')

# print('사칙연산 종료')

# 사칙연산 시작
# 나누기 결과 : 4.0
# 인덱스 예외. 추가 처리2 list index out of range
# 사칙연산 종료

# 예외가 발생하면 그 밑의 코드들은 실행하지 않고 그냥 종료해버림

try :
    print(f'나누기 결과 : {divide(a, b)}')
    res = int(numbers[1]) * 8
    num = int(input('수를 입력하세요.'))

except ZeroDivisionError as e:
    print(f'나누기 예외. 추가 처리1 {e}')
except IndexError as e:
    print(f'인덱스 예외. 추가 처리2 {e}')
except ValueError as e :
    print(f'숫자만 넣으세요.')
except Exception as e:
    print(f'알 수 없는 예외. 추가 처리5 {e}')
finally :
    print(f'곱하기 결과 : {multiple(a, b)}')
    print(f'  빼기 결과 : {minus(a, b)}')
    print(f'더하기 결과 : {add(a, b)}')

print('사칙연산 종료')

# DB를 사용할 때 finally에 DB종료를 넣는다
# DB를 열다가 오류가 나든 안나든 종료를 해야하기 때문

# f9 = 멈추고 기다림
# f10 = 한 줄씩 실행
# f11 = 함수로 진입