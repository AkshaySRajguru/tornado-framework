import tornado.web
import tornado.ioloop


class BasicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World !! this is a get request returned from BasicRequestHandler.")


class ListFruitsRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class QueryParamRequestHandler(tornado.web.RequestHandler):
    """
    Accessing query parameter from url: http://localhost:8882/isEven?num=3
    """
    def get(self):
        num = self.get_argument("num")
        if num.isdigit():
            r = "odd" if int(num) % 2 else "even"
            self.write(f"The integer {num} is {r}")
        else:
            self.write(f"{num} is not a valid integer.")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", BasicRequestHandler),
        (r"/fruits", ListFruitsRequestHandler),
        (r"/isEven", QueryParamRequestHandler)
    ])

    port = 8882
    app.listen(port)
    print(f"Application is ready and listening on port {port}")
    # to make server run till one of the callbacks calls stop()
    tornado.ioloop.IOLoop.current().start()
