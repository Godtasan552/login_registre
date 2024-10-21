from django.contrib import admin
from .models import MyModel, Author, Blog, UserProfile

admin.site.register(MyModel)
admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(UserProfile)
