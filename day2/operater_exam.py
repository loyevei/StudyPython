# 연산자
a = 11
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

# 문자열 연산
stat1 = 'Hello'
stat2 = 'World'
res = stat1 + stat2
res1 = stat1 , stat2

print(stat1 + stat2)       # HelloWorld
# print(stat1 - stat2)   ->  문자열에서는 -(빼기) 없음
print(stat1 * 5)           # HelloHelloHelloHelloHello
# print(stat1 * stat2)   ->  문자끼리 *(곱하기) 없음
# print(stat1 / 3)       ->  문자열에서는 /(나누기) 없음
print(stat1, stat2)        # Hello World

print(res) 
print(res1)                # ('Hello', 'World')



stat3 = '안녕하세요'
print(stat3)
stat4 = '저리가' + stat3[3:]
print(stat4)


## 문자열 포맷팅
첫번째 = '투'
두번째 = '유'

str1 = "I'm so happy {0} you. Are {1}?".format(첫번째, 두번째)
print(str1)

str2 = f"I'm so happy {첫번째} you. Are {두번째}?"
print(str2)

## 숫자 천단위 콤마
money = 100000000000
print(format(money, ',d'))

from datetime import datetime
from posixpath import split
from re import M

now = datetime.now()         # 현재일시 생성
print(now)
print(now.strftime('%Y년 %m월 %d일 %H:%M:%S'))

import math

myPi = math.pi
print(myPi)

print('{0}'.format(myPi))
print('{0:0.2f}'.format(myPi))
print(f'{myPi:0.6f}')

full_name = 'Hugo MG Sung'
age = 47
greeting = f'''안녕하세요. 
저는 {full_name}입니다. 
나이는 {age:0.1f}살이구요.'''

print(greeting)

part_name = full_name.split()
print(part_name)
print(type(part_name))            # 리스트임

test = 'Hey, guys'
print(test.split(','))

# | split
code = 'TEST|2022|01|17|F45678'
split_codes = code.split('|')
print(split_codes)

# 단어교체 -> replace
print(full_name.replace('Hugo MG', 'Ashley'))

# 공백 제거 -> strip  == Oracle의 TRIM과 동일
aaa = '       Hello, World      '
print(aaa.lstrip())
print(aaa.rstrip())
print(aaa.strip())

# 위치 알려주기 - index
print(full_name.index('H'))    # 0
# print(full_name.index('h'))  # 값을 못 찾음
print(full_name.index('u'))    # 1
print(full_name.index('g'))    # 2
print(full_name.index('G'))    # 6

print(full_name.find('X'))     # -1 (해당 글자가 없다)
print(full_name.find('MG'))    # 5 (M은 5, G는 6인데 M걸로 나옴)

print(full_name.count('u'))    # 2 (u는 2번 나왔음)
print(full_name.count('n'))

print('-'.join(full_name))
print(full_name.lower())
print(full_name.upper())

