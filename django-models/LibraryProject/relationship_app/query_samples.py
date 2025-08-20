import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"\nBooks by {author.name}:")
        for book in books:
            print("-", book.title)
    except Author.DoesNotExist:
        print(f"No author found with name '{author_name}'")