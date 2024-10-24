from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # ฟิลด์เพิ่มเติมที่คุณต้องการสามารถเพิ่มที่นี่ได้
    
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # เปลี่ยนชื่อให้แตกต่าง
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # เปลี่ยนชื่อให้แตกต่าง
        blank=True,
        help_text='Specific permissions for this user.'
    )
