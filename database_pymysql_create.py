import pymysql

#连接数据库
db = pymysql.connect(
    host='10.13.2.4',
    port=3307,
    user='root',
    passwd='123456',
    database='mydb',
    charset='utf8')

#获取操作游标
cursor = db.cursor()
#数据库操作语句
sql = """
    create table employeetest(
    first_name char(20) not null,
    last_name char(20),
    age int,
    sex char(1),
    income float)
"""
#执行SQL语句
cursor.execute(sql)
#关闭数据库连接
db.close()

