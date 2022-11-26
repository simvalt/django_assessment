from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


# Create user model from abstract base user model and call it administrator


class Administrator(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "username"]
    objects = UserManager()

    def __str__(self):
        return self.email

    def roll(self):

        if self.is_staff and self.is_superuser:
            return "administrator"
        elif self.is_staff:
            return "super_administrator"
        else:
            return "normal_user"
