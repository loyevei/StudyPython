# Mycar.py

from Vehicle import Car
 
if __name__ == '__main__':
    mycar = Car('95나 1228', '흰색')
    # mycar.차량번호 = '95나 1228'
    # mycar.색상 = '흰색'
    mycar.연료 = '경유'
    # mycar.__제조사 = '기아'
    mycar.출고년도 = 1999
    # mycar.기어단수 = 7
    # mycar.__제조사 = '기아'

    # print(mycar.__제조사)
    # print(mycar.연료)
    # print(mycar.기어단수)
    mycar.set제조사('쌍용')
    mycar.제조사확인()
    

    mycar.전진한다(2)
    print(mycar)
    