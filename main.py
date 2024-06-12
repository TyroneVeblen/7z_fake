import os
import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QThread, Signal

from basetools import get_file_list
from ui.MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QWidget


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.status = None
        self.worker = None
        self.setupUi(self)
        self.folder = ""
        self.select_folder_button.clicked.connect(self.select_folder)
        self.start.clicked.connect(self.main)

    def select_folder(self):
        self.folder = QFileDialog.getExistingDirectory(QWidget())
        self.lineEdit.setText(self.folder)

    def main(self):
        file_list = get_file_list(self.folder)
        self.progressBar.setRange(0, len(file_list))
        current_text = self.comboBox.currentText()
        self.status = {"s": True}
        self.worker = progress_bar(file_list, current_text, self.status)
        self.worker.trigger.connect(self.setValue)
        if self.start.text() == "开始":
            self.worker.start()
            self.start.setText("结束")
        else:
            self.start.setText("开始")
            self.status = {"s": False}

    def setValue(self, num):
        self.progressBar.setValue(num)
        if self.progressBar.maximum() == num:
            self.start.setText("开始")


class progress_bar(QThread):
    trigger = Signal(int)

    def __init__(self, file_list, current_text, status):
        super().__init__()
        self.file_list = file_list
        self.current_text = current_text
        self.status = status

    def run(self):
        i = 0
        for file in self.file_list:
            if self.status["s"]:
                with open(file, "rb+") as f:
                    bytes_string = f.read(6)
                    ture_hander = bytes.fromhex("377abcaf271c")
                    fake_hander = bytes.fromhex("384c971b4377")
                    f.seek(0)
                    if self.current_text == "修改":
                        if bytes_string == fake_hander:
                            pass
                        else:
                            if file.split(".")[-1] == "7z":
                                f.write(fake_hander)
                    else:
                        if bytes_string == ture_hander:
                            pass
                        else:
                            f.write(ture_hander)
                i += 1
                self.trigger.emit(i)
            else:
                break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
