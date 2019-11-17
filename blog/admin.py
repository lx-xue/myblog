from django.contrib import admin
from blog.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'publish_time')
    list_filter = ('publish_time',)


admin.site.register(Article, ArticleAdmin)
