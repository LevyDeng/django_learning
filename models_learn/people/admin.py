from django.contrib import admin

# Register your models here.
from .models import Article,Person

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time')

admin.site.register(Article,ArticleAdmin)
admin.site.register(Person)