from django.db import models

# Create your models here.

class Idea(models.Model):
    
    class Visibility(models.TextChoices):
        
        public = "Public"
        protected = "Protected"
        private = "Private"
        
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=144)
    visibility = models.CharField(choices=Visibility.choices, default=Visibility.public)
    