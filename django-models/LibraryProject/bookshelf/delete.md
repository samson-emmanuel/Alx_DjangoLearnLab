from bookshelf.models import Book

book=Book.object.filter(title="Nineteen Eighty-Four")
book.delete()
Book.object.all()