from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

# Create your models here.

def user_directory_path(instance, filename):
    return 'user_{}/{}'.format(instance, filename)

class Category(models.Model):
    category_name = models.CharField(max_length=20)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.category_name

class Item(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=CASCADE, null=True)
    thumbnail = models.ImageField(upload_to=user_directory_path)
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank= True, null= True)
    price = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(1000000)])

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField()
    body = models.TextField()
    id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title