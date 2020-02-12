#include <QWheelEvent>
#include "mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    view = new QWebEngineView(this);
    view->resize(1000, 600);
    view->load(QUrl("https://cges30901.github.io/test/vert2"));
    setCentralWidget(view);
    view->focusProxy()->installEventFilter(this);
}

bool MainWindow::eventFilter(QObject *obj, QEvent *event)
{
    if (obj == view->focusProxy() && event->type() == QEvent::Wheel) {
        QWheelEvent *wheel=static_cast<QWheelEvent *>(event);
        //The coordinate of javascript and Qt WebEngine is different.
        //In javascript, the beginning of document is 0.
        //In Qt WebEngine, the end of document is 0.
        //So I have to convert it to use javascript to scroll.
        int pos=view->page()->scrollPosition().x()-view->page()->contentsSize().width()+view->width();
        view->page()->runJavaScript(QString("window.scrollTo(%1, %2);")
                                    .arg(pos+wheel->angleDelta().y()).arg(0));
        return true;
    }
    else {
        // pass the event on to the parent class
        return QMainWindow::eventFilter(obj, event);
    }
}
