import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
django.setup()

from relationship_app.models import Library

all_books = Library.object.all()
print('all Libarary')
for lib in Library:
  print(lib.books)
