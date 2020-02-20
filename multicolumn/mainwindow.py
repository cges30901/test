import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtCore import QUrl, pyqtSlot, QEvent


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.view = QWebEngineView(self)
        self.view.load(QUrl("https://cges30901.github.io/test/multicolumn/img"))
        self.setCentralWidget(self.view)
        self.view.loadFinished.connect(self.paginate)
        self.view.focusProxy().installEventFilter(self)
        self.pageIndex = 0

    def eventFilter(self, source, e):
        if source == self.view.focusProxy():
            #pos_js = self.view.page().scrollPosition().x() - self.view.page().contentsSize().width() + self.view.width()
            if e.type() == QEvent.Wheel:
                self.pageCount=round(self.view.page().contentsSize().height()/self.view.height())
                pageHeight=self.view.page().contentsSize().height()/self.pageCount
                if e.angleDelta().y() > 0:
                    if self.pageIndex > 0:
                        self.pageIndex -= 1
                elif e.angleDelta().y() < 0:
                    if self.pageIndex < self.pageCount - 1:
                        self.pageIndex += 1
                self.view.page().runJavaScript("window.scrollTo({0}, {1});"
                    .format(self.view.page().scrollPosition().x() , pageHeight * self.pageIndex))
                print(self.pageIndex,self.view.height(), self.view.page().scrollPosition().y(), self.view.page().contentsSize().height())
                return True
            else:
                return False
        return False


    @pyqtSlot(bool)
    def paginate(self):
        self.view.page().runJavaScript('''
var el = document.querySelectorAll('img');
for(var i = 0; i < el.length; i++){
    //wrap image in div so two consecutive images can be separated
    var wrapper = document.createElement('div');
    el[i].parentNode.insertBefore(wrapper, el[i]);
    wrapper.appendChild(el[i]);

    //prevent pagination failure when wide images exist
    el[i].style.maxHeight = "100%";
    el[i].style.maxWidth = document.documentElement.clientWidth + "px";
    el[i].style.margin = 0;
}
var columnInit = Math.floor(document.body.scrollWidth / document.documentElement.clientWidth);
for(var column = columnInit; column < columnInit * 2; column++){
    document.body.style.columnCount = column;
    document.body.style.height = column + "00vh";
    if(document.body.scrollWidth <= document.documentElement.clientWidth){
        break;
    }
}
//hide scroll bar
document.body.style.overflow='hidden';
''')


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setGeometry(0, 0, 1000, 700)
    window.show()
    sys.exit(app.exec_())
