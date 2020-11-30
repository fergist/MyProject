from PyQt5.QtWidgets import QWidget, QApplication
import sys

class EX(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,1000,800)

app = QApplication(sys.argv)
b = EX()
b.show()
sys.exit(app.exec())