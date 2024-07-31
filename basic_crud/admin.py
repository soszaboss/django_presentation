from django.contrib import admin
from .models import Books, Authors

class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'birth_date', 'nationality')
    list_per_page = 10
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'publication_date', 'author_fullname')
    list_per_page = 10

    def author(self, obj):
        return obj.author.fullname
    

# Register your models here.
admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Books, BooksAdmin)