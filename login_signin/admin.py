from django.contrib import admin
from .models import MyModel,Author, Blog  # เปลี่ยนเป็นโมเดลของคุณ

admin.site.register(MyModel)
admin.site.register(Author)
admin.site.register(Blog)
