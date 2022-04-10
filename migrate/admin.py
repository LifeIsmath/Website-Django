from django.contrib import admin

from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ...
    

admin.site.register(Category, CategoryAdmin)
