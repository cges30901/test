import ebooklib
from ebooklib import epub
import os

def get_item_from_tuple(tup, level, toc_dir):
    toc=[]
    for a in tup:
        if isinstance(a, tuple):
            toc.extend(get_item_from_tuple(a, level))
        elif isinstance(a, list):
            toc.extend(get_item_from_tuple(a, level + 1))
        else:
            print(a.href,os.path.normpath(os.path.join(toc_dir, a.href)))
            item = book.get_item_with_href(a.href.split('#')[0])
            toc.append([a.title, os.path.join(reader.opf_dir, item.file_name), level])
    return toc

reader = epub.EpubReader('level.epub')
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
toc=[]
print(book.toc[0][0].href)
for a in book.toc:
    if isinstance(a, tuple):
        toc.extend(get_item_from_tuple(a, 0, toc_dir))
    else:
        item = book.get_item_with_href(a.href.split('#')[0])
        toc.append([a.title, os.path.join(reader.opf_dir, item.file_name), 0])



#for a in book.toc:
#    print(os.path.normpath(os.path.join(ncx_dir, a.href)))
