from django.contrib import admin

# Register your models here.
from . models import Tag,Author,Post


class postAdmin(admin.ModelAdmin):
    list_display=("title","author","excerpt")
    list_filter=("tag","date","author")
    prepopulated_fields={"slug":("title",)}

admin.site.register(Post,postAdmin)
admin.site.register(Tag)
admin.site.register(Author)
