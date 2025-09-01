from django.apps import AppConfig
from django.core.management import call_command
import os

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        if os.getenv("RENDER") == "1":  # Solo en Render
            try:
                from .models import Post
                if Post.objects.count() == 0:
                    call_command("loaddata", "blog_data.json")
            except Exception:
                pass


