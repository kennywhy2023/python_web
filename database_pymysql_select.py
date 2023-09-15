import pymysql

# 连接数据库
db = pymysql.connect(
    host='10.13.2.4',
    port=3307,
    user='root',
    passwd='123456',
    database='mydb',
    charset='utf8')

# 获取操作游标
cursor = db.cursor()
# 数据库查询语句
sql = " select * from employeetest \
        where income > %f" % (500)

try:
    # 执行SQL语句
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s, lname=%s, age=%s, sex=%s, income=%s" %
            (fname, lname, age, sex, income))
except BaseException:
    print("Error: unable to fetch data")
# 关闭数据库连接
db.close()
