#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QWebEngineView>

class MainWindow : public QMainWindow
{
    Q_OBJECT
    QWebEngineView *view;

public:
    MainWindow(QWidget *parent = nullptr);
};
#endif // MAINWINDOW_H
