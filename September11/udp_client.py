import socket


class UDP_Client:
    def __init__(self, server_port):
        self.server_port = server_port
        self.server_address = ("localhost", self.server_port)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, message):
        self.client_socket.sendto(message.encode(), self.server_address)

    def receive(self):
        data, addr = self.client_socket.recvfrom(1024)
        response = data.decode()
        return response


client = UDP_Client(9900)
while True:
    message = input("Введите сообщение для отправки (или 'exit' для выхода): ")
    if message.lower() == "exit":
        break
    client.send(message)
    response = client.receive()
    print(f"Ответ от сервера: {response}")
