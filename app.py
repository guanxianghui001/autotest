from flask import Flask
from sqlalchemy import create_engine, Table
app = Flask(__name__)

# engine = create_engine('mysql://root:gxh123456@localhost:3306/yl_test')
# # 配置数据库的地址
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:gxh123456@localhost:3306/yl_test'
#
# # 跟踪数据库的修改 --> 不建议开启 未来的版本中会移除
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# #查询时会显示原始SQL语句
# # app.config['SQLALCHEMY_ECHO'] = True
#
# # 创建数据库对象
# db = SQLAlchemy(app)
# def add_date():
#     user1=yl_user(user='xiaoyu',name='小玉',password='123456',sex='10B')
#     db.session.add(user1)
#     db.session.commit()
# add_date()
import pymysql

conn = pymysql.Connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='gxh123456',
        db='yl_test',
        charset='utf8')
cursor = conn.cursor()
try:
    sql_insert1 = "insert into yl_user(user,name,password,sex,email) values ('xiaotao','小淘','123456','10B','111@qq.com')"
    # sql_insert2 = "insert into yl_user(user,email) values ('girlfriend2','222222@qq.com')"
    cursor.execute(sql_insert1)
    # cursor.execute(sql_insert2)
    conn.commit()
except Exception as e:
    print(e)
conn.rollback()
cursor.close()
conn.close()


@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/login')
def login():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
