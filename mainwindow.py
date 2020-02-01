import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtCore import QUrl


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.view = QWebEngineView(self)
        self.view.load(QUrl("https://cges30901.github.io/test/vert"))
        self.setCentralWidget(self.view)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setGeometry(0, 0, 1000, 700)
    window.show()
    sys.exit(app.exec_())
