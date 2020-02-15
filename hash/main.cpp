#include <QApplication>
#include <QWebEngineView>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QWebEngineView view;
    view.load(QUrl::fromLocalFile(a.applicationDirPath()+"/test.html"));
    view.show();
    return a.exec();
}
