# Person.py
# Person 클래스

from jinja2 import FileSystemLoader


class Person:
    name = '무명이'    # 아직 이름이 없다
    age = 0
    height = 0
    gender = ''
    feetsize = 250
    bloodtype = ''

    # 생성자
     # 이니셜라이즈(초기화를 해준다) 
     # 없으면 클래스가 자동으로 만듬 -> def __init__(self): pass
    def __init__(self, name, age) -> None:   # 리턴값이 None이다
        self.name = name
        self.age = age
        print('Person이 생성되었습니다')

    def 소개한다(self) -> None:
        greeting = f'''안녕하세요. 저는 {self.name}입니다.
        {self.gender}구요. {self.age}살 입니다.
        신발 사이즈는 {self.feetsize}입니다.
        '''
        print(greeting)
    
    def 먹는다(self, food):
        print(f'{self.name}이(가) {food}을(를) 먹는다')

    def 일한다(self, drink):
        print(f'{self.name}이(가) {drink}을(를) 마시면서 일한다')

if __name__ == '__main__':
    # p = Person()     # p라는 이름의 Person 객체 생성
    # print(type(p))
    # print(id(p))     # id값
 
    # p2 = Person()    # p2 객체 생성
    # print(type(p2))
    # print(id(p2))

    kye = Person('김예은', 28)   # == __init__(self, name, age):
    # kye.name = '김예은'
    # kye.age = 28
    kye.height = 163
    kye.gender = 'female'
    # kye.feetsize = 230
    kye.bloodtype = 'RH+ AB'

    hgd = Person('홍길동', 490)
    # hgd.name = '홍길동'
    # hgd.age = 490
    hgd.height = 150
    hgd.gender = 'male' 

    kye.소개한다()
    kye.먹는다('본죽')
    kye.일한다('핫식스')
