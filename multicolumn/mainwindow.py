import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtCore import QUrl, pyqtSlot


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.view = QWebEngineView(self)
        self.view.load(QUrl("https://cges30901.github.io/test/vert2"))
        self.setCentralWidget(self.view)
        self.view.loadFinished.connect(self.paginate)

    @pyqtSlot(bool)
    def paginate(self):
        self.view.page().runJavaScript('''
            var column = Math.floor(document.body.scrollWidth / document.documentElement.clientWidth);
            while(document.body.scrollWidth > document.documentElement.clientWidth){
                document.body.style.columnCount=column;
                document.body.style.height=column+"00vh";
                column++;
            }''')


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setGeometry(0, 0, 1000, 700)
    window.show()
    sys.exit(app.exec_())
