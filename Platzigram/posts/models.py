"""Posts Models."""
#django
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
#utils


class Post(models.Model):
    """Post Model."""
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Return title and username.

        Returns:
            str: title and username
        """
        return f'{self.title} by @{self.user.username}'