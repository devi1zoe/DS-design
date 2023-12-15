from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QFileDialog
from PySide6.QtGui import QPixmap, QRegion


def take_snapshot(table_widget):
    # 使用 QWidget.grab() 获取整个表单的截图
    pixmap = table_widget.grab()
    # 渲染 table widget 到 QPixmap
    table_widget.render(pixmap)
    # 保存截图到文件
    file_dialog = QFileDialog()
    file_path, _ = file_dialog.getSaveFileName(None, "Save Image", "", "Images (*.png);;All Files (*)")
    if file_path:
        pixmap.save(file_path, "PNG")

