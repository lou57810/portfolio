from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
# from django.contrib.auth.models import UserManager
from django.db import models

# From Code Aura https://www.youtube.com/watch?v=IdpwReLHrbk


class CustomUserManager(BaseUserManager):
    # From class UserManager(BaseUserManager)
    # Let's override _create_user fct:
    def _create_user(self, email, password, first_name, **extra_fields):
        if not email:
            raise ValueError("Email must be provided!")
        if not password:
            raise ValueError("Password is not provided!")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, first_name, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, first_name, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    # AbstractBaserUser has password, last_login, is_active by default
    email = models.EmailField(db_index=True, unique=True, max_length=64)
    first_name = models.CharField(max_length=64)

    is_staff = models.BooleanField(default=True)    # Needed to log to django-admin
    is_active = models.BooleanField(default=True)   # Needed to log to django-admin
    is_superuser = models.BooleanField(default=True)  # Inherited from PermissionsMixin

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    profile_photo = models.ImageField(verbose_name='photo de profil', default='default_profile.jpg')
    # role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


"""
class User(AbstractUser):

    CREATOR = 'CREATOR'
    SUBSCRIBER = 'CONTRIBUTOR'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné'),
    )

    profile_photo = models.ImageField(verbose_name='photo de profil')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='role')
    
    follows = models.ManyToManyField(
        'self',
        limit_choices_to={'role': CREATOR},
        symmetrical=False,
        verbose_name='suit'
    )

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == self.CREATOR:
            group = Group.objects.get(name='creators')
            group.user_set.add(self)
        elif self.role == self.SUBSCRIBER:
            group = Group.objects.get(name='subscribers')
            group.user_set.add(self)
    """