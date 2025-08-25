from bookshelf.models import Book
book = Book.objects.get(id=1)
book.title = "Nintheen eighty four"
book.title
book.save()

#Output
# <Book: Nineteen Eighty-Four by George Orwell (1949)>
