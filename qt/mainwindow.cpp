#include <QResizeEvent>
#include "mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    view = new QWebEngineView(this);
    view->resize(1000, 600);
    view->load(QUrl("https://cges30901.github.io/test/vert2"));
    qDebug()<<"size: "<<view->page()->contentsSize();
    setCentralWidget(view);
    view->installEventFilter(this);
}

bool MainWindow::eventFilter(QObject *obj, QEvent *event)
{
    if (obj == view && event->type() == QEvent::Resize) {
        qDebug()<<"size: "<<view->page()->contentsSize();
        return true;
    }
    else {
        // pass the event on to the parent class
        return QMainWindow::eventFilter(obj, event);
    }
}
