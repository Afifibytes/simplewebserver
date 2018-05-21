from http.server import HTTPServer, BaseHTTPRequestHandler
from generator import Generator
from winning import winning_type

class RequestHandler(BaseHTTPRequestHandler):
    """
    request handler class for the HTTP request
    """
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            randNumbers = connectionListOfRandNumbers()
            self.wfile.write(bytes(str(randNumbers), "utf8"))
            self.wfile.write(bytes(winning_type(randNumbers), "utf8"))


def connectionListOfRandNumbers():
    """
    setting up the list of random numbers for the connection response
    """
    start = 0
    end = 10
    elements = 3

    try:
        number_generator = Generator(elements, start, end)
        listOfNumbers = number_generator.generate()
    except TypeError:
        listOfNumbers = [0, 0, 0]

    return listOfNumbers

def run():
    """
    running the web server and setting its configurations
    """
    print("starting server ...")

    port = 8080
    server_address = ('localhost', port)
    httpd = HTTPServer(server_address, RequestHandler)

    print("running server on port {}".format(port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("shutting down server ...")
        httpd.socket.close()


