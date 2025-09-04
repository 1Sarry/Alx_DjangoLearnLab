from rest_framework import serializers
from .models import Book, Author
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate_pub_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Publication can't be in the future! haha")
        return value
        

class AuthorSerializer(serializers.ModelSerializer):

    books = BookSerializer(many=True, read_only=True)
    #Nested serializer
    class Meta:
        model = Author
        fields =['name', 'books']
    
    
