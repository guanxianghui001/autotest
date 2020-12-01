import pymysql

conn = pymysql.Connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='gxh123456',
        db='yl_test',
        charset='utf8')
def get_db():

    cursor = conn.cursor()
    return cursor
def close_db():
    conn.close()
# try:
#     sql_insert1 = "insert into yl_user(user,name,password,sex,email) values ('xiaotao','小淘','123456','10B','111@qq.com')"
#     # sql_insert2 = "insert into yl_user(user,email) values ('girlfriend2','222222@qq.com')"
#     cursor.execute(sql_insert1)
#     # cursor.execute(sql_insert2)
#     conn.commit()
# except Exception as e:
#     print(e)
# conn.rollback()
# cursor.close()
# conn.close()

