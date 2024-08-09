from django.contrib import admin
from .models import Articles,Comment



# class CommentInline(admin.StackedInline): # new
class CommentInline(admin.TabularInline): 
    model = Comment

class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [
    CommentInline,
]


# Register your models here.
admin.site.register(Articles,ArticleAdmin)
admin.site.register(Comment)