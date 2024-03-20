import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

html_content = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <title>Python Docker</title>
  </head>
  <body>
    <h1>¡Hola mundo sin flask desde un docker!</h1>
  </body>
</html>
"""

class HTMLServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html_content.encode())

def run(server_class=HTTPServer, handler_class=HTMLServer, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor HTTP sirviendo en el puerto {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
