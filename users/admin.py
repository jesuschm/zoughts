from django.contrib import admin
from django.apps import apps
from .models import User

# Permite gestionar los siguientes modelos desde el panel de admin de Django.
admin.site.register(User) 

app = apps.get_app_config('graphql_auth')

for model_name, model in app.models.items():
    admin.site.register(model) 