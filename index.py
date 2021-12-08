import tornado.web
import tornado.ioloop


class BasicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World !! this is a get request returned from BasicRequestHandler.")


class ListFruitsRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", BasicRequestHandler),
        (r"/fruits", ListFruitsRequestHandler),
    ])

    port = 8882
    app.listen(port)
    print(f"Application is ready and listening on port {port}")
    # to make server run till one of the callbacks calls stop()
    tornado.ioloop.IOLoop.current().start()
