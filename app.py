import http.server
import socketserver
import os

PORT = 7860

class CustomHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Reads and serves index.html from your repository
        if os.path.exists("index.html"):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("index.html", "rb") as f:
                self.wfile.write(f.read())
        else:
            self.send_error(404, "index.html not found in repository")

if __name__ == "__main__":
    print(f"==> Serving index.html on 0.0.0.0:{PORT}...")
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("0.0.0.0", PORT), CustomHTTPHandler) as httpd:
        httpd.serve_forever()
