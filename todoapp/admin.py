from django.contrib import admin
from .models import Todo

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'memo', 'completed', 'created', 'updated')

admin.site.register(Todo, BookAdmin)