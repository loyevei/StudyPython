# 커서에 접근하는 코드를 함수로 작성
import cx_Oracle as ora

def myconn():
    dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')   # datasourcename(내가 어디 접속하는지, 아이디 패스워드 보내는 곳)
    conn = ora.connect(user='scott', password='tiger', dsn=dsn, encoding='utf-8')
    return conn

def getAllData(conn):    # conn객체를 매개변수로 받아서 쿼리를 실행할 함수
    cur = conn.cursor()  # 커서 생성
    query = 'SELECT * FROM emp'  # emp 테이블에서 데이터를 모두 가져와라
    for row in cur.execute(query):   # emp 테이블의 최상단에 커서가 위치하면서
        print(row)    # 모든 데이터를 한 줄씩 출력

def getNameAndJobData(conn):
    cur = conn.cursor()
    query = 'SELECT ename, job FROM emp'   # emp 테이블에서 ename, job만 가져와라
    cur.execute(query)    # 실행
    while True:
        row = cur.fetchone()    # fetch one = 한 row(레코드) 읽기
        if row is None:
            break
        else:
            print(row)

# def getDeptName(conn, no, loc):
#     cur = conn.cursor()
#     query = f'SELECT * FROM dept WHERE deptno = {no} AND loc = \'{loc}\''   
#     cur.execute(query)
#     row = cur.fetchone()
#     print(row)

# def getDeptName(conn, tup):
#     cur = conn.cursor()
#     # query = 'SELECT * FROM dept WHERE deptno = :1'   
#     # # :1(매개변수) ->  no에 따라 숫자가 바뀜 (근데 매개변수가 1개라는 뜻)
#     # # deptno = 10 -> 10번만 가져와라 
#     # cur.execute(query, no)
#     query = f'SELECT * FROM dept WHERE deptno = {tup[0]} AND loc = \'{tup[1]}\''   
#     # :1(매개변수) ->  no에 따라 숫자가 바뀜 (근데 매개변수가 1개라는 뜻)
#     # deptno = 10 -> 10번만 가져와라 
#     cur.execute(query, tup)
#     row = cur.fetchone()
#     print(row)

def getDeptName(conn, tup):
    cur = conn.cursor()
    # query = 'SELECT * FROM dept WHERE deptno = :1'   
    # # :1(매개변수) ->  no에 따라 숫자가 바뀜 (근데 매개변수가 1개라는 뜻)
    # # deptno = 10 -> 10번만 가져와라 
    # cur.execute(query, no)
    query = 'SELECT * FROM dept WHERE deptno = :1 AND loc = :2'   
    # :1(매개변수) ->  no에 따라 숫자가 바뀜 
    # deptno = 10 -> 10번만 가져와라 
    cur.execute(query, tup)
    row = cur.fetchone()
    print(row)


if __name__ == '__main__':  # 언더바 2개씩   
    # 내가 지금 시작(사용)하는 파이썬의 파일의 네임(__name__)이 메인이라면
    # __ 애들은 .py 파일을 만들면 무조건 다 들어가 있음
    print('프로그램 시작')
    # 함수 호출
    scott_conn = myconn()    # dsn 만들고 connect() 후에 접속객체 conn을 리턴해줌
    
    print('emp 테이블 전체 조회(SELECT *)')
    getAllData(scott_conn)

    print('emp에서 2개의 컬럼 조회')
    getNameAndJobData(scott_conn)

    # no = input('1. 부서번호를 입력하세요: ')
    # loc = input('2. 지역명을 입력하세요: ').upper()
    # # print(f'부서번호 : {no}, 지역 : {loc}')
    # getDeptName(scott_conn, no, loc)

    no = input('1. 부서번호를 입력하세요: ')
    loc = input('2. 지역명을 입력하세요: ').upper()
    tup = (no, loc)
    # print(f'부서번호 : {no}, 지역 : {loc}')
    getDeptName(scott_conn, tup)

    print('프로그램 종료')

