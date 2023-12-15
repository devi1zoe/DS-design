import sys
from c_Interface.modules import resources
from c_Interface.modules import *
from c_Interface.page import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("c_Interface/images/images/icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
