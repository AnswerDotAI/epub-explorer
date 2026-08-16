"""EPUB exploration skill for reading `.epub` books directly from the ZIP archive without extraction. It exposes the `Epx` class for opening a book, listing its table of contents, reading and searching sections as markdown, listing embedded images, and extracting images by internal EPUB path. It also allows exporting a book into notebooks for close reading.

## What this skill provides

The main public object is `Epx`, a lightweight EPUB reader class.

Typical usage:

    book = Epx()
    book.toc()
    book.section(5)
    book.search('technical future')

## Class overview

`Epx(path=None)` opens an EPUB file as a ZIP archive and loads:

- book metadata such as title and creators
- the OPF manifest
- the spine (reading order)
- NCX table-of-contents labels when available

The object representation shows the title, creators, and number of readable sections.

If a path is not provided, `Epx` will try to find a book automatically using this priority:

1. explicit `path`
2. `EPX_BOOK` environment variable
3. exactly one `.epub` file in the current directory

## Main methods

### `toc()`

Returns a plain-text table mapping spine indices to section names.

These numeric indices are used with `section(idx)`.

Example:

    book = Epx()
    print(book.toc())

### `section(idx)`

Reads one spine section by index and converts its XHTML to markdown.

This is the main method for reading book contents in LLM-friendly form.

Example:

    t = book.section(7)
    print(t)

### `search(query)`

Searches every spine section case-insensitively while ignoring markdown formatting and returns records containing the section index, line number, internal href, and matching text.

Example:

    book.search('technical future')

### `images()`

Returns a list of image paths available in the EPUB, relative to the OPF location.

These paths can be passed to `img(path)`.

Example:

    book.images()

### `img(path)`

Extracts one embedded image and returns it as a PIL image object.

Use paths returned by `images()`.

Example:

    im = book.img('images/00001.jpeg')

## Exporting to notebooks

`epx_to_nbs(book, dest='nbs')` exports each spine section of an `Epx` book as a separate Jupyter notebook under the `dest` directory. Each section's markdown is split into cells on double newlines. Filenames are slugified TOC labels prefixed with zero-padded indices (e.g. `005_chapter_i.ipynb`).

Example:

    book = Epx()
    epx_to_nbs(book, 'my_chapters')
"""

__all__ = ['Epx', 'epx_to_nbs']

from epub_explorer.epx import Epx, epx_to_nbs
