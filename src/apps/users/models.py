from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_supplier = models.BooleanField(default=False, verbose_name="Поставщик")
    is_client = models.BooleanField(default=False, verbose_name="Клиент")

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Added unique related_name to avoid clashes
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  # Added unique related_name to avoid clashes
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email