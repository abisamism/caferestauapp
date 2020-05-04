from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length = 200)
    phone = models.IntegerField()
    email = models.EmailField()
    
    class Meta:
        verbose_name = ("Brand")
        verbose_name_plural = ("Brands")

    def __str__(self):
        return self.name

class AboutUs(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    # image = models.ImageField(upload_to='about_us/')

    class Meta:
        verbose_name = 'about us '
        verbose_name_plural = 'about us '

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=30)


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Meals(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    category = models.ForeignKey('Category' , on_delete=models.SET_NULL , null=True)
    people = models.IntegerField()
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    preperation_time =models.IntegerField()
    image = models.ImageField(upload_to='meals/')
   
    class Meta:
        verbose_name = 'meal'
        verbose_name_plural = 'meals'


    def __str__(self):
        return self.name

class Chef(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    bio = models.TextField()
    image = models.ImageField(upload_to='chef/')    

    class Meta:
        verbose_name = 'chef'
        verbose_name_plural = 'chefs'

    def __str__(self):
        return self.name