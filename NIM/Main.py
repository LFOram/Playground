import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__=="__main__":
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(800, 800)
    w.move(550, 120)
    w.setWindowTitle('Digital NIM')
    w.show()

    sys.exit(app.exec_())
