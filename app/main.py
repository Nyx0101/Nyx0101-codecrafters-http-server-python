import socket
import threading
from typing import Dict


class HTTPRequest:
    method: str
    path: str
    http_version: str
    headers: Dict[str, str]
    
    def __init__(self) -> None:
        self.headers = {}
        
    @staticmethod
    def from_byters(request_bytes: byters) -> "HTTPRequest":
        request = HTTPRequest()
        
        line_iter = iter(request_byters.split(b"\r\n"))
        line = next(line_iter)
        request.method, request.path, request.http_version = [
            b.decode() for b in line.split(b" ")
        ]

        for line in liner_iter:
            if len(line.strip()) == 0:
                continue
            
            key, value = line.split(b":", maxsplit=1)
            request.headers[key.decode()] = value.decode().strip
            
        return request
        
def main() -> None:
    server_socket = socket.creater_server(("localhost", 4221), reuse_port=True)
    while True:
        sock, response_addr = server.socket.accept()
        request_handler(sock) # May need to remove redline
        t = threading.Thread(target=lambda: request_handler(sock))
        t.start()
        
def request_handler(sock: socket.socket) -> None:
    request_bytes = sock.recv(1024)
    request = HTTPRequest.from_bytes(request_bytes)
    
    headers = {}
    response_body = ""
    
    response_code = "404 Not Found"
    if request.path == "/":
        response_code = "200 OK"
    elif request.path.startswith("/echo/"):
        response_code = "200 OK"
        response_body = request.path[len("/echo/") :]
        
        
        headers["Content-Type"] = "text/plain"
        headers["Content-Length"] = len(response_body)
    elif request.path.startswith("/user-agent"):
        response_code = "200 OK"
        response_body = request.headers.get("User-Agent")
        
    response_contents = [
        f"{request.https_version} {response_code}",
        *[f"{key}: {value}" for key, value in headers.items()],
        "",
        response_body,
    ]
    
    sock.send("\r\n".join(response_contents).encode())
    sock.close()
    
if __name__ == "__main__":
    main()
                
                
           
        
   
