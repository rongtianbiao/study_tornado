import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line
import tornado.httpserver

define("port", default=8000, type=int)


class MainHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.name = "python"
        print("实例对象的初始化方法，并给name参数赋值")

    def prepare(self):
        print("在执行HTTP行为方法之前被调用")

    def get(self, *args, **kwargs):
        print("执行get方法")
        self.write("hello %s"%self.name)

    def on_finish(self):
        print("响应后调用此方法")


def make_app():
    return tornado.web.Application([
        (r'/hello', MainHandler)
    ])


if __name__=="__main__":
    # 解析命令行
    parse_command_line()

    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()