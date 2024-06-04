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
                    f"Content-Length: {len(echo_message)}\r\n\r\n"
                    f"{echo_message}"
                ).encode()
                client_socket.sendall(response)
            else:
                client_socket.sendall(NOTFOUND_RESPONSE)
        else:
            client_socket.sendall(NOTFOUND_RESPONSE)
    except Exception as e:
        print(f"Error handling request: {e}")
    finally:
        client_socket.close()
        
        
def main():
    print("Logs from your program will appear here!")
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    print("Server started on localhost: 4221")
    
    
    try:
        while True:
            client_socket, _retaddr = server_socket.accept()
            handle_request(client_socket)
    except KeyboardInterrupt:
        print("Server is shutting down...")
    finally:
        server_socket.close()
        
        
if__name__=="__main__":
    main()
                    
         
