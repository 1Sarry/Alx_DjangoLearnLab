import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"\nBooks in {library.name}:")
        for book in books:
            print("-", book.title)
           
    except Author.DoesNotExist:
        print(f"No library found with the name '{library_name}'")

def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"\nBooks by {author.name}:")
        for book in books:
            print("-", book.title)
    except Author.DoesNotExist:
        print(f"No author found with name '{author_name}'")


def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library_name)
        print(f"\nLirarian for {library.name}: {librarian.name}")
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print(f"No libraria found for library '{library_name}'")