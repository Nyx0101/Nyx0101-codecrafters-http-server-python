import socket
import re


OK_RESPONSE = "HTTP/1.1 200 OK\r\n\r\n".encode()
NOTFOUND_RESPONSE = "HTTP/1.1 404 Not Found\r\n\r\n".encode()

def handle_request(client_socket):
    try:
        request = client_socket.recv(1024).decode()
        if not request:
            return
            
        print(f"Received request: {request}")
        
        
        match = re.search(r"GET (.*) HTTP", request)
        if match:
            url = match.group(1)
            print(f"Parsed URL: {url}")
            
            if url == "/":
                client_socket.sendall(OK_RESPONSE)
            elif url. startswith("/echo/"):
                echo_message = url[6:]
                response = (
                    f"HTTP/1.1 200 OK\r\n"
                    f"Content-Type: text/plain\r\n"
         
