from tornado.web import Application
from tornado.web import RequestHandler
import tornado.ioloop
from tornado.httpserver import HTTPServer
from tornado.options import options, define, parse_command_line
import torndb
import redis
from study_tornado import config

define("port", default=9999, type=int, help="端口号")


class Application(Application):
    """增加redis和db属性"""
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.db = torndb.Connection(host="localhost", database="ihome", user="root", password="3535")
        self.redis = redis.StrictRedis(host="127.0.0.1", port=6379, db=0)


class BaseRequestHandler(RequestHandler):
    """扩充RequestHandler类的方法"""
    @property
    def db(self):
        return self.application.db

    @property
    def redis(self):
        return self.application.redis


class IndexHandler(BaseRequestHandler):
    def get(self):
        print(self.redis.get("a"))
        # cursor = self.db.cursor()
        # cursor.execute("show tables;")
        # print(cursor.fetchall())
        self.write("ok")


if __name__=="__main__":
    parse_command_line()
    app = Application([
        (r'^/', IndexHandler)
    ],
        debug=True
    )
    http_server = HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.current().start()




