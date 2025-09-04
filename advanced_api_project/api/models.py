from django.db import models

# Create your models here.
class Book (models.Model):
    title = models.CharField(max_length=100),
    publication_year = models.DateTimeField()


    def __str__(self):
        return self.title

    
class Author(models.Model):
    name = models.CharField(max_length= 200)


    def __str__(self):
        return self.name