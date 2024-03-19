# Importar los módulos necesarios
import http.server
import socketserver

# Definir una clase que herede de SimpleHTTPRequestHandler
class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    # Sobrescribir el método do_GET para manejar las solicitudes GET
    def do_GET(self):
        # Enviar una respuesta de estado 200 (OK)
        self.send_response(200)
        # Establecer la cabecera Content-type como texto/html
        self.send_header('Content-type', 'text/html')
        # Finalizar las cabeceras
        self.end_headers()
        # Escribir en el flujo de salida el contenido que queremos enviar, en este caso, "Hello, World!"
        self.wfile.write(b"Hello, World!")

# Definir el puerto en el que se ejecutará el servidor
PORT = 5000

# Asignar la clase SimpleHTTPRequestHandler al Handler
Handler = SimpleHTTPRequestHandler

# Crear un servidor TCP en el puerto especificado que maneje las solicitudes con el Handler definido
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    # Imprimir un mensaje indicando que el servidor está activo y escuchando en el puerto especificado
    print("Servidor activo en el puerto", PORT)
    # Iniciar el servidor y mantenerlo ejecutándose de forma indefinida
    httpd.serve_forever()
