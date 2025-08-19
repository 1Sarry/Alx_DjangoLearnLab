from django.db import models

class Company(models.Model):
    comapany_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    founded = models.IntegerField()

    def __str__(self):
     return f"{self.comapany_name}  {self.location} ({self.founded})"

class Dempartment(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="departments")
    def __str__(self):
      return self.name
 
class Employees(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.ForeignKey(Dempartment, on_delete=models.CASCADE, related_name='employees')
    job_title = models.CharField(max_length=100)
    hire_date = models.DateField(null=False)

    def __str__(self):
     return f"{self.first_name} works in {self.department} department."
    
class Product(models.Model):
   name = models.CharField(100)
   price = models.IntegerField()

   def __str__(self):
      return self.name
   
class Product_Detail(models.Model):
   product_desc = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="prduct_detail")

   def __srt__(self):
      return self.product_desc