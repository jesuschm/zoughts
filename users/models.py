from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    
    email = models.EmailField(blank=False, unique=True, max_length=255, verbose_name = "email")
    
    # An User can follow N users (and to be followed by N users)
    follows = models.ManyToManyField(to='users.User', related_name='follow', through='ConnectionRequest', symmetrical = False)
    
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    
class ConnectionRequest(models.Model):
    from_user = models.ForeignKey(User, related_name = 'from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name = 'to_user', on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    
    class Meta:
        unique_together = (('from_user', 'to_user'),)