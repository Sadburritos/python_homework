import socket
import json


class XoServer:
    addr = None
    on_char_request = None

    def __init__(self, host, port):
        self.answer = {}
        self.addres = (host, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.sock)

    def receive(self):
        char = self.on_char_request()
        data = self.sock.recvfrom(4096)
        data = data.decode(encoding="utf-8")
        data = json.loads(data)

        self.answer = json.dumps(self.answer)

    def send(self, row, col):
        message = f'{row}, {col}'
        self.sock.sendto(message.encode(), self.addres)

    def char_response(self):
        pass
