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

sql = "show tables;"
print(seol_db.execute(sql))