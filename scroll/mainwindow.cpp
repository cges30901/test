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
        qDebug()<<wheel->angleDelta();
        return true;
    }
    else {
        // pass the event on to the parent class
        return QMainWindow::eventFilter(obj, event);
    }
}
