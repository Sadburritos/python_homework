import socket


class UDP_Server:
    def __init__(self, port):
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind(('0.0.0.0', self.port))

    def start(self):
        print(f"UDP server is listening on port {self.port}")
        while True:
            data, addr = self.server_socket.recvfrom(1024)
            message = data.decode()
            print("Received message: {message}")
            self.server_socket.sendto(b"OK", addr)

    def stop(self):
        self.server_socket.close()


server = UDP_Server(9900)
server.start()
