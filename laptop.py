from http.server import BaseHTTPRequestHandler, HTTPServer
import os

HOST = "0.0.0.0"
PORT = 5000

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/open":
            os.system("xdg-open ~/Desktop/zubair.html")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"HTML Opened")

        elif self.path == "/close":
            os.system("pkill firefox")
            os.system("pkill chromium")
            os.system("pkill chrome")

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Browser Closed")

        else:
            self.send_response(404)
            self.end_headers()

server = HTTPServer((HOST, PORT), MyServer)

print("Server Running...")
print("Port:", PORT)

server.serve_forever()
