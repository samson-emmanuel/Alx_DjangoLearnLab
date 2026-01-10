# CRUD Operations Documentation

This documentation demonstrates the following commands Create, Retrieve, Update, and Delete (CRUD) operations
performed on the `Book` model using the Django shell.

---

## Create Operation

### Python Command
```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
# Expected output 
# <Book: 1984>

## Retrive Operation
book = Book.objects.filter(title="1984").first()
book.title, book.author, book.publication_year

# Expected output
# ('1984', 'George Orwell', 1949)

## Update Operation
book = Book.objects.filter(title="1984").first()
book.title = "Nineteen Eighty-Four"
book.save()
book.title

# Expected Output
# 'Nineteen Eighty-Four'


## Delete operation
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()

# Expected output
# <QuerySet []>
