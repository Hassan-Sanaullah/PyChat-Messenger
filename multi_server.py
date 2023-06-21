import socket
from threading import Thread
from server_action import main_action

def handle_client(client_socket):
    while True:
                # Receive data from the client
                data = client_socket.recv(1024).decode()
                print("Received from client:", data)

                if not data:
                    # No more data, break the loop
                    break
                
                # Pass data to the action function in server_action.py
                response = main_action(data)

                # Process the data or perform any required operations
                # Send a response to the client
                client_socket.sendall(response.encode())

                

            # Close the client socket
    client_socket.close()
    print("Client connection closed.")

def main():
    # Server IP and port
    server_ip = "127.0.0.1"
    server_port = 8080

    # Create a TCP server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind the socket to the server address
        server_socket.bind((server_ip, server_port))

        # Listen for incoming connections
        server_socket.listen(1)
        print("Server is listening for incoming connections...")

        while True:
            # Accept a client connection
            client_socket, client_address = server_socket.accept()
            print("Connected to client:", client_address)

            # Create a new thread to handle the client connection
            client_thread = Thread(target=handle_client, args=(client_socket,))
            client_thread.start()

    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        # Close the server socket
        wait = input("Enter anything to continue")
        server_socket.close()

main()