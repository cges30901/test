import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtCore import QUrl, pyqtSlot, QEvent


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.view = QWebEngineView(self)
        self.view.load(QUrl.fromLocalFile("/home/manjaro/project/epub/ol.epub_FILES/OEBPS/Text/text02.xhtml"))
        self.setCentralWidget(self.view)
        self.view.loadFinished.connect(self.paginate)
        self.view.focusProxy().installEventFilter(self)
        self.pos = 0

    def eventFilter(self, source, e):
        if source == self.view.focusProxy():
            #pos_js = self.view.page().scrollPosition().x() - self.view.page().contentsSize().width() + self.view.width()
            if e.type() == QEvent.Wheel:
                col=self.view.page().contentsSize().height()//self.view.height()
                height=self.view.page().contentsSize().height()/col
                #print(height)
                if e.angleDelta().y() > 0:
                    self.pos -= height
                    if self.pos<0:
                        self.pos=0
                    self.view.page().runJavaScript("window.scrollTo({0}, {1});"
                        .format(self.view.page().scrollPosition().x() , self.pos))
                else:
                    self.pos += height
                    if self.pos>self.view.page().contentsSize().height()-self.view.height():
                        self.pos=self.view.page().contentsSize().height()-self.view.height()
                    self.view.page().runJavaScript("window.scrollTo({0}, {1});"
                        .format(self.view.page().scrollPosition().x() , self.pos))
                print(self.pos, self.view.page().scrollPosition().y(), self.view.page().contentsSize().height())
                return True
            else:
                return False
        return False
                

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
