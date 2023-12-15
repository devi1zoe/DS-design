from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QVBoxLayout, QWidget

class MyApplication(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        # 创建主窗口和布局
        self.main_window = QMainWindow()

        # 创建一个堆叠窗口
        self.stacked_widget = QStackedWidget()

        # 创建页面
        page1 = QWidget()
        page2 = QWidget()
        page3 = QWidget()

        # 添加页面到堆叠窗口
        self.stacked_widget.addWidget(page1)
        self.stacked_widget.addWidget(page2)
        self.stacked_widget.addWidget(page3)

        # 创建一个 QWebEngineView 对象
        self.qwebengine = QWebEngineView()

        # 创建一个布局管理器
        layout_page3 = QVBoxLayout(page3)
        layout_page3.addWidget(self.qwebengine)

        # 将堆叠窗口设置为主窗口的中央部件
        self.main_window.setCentralWidget(self.stacked_widget)

        # 显示主窗口
        self.main_window.show()

if __name__ == "__main__":
    app = MyApplication([])
    app.exec()
