import sys
from PyQt6.QtCore import Qt, pyqtSignal, QThread
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QFileDialog


class WorkerThread(QThread):
    data_ready = pyqtSignal(str)

    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def run(self):
        try:
            with open(self.file_path, "r") as file:
                data = file.read()
            self.data_ready.emit(data)
        except FileNotFoundError:
            self.data_ready.emit("File not found")


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("File Reader App")
        self.setGeometry(100, 100, 400, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        self.open_button = QPushButton("Открыть")
        layout.addWidget(self.open_button)

        central_widget.setLayout(layout)

        self.open_button.clicked.connect(self.open_file)

    def open_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Text Files (*.txt);;All Files (*)",
                                                   options=options)
        if file_path:
            self.start_worker_thread(file_path)

    def start_worker_thread(self, file_path):
        self.worker_thread = WorkerThread(file_path)
        self.worker_thread.data_ready.connect(self.update_text_edit)
        self.worker_thread.start()

    def update_text_edit(self, data):
        self.text_edit.setPlainText(data)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
