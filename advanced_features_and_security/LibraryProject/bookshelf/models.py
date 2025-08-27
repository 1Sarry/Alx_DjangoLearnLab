from django.db import models
from django.contrib.auth.models import AbstractUser # It used to create extra fields like role, date_of_birth and so on while User moder w/c is the default has fixed fields (first_n, last_n email, username and pw) 
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length= 100)
    publication_year = models.IntegerField()


    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be ser")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user    
   
# Create normal and super users

def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)
class CustomUser(AbstractUser):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()
    objects = CustomUserManager()

    def __str__(self):
        return self.user