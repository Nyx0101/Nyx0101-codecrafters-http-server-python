import socket
import threading
import logging

logging .basicConfig(level=logging.INFO)

def handle_client(client_socket):
    try:
        request = client_socket.recv(4096)
        if not request:
            return        
        request = request.decode("utf-8")
        logging.info(f"Received request: {request}")      
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/plain\r\n\r\n"
        response_length = len(response.encode("utf-8"))
        response += "Content-Length: {}\r\n\r\n".format(response_length)
        response += "Hello, World!\r\n"
        client_socket.sendall(response.encode("utf-8"))
    except Exception as e:
        logging.error(f"Error handling client: {e}")
    finally:
        client_socket.close()
    
def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    logging.info("Server started")
    
    while True:
        conn, address = server_socket.accept()
        logging.info(f"Connected by {address}")
        client_thread = threading.Thread(target=handle_client, args=(conn,))
        client_thread.start()
        
if __name__ == "__main__":
    main()
    
    

                
                
           
        
   
