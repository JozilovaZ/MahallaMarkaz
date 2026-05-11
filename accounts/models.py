from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, fullname, password=None, **extra):
        if not email:
            raise ValueError('Email kiritilishi shart')
        user = self.model(email=self.normalize_email(email), fullname=fullname, **extra)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fullname, password=None, **extra):
        extra.setdefault('is_staff', True)
        extra.setdefault('is_superuser', True)
        extra.setdefault('role', 'admin')
        return self.create_user(email, fullname, password, **extra)


class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('resident', 'Mahalla fuqarosi'),
        ('admin', 'Administrator'),
        ('responsible', "Mas'ul shaxs"),
    ]

    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='resident')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']

    def __str__(self):
        return f'{self.fullname} ({self.email})'
