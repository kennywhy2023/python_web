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
    insert into employeetest(first_name,
    last_name,age,sex,income)  
    values('mac', 'Mohan', 20, 'M', 500);
"""
try:
    #执行SQL语句
    cursor.execute(sql)
    #提交到数据库执行
    db.commit()
except:
    db.rollback()
    print('Error to insert data.')
#关闭数据库连接
db.close()

