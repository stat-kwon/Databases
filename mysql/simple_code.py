import pymysql

# 1. mysql에 접속해준다.
db_conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'seolmin',
    passwd = 'seolmin',
    db = 'blog_db',
    charset = 'utf8'
)

# 2. 잘 연결 되었는지 확인
seol_db = db_conn.cursor()
print('seol_db:',seol_db)

# sql = "drop table user_info;"
# seol_db.execute(sql)
# db_conn.commit()

# 3. table이 있는지 없는지 확인(있으면 1 없으면 0가 return 됨)
sql = "show tables;"
print(seol_db.execute(sql))

# 4. 테이블 생성
sql = """
CREATE TABLE user_info (
    USER_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    USER_EMAIL VARCHAR(100) NOT NULL,
    BLOG_ID CHAR(4),
    PRIMARY KEY(USER_ID)
);
"""
seol_db.execute(sql)
db_conn.commit() # 데이터베이스를 변경하는 명령은 commit() 해주기

# 5. record 생성
user_email = 'test@test.com'
blog_id = 'A'

sql = "INSERT INTO user_info (USER_EMAIL, BLOG_ID) VALUES ('%s', '%s')" % (str(user_email), str(blog_id))
seol_db.execute(sql)
db_conn.commit()

sql = "SELECT * FROM user_info"
seol_db.execute(sql)
results = seol_db.fetchall()
for result in results:
    print (result, type(result))