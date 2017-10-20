python divoff2md.py  > md/diurnale.md
pandoc --epub-chapter-level=2 --epub-stylesheet=style.css --epub-cover-image=img/cover.png --epub-metadata=meta.xml --toc-depth=2 -o diurnale.epub md/diurnale.md
kindlegen diurnale.epub
open diurnale.epub
