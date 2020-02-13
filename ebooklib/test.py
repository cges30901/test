import ebooklib
from ebooklib import epub
import os

def get_toc(input, level):
    toc=[]
    for a in input:
        if isinstance(a, tuple):
            toc.extend(get_toc(a, level))
        elif isinstance(a, list):
            toc.extend(get_toc(a, level + 1))
        else:
            toc.append([a.title, a.href, level])
    return toc

reader = epub.EpubReader('ncx.epub')
book = reader.load()
reader.process()

all_items = book.get_items()
for a in all_items:
    if isinstance(a, epub.EpubNav):
        toc_dir = os.path.dirname(a.file_name)
        break
if not toc_dir:
    all_items = book.get_items()
    for a in all_items:
        if a.get_type() == 4:
            toc_dir = os.path.dirname(a.file_name)
            break

toc = get_toc(book.toc, 0)

for a in toc:
    print(a)
