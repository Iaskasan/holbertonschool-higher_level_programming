import http.server
import socketserver
import json
'''module to create a simple http server'''

PORT = 8000


class RequestHandler(http.server.BaseHTTPRequestHandler):
    '''class to handle requests to the server'''

    def do_GET(self):
        '''method to handle GET requests to the server'''
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "Text/html")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"404 Not Found")
            self.send_error(404, "Endpoint not found")


with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print("Serving at port:", PORT)
    httpd.serve_forever()
