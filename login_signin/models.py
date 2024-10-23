from django.db import models
from django.contrib.auth.models import User

class MyModel(models.Model):
    name = models.CharField(max_length=100)

class Author(models.Model):
    TITLE_CHOICES = [
        ('Mr', 'Mr.'),
        ('Mrs', 'Mrs.'),
        ('Ms', 'Ms.'),
        ('Dr', 'Dr.'),
        ('Prof', 'Prof.'),
    ]
    title = models.CharField(max_length=10, choices=TITLE_CHOICES, default='Mr')
    first_name = models.CharField(max_length=100, default='Unknown')
    last_name = models.CharField(max_length=100, default='Unknown')
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name}"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.username