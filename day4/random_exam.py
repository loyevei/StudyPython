# random 함수
from random import *

# print(random.choice(range(1,7)))  # 주사위

# lottery
numbers = list(range(1,46))         # 1 ~ 45
lottery = []                        # list()

for i in range(6):   # 6번 반복하겠다 (0 ~ 5)
    # lottery.append(random.choice(numbers))   # 1 ~ 45까지의 수 중에서 랜덤으로 고르겠다
    lottery.append(choice(numbers))    # 다른 패키지의 choice와 충돌할 수 있으니 조심하기

print(lottery)
