import socket


def main():
    print("Logs from your program will appear here!")
    
    
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    conn, addr = server_socket.accept()
    with conn:
        val = conn.recv(1024)
        pars = val.decode()
        args = pars.split("\r\n")
        response = b"HTTP/1.1 404 Not Found\r\n\r\n"
        if len(args) > 1:
            path = args[0].split(" ")
            if path == "/":
                response = b"HTTP/1.1 200 OK\r\n\r\n"
            if "echo" in path[1]:
                string = path[1].strip("/echo/")
                response = f"HTTP/1.1 200 OK/r/n/Content-Type: text/plain/r/nContent-Length: {len(string)}\r\n\r\n{string}".encode()
            print(f"Recieved: {val}")
            conn.sendall(response)
    
     
if __name__ == "__main__":
    main()
