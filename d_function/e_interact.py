from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
import sys

class WebBrowserWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://csacademy.com/app/graph_editor/"))

        layout = QVBoxLayout(self)
        layout.addWidget(self.browser)

        screen_geometry = QApplication.desktop().availableGeometry()
        x_offset = 720
        y_offset = 520
        self.setGeometry(x_offset, y_offset, 1200, 600)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_pos = event.globalPos()
            self.dragging = True

    def mouseMoveEvent(self, event):
        if self.dragging:
            delta = event.globalPos() - self.start_pos
            self.move(self.mapToGlobal(delta))
            self.start_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.dragging = False

    def set_geometry(self, x, y, width, height):
        self.setGeometry(x, y, width, height)

app = QApplication(sys.argv)
window = WebBrowserWidget()

def run_application(x, y, c, k):
    window.set_geometry(x, y, c, k)
    window.show()
