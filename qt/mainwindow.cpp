#include "mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    view = new QWebEngineView(this);
    view->load(QUrl("https://cges30901.github.io/test/vert2"));
    setCentralWidget(view);
}
