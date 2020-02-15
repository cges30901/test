#include <QApplication>
#include <QWebEngineView>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QWebEngineView view;

    //open remote html with id is working
    //view.load(QUrl("https://cges30901.github.io/test/hash/test#p3"));

    //open local file is working
    //view.load(QUrl::fromLocalFile(a.applicationDirPath()+"/test.html"));

    //open local file with id is not working
    view.load(QUrl::fromLocalFile(a.applicationDirPath()+"/test.html#p3"));

    view.show();
    return a.exec();
}
