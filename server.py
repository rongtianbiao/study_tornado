import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line

define("port", default=8000, type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        name = self.get_argument("name", "xiaoming")
        self.write("hello %s"%name)


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