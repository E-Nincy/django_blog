# blog/apps.py
from django.apps import AppConfig
import os
import json
from django.core.management import call_command
from django.db.utils import OperationalError

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        if os.getenv("RENDER") == "1":
            from django.db import connections
            try:
                c = connections['default'].cursor()
                return
            except OperationalError:
                json_file = os.path.join(os.path.dirname(__file__), "blog_data.json")
                if os.path.exists(json_file):
                    call_command("loaddata", json_file)



