from tornado.web import Application
from config import settings
from urls import urlpatterns

# import psycopg2
#import sqlite3
class NewApp(Application):
    def __init__(self):
        handlers = urlpatterns
        # 这里可填写连接数据库代码，并生成游标
        self.conn = psycopg2.connect(
                            host='localhost',
                            port=5432,
                            database='database',
                            user='username',
                            password='password'
                            )
        self.db = self.conn.cursor()

        print('服务器程序启动成功')

        print('按下 Ctrl + C 退出服务器程序')
        Application.__init__(self, handlers,**settings)
