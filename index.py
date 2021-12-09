import json

import tornado.web
import tornado.ioloop


# class BasicRequestHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, World !! this is a get request returned from BasicRequestHandler.")


class MainRequestHandler(tornado.web.RequestHandler):
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


class ResourceParamRequestHandler(tornado.web.RequestHandler):
    """
    Parameters passed from regex will be arguments for HTTP methods.
    e.g. studentName, courseId for get method
    Accessing resource parameter from url: http://localhost:8882/students/akshay/12
    Output: Welcome akshay you are viewing course 12
    """
    def get(self, studentName, courseId):
        self.write(f"Welcome {studentName} you are viewing course {courseId}")


class TextFileRequestHandler(tornado.web.RequestHandler):
    def get(self):
        fh = open("fruits_list.txt", "r")
        fruits = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(fruits))

    def post(self):
        """
        tested via postman: http://localhost:8882/textFile?fruit=Lemon
        """

        fruit = self.get_argument("fruit")
        fh = open("fruits_list.txt", "a")
        fh.write(f"{fruit}\n")
        fh.close()
        self.write(json.dumps({"message": "Fruit added successfully."}))


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", MainRequestHandler),
        (r"/isEven", QueryParamRequestHandler),
        (r"/students/([a-z]+)/([0-9]+)", ResourceParamRequestHandler),
        (r"/textFile", TextFileRequestHandler)
    ])

    port = 8882
    app.listen(port)
    print(f"Application is ready and listening on port {port}")
    # to make server run till one of the callbacks calls stop()
    tornado.ioloop.IOLoop.current().start()
