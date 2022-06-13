from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse_lazy


class BaseModel:
    """
    A mixin class to provide get_absolute_url method to model classes following common naming conventions.
    Requires ListView names to be list_model_name.
    """

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        suffix = self._meta.verbose_name.lower()
        return reverse_lazy('auth2:' + suffix + '_list')


# Create your models here.
#
# class User(AbstractUser):
#     bio = models.CharField(max_length=1024)
#     image = models.ImageField(upload_to='images/users/')
