from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        hour = datetime.datetime.now().hour

        if 10 <= hour < 12:
            message = "Hello from Mohan"
        elif 16 <= hour < 18:
            message = "Hello from Pankaj"
        else:
            message = "Service not available at this time"

        self.wfile.write(message.encode())

if __name__ == "__main__":
    server = HTTPServer(("", 8080), handler)
    print("Server started at port 8080...")
    server.serve_forever()

