from django.db import models
from django.contrib.auth.models import AbstractUser


class BeelineUser(AbstractUser):
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.phone_number
