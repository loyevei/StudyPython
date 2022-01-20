# bbokrentalshop.py
# divtbl, membertbl
import cx_Oracle as ora

def myconn():
    dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')
    conn = ora.connect(user ='scott', password = 'tiger', dsn = dsn, encoding = 'utf-8')
    return conn

def getAllDataFromDivtbl(conn):
    cur = conn.cursor()
    query = 'SELECT * FROM divtbl'
    for row in cur.execute(query):
        print(row)

def setDataIntoDivtbl(conn, tup):
    cur = conn.cursor()
    query = '''INSERT INTO divtbl (division, names) 
               VALUES (:1, :2)'''
    cur.execute(query, tup)
    # cur.close()
    conn.commit()    # COMMIT; 필수 DB에서의 커밋과 같음 / ROLLBECK도 있음

# membertbl에서 일부 데이터 가져오기
def getSomeDataFromMembertbl(conn):
    cur = conn.cursor()
    query = '''SELECT names, levels, addr, mobile, email 
                 FROM membertbl
                WHERE addr LIKE '서울%'
                  AND UPPER(email) LIKE '%@NAVER.COM'
                ORDER BY idx DESC'''
    for row in cur.execute(query):
        print(row)

    cur.close()

# membertbl에 신규회원 등록하기
def setNewMemberIntoMembertbl(conn, tup):
    cur = conn.cursor()
    query = '''SELECT ROWNUM, idx
                FROM (
                    SELECT idx FROM membertbl
                    ORDER BY idx DESC  
                        ) 
                WHERE ROWNUM = 1'''
    cur.execute(query)
    idx = cur.fetchone()
    if idx is None:
        idx = 0
    else:
        idx = idx[1]

    intup = (idx+1, tup[0], tup[1], tup[2], tup[3])

    query = '''INSERT INTO membertbl 
                       (idx, names, levels, userid, password)
               VALUES  (:1, :2, :3, :4, :5)'''
    
    cur.execute(query, intup)
    conn.commit()

def setChangeMemberFromMembertbl(conn, tup):
    cur = conn.cursor()
    query = '''UPDATE membertbl
                  SET addr = :1
                    , mobile = :2
                    , email = :3
                WHERE idx = :4'''
    cur.execute(query, tup)
    cur.close()
    conn.commit()

def deleteDivision(conn, division):
    cur = conn.cursor()
    query = 'DELETE FROM divtbl WHERE division = :1'
    cur.execute(query, (division, ))   
    # 데이터가 하나면 튜플로 변경. ',' 를 반드시 넣어줘야 함!!!
    conn.commit()


if __name__ == '__main__':
    print('책 대여점 프로그램 시작')
    scott_conn = myconn()   # DB접속
    # 1. divtbl에서 데이터 조회
    # print('책 장르 정보조회')
    # getAllDataFromDivtbl(scott_conn)
    # 2. divtbl에 새로운 데이터 입력
    # print('책 장르 정보 입력')
    # division = input('구분 코드 입력: ')
    # names = input('장르명 입력: ')
    # tup = (division, names)
    # setDataIntoDivtbl(scott_conn, tup)
    # print('정보 입력 성공')
    # 3. membertbl에서 데이터 조회
    # getSomeDataFromMembertbl(scott_conn)
    # 4. membertbl에 새 데이터 입력
    # print('신규 회원 입력')
    # names = input('이름 입력: ')
    # levels = input('레벨 입력(A~D): ')
    # userid = input('아이디 입력(최대 20자): ')
    # password = input('패스워드 입력(최대 20자): ')
    # tup = (names, levels, userid, password)
    # setNewMemberIntoMembertbl(scott_conn, tup)
    # print('신규회원 저장성공')
    # 5. membertbl 새 데이터 수정
    # print('기존 회원 수정')
    # idx = input('변경회원번호: ')
    # addr = input('주소 입력: ')
    # mobile = input('폰번호 입력(-포함): ')
    # email = input('이메일 입력: ')
    # tup = (addr, mobile, email, idx)
    # setChangeMemberFromMembertbl(scott_conn, tup)
    # print('기존 회원 수정완료')
    # 6. divtbl에 임의 데이터 삭제
    print('책 장르정보 삭제')
    division = input('삭제할 장르코드 입력: ')
    deleteDivision(scott_conn, division)
    print('삭제 성공')

