from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Article

# Register your models here.

@admin.register(Article)
class ArticleAdmin(TranslatableAdmin):
    list_display = ('safe_title', 'created_at')

    def safe_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True)

    safe_title.short_description = 'Title'