from django.contrib import admin
from .models import Bookmark


# admin 사이트에 title과 url을 문자열로 화면에 출력을 지정
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']

admin.site.register(Bookmark, BookmarkAdmin)

# Register your models here.
