#include <QWheelEvent>
#include "mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    view = new QWebEngineView(this);
    view->resize(1000, 600);
    view->load(QUrl("https://cges30901.github.io/test/vert2"));
    setCentralWidget(view);
    connect(view,&QWebEngineView::loadFinished,this,&MainWindow::scroll);
}

void MainWindow::scroll()
{
    view->page()->runJavaScript(QString("window.scrollTo(-5000, 0);"));
}
