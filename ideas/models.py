from django.db import models

class Idea(models.Model):
    
    class Visibility(models.TextChoices):
        public = "Public"
        protected = "Protected"
        private = "Private"
        
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=144)
    visibility = models.CharField(max_length= 9, choices=Visibility.choices, default=Visibility.public)
    
    # An Idea is created by a user
    user = models.ForeignKey(to='users.User', related_name='idea', on_delete=models.CASCADE)
    
    @staticmethod
    def get_self_ideas(my_user_id):
        return Idea.objects.filter(user_id=my_user_id).order_by('-created_at')