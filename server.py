import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from controllers import  ControllerClass
from dotenv import load_dotenv
import json
from urllib.parse import urlparse
load_dotenv()


#Defining a HTTP request Handler class
class ServiceHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/json')
        self.end_headers()
        get_url = urlparse(self.path)
        query = get_url.query
        get_param = dict(qc.split("=") for qc in query.split("&"))

        if get_url.path == '/property':
            # se llama el metodo que procesa la logica de los property.
            data= ControllerClass.list_property(self, get_param)
                    
        # Escribir respuesta para el cliente.
        self.wfile.write(json.dumps(data).encode())
		
    
def main():
    PORT = int(os.getenv('PORT'))    			
    server = HTTPServer(('127.0.0.1',PORT), ServiceHandler)
    print(f'Server Initialization in port {PORT}') 
    server.serve_forever()


if __name__ == '__main__':
    main()