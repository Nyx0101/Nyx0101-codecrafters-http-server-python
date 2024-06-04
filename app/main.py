import socket


def main():

 
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    client, addr  = server_socket.accept()
    
    data = client.recv(1024).decode()
    print(f"Received data: {data}")
    
    req = data.split("\r\n")
    if len(req) > 0:
        path = req[0].split(" ")[1]
        print(f"Parsed path:{path}")
        
        if path =="/":
            response = "HTTP/1.1 200 OK\r\n\r\n".encode()
        elif path.startswith("\echo"):
            echo_message = path[6:]
            response = (f"HTTP/1.1 200 OK\r\n"
                        f"Content-Type: text/plain\r\n"
                        f"Content-Length: {len(echo_message)}\r\n\r\n"
                        f"{echo-message}").encode()
        elif path.startswith("/user-agent"):
            user_agent = ""
                for header in req:
                    if header.startswith("User-Agent"):
                        user_agent = header.split(": ")[1]
                        break
                if user_agent:
                    response = (f"HTTP/1.1 200 OK\r\n"
                                f"Content-Type: text/plain\r\n"
                                f"Content-Length: {len(user_agent)}\r\n\r\n"
                                f"{user_agent}").encode()
                else:
                    response = "HTTP/1.1 404 Not Found\r\n\r\n".encode()
            else:
                response = "HTTP/1.1 404 Not Found\r\n\r\n".encode()
                
            print(f"Sending response: {response.decode()}")
            client.send(response)
        else:
            print("No request data received.")
            response = "HTTP/1.1 400 Bad Request\r\n\r\n".encode()
            client.send(response)
            
        client.close()
        print("Connection closed")
        
if__name__ == "__main__":
    main()
        
   
