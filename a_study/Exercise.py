# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QWidget
# from PySide6.QtCore import Qt
#
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         btn = QPushButton('按钮',self)
#         btn.setGeometry(100,100,200,100)
#         btn.setToolTip('提示')
#         btn.setText('重新设置的按钮')
#         btn.clicked.connect(self.hello)
#
#         lb = QLabel('标签',self)
#         lb.setText('重新设置的文字')
#         lb.setAlignment(Qt.AlignmentFlag.AlignCenter)
#
#         line = QLineEdit(self)
#         line.setPlaceholderText('请输入内容')
#         line.setGeometry(100, 220, 200, 30)
#
#     def hello(self):
#             print('hello world')
#
# if __name__ == '__main__':
#     app = QApplication([])
#     window = MyWindow()
#     window.show()
#     app.exec()
















# #login项目
# from PyQt6.QtWidgets import QApplication, QWidget
# from login import Ui_Form
#
#
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.ui = Ui_Form()
#         self.ui.setupUi(self)
#
#         self.ui.pushButton.clicked.connect(self.loginFuc)
#
#     def loginFuc(self):
#         account = self.ui.lineEdit.text()
#         password = self.ui.lineEdit_2.text()
#
#         if account == 'admin' and password == '123456':
#             print('success')
#         else:
#             print('false')
#
#
# if __name__ == '__main__':
#     app = QApplication([])
#     window = MyWindow()
#     window.show()
#     app.exec()













# #calculate项目
# from PyQt6.QtWidgets import QApplication, QWidget
# from calculate import Ui_Form
#
#
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.ui = Ui_Form()
#         self.ui.setupUi(self)
#
# if __name__ == '__main__':
#     app = QApplication([])
#     window = MyWindow()
#     window.show()
#     app.exec()















# from PyQt6.QtWidgets import QApplication, QWidget, QComboBox,QVBoxLayout
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         # 复选框
#         cb = QComboBox()
#         cb.addItems(['信息安全','计算机科学与技术','物联网技术'])
#         cb.currentIndexChanged.connect(lambda: print(cb.currentText()))
#         #布局
#         mainlayout = QVBoxLayout()
#         mainlayout.addWidget(cb)
#         self.setLayout(mainlayout)
#
# if __name__ == '__main__':
#     app = QApplication([])
#     window = MyWindow()
#     window.show()
#     app.exec()







# # 单选框 + 按钮
# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QPushButton
#
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         cb = QCheckBox('是否被选中')
#         cb.stateChanged.connect(self.on_checkbox_state_changed)
#
#         btn = QPushButton('获取状态')
#         btn.clicked.connect(lambda: print(cb.isChecked()))
#
#         # 布局
#         mainlayout = QVBoxLayout()
#         mainlayout.addWidget(cb)
#         mainlayout.addWidget(btn)
#         self.setLayout(mainlayout)
#
#     def on_checkbox_state_changed(self, state):
#         if state == 2:  # 2 表示选中状态
#             print('被选中')
#         else:
#             print('未被选中')
#
# if __name__ == '__main__':
#     app = QApplication([])
#     window = MyWindow()
#     window.show()
#     app.exec()

















# 单选的点，只能选一个----Groupbox
# zeal