from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
class Author(models.Model):
    # กำหนดตัวเลือกสำหรับคำนำหน้าชื่อ
    TITLE_CHOICES = [
        ('Mr', 'Mr.'),
        ('Mrs', 'Mrs.'),
        ('Ms', 'Ms.'),
        ('Dr', 'Dr.'),
        ('Prof', 'Prof.'),
    ]
    
    # คำนำหน้าชื่อ
    title = models.CharField(max_length=10, choices=TITLE_CHOICES, default='Mr')  # ใส่ default สำหรับคำนำหน้า
    first_name = models.CharField(max_length=100, default='Unknown')  # ใส่ default สำหรับชื่อ
    last_name = models.CharField(max_length=100, default='Unknown')  # ใส่ default สำหรับนามสกุล
    birth_date = models.DateField(null=True, blank=True)  # สามารถใส่เป็น null ได้สำหรับวันเกิด

    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name}"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)