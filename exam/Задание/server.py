import socket
import json


class XoServer:
    on_char_request = None

    def __init__(self, host, port):

        self.answer = {}
        self.addres = (host, port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    def receive(self):
        char = self.on_char_request()
        data = self.sock.recvfrom(4096)
        # data = data.decode(encoding= "utf-8")
        data = json.loads(data.decode(encoding= "utf-8"))



        self.answer = json.dumps(self.answer)

    def send(self):







"""
import socket
from logger import log
from message import Message


class UdpReceiver(QThread):
    message = pyqtSignal(Message)
    hello = pyqtSignal(Message)

    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        hostname = socket.gethostname()
        ip_adr = socket.gethostbyname(hostname)
        self.addres = (ip_adr, 9900)
        self.running = False
        

    def run(self):
        log.i("Ресивер запущен")
        self.socket.bind(self.addres)
        self.running = True
        while self.running:
            data, addr = self.socket.recvfrom(4096)
            received_string = data.decode(encoding= "utf-8")
            log.d(f'получено сообщение от {addr}: {received_string}')
            msg = Message(received_string)
            msg.senderIP = addr[0]
            if msg.type == 'service_request' and msg.text.lower() == 'hello':
                self.hello.emit(msg)
            else:
                self.message.emit(msg)

    def stop(self):
        self.running = False
        super().stop()
"""