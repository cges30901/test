import ebooklib
from ebooklib import epub
import os


reader = epub.EpubReader('saw.epub')
book = reader.load()
for a in book.toc:
    item = book.get_item_with_href(a.href.split('#')[0])
    print(a.title, os.path.join(reader.opf_dir, item.file_name))
