from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy


class UserManager(BaseUserManager):
    def _create_user(self, email, account_id, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, account_id=account_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, account_id, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            email=email,
            account_id=account_id,
            password=password,
            **extra_fields,
        )

    def create_superuser(self, email, account_id, password, **extra_fields):
        extra_fields['is_active'] = True
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self._create_user(
            email=email,
            account_id=account_id,
            password=password,
            **extra_fields,
        )


class User(AbstractBaseUser, PermissionsMixin):
    account_id = models.CharField(
        verbose_name=gettext_lazy("account_id"), unique=True, max_length=100
        )

    username = models.CharField(
        verbose_name=gettext_lazy("username"), max_length=30, unique=True, null=True, blank=False
    )

    password = models.CharField(
        verbose_name=gettext_lazy("password"), max_length=50, null=True, blank=False
    )

    email = models.EmailField(
        verbose_name=gettext_lazy("email"), unique=True
    )
    
    first_name = models.CharField(
        verbose_name=gettext_lazy("first_name"), max_length=30
    )

    last_name = models.CharField(
        verbose_name=("last_name"), max_length=30
    )

    is_superuser = models.BooleanField(
        verbose_name=gettext_lazy("is_superuser"), default=False
    )

    is_staff = models.BooleanField(
        verbose_name=gettext_lazy('staff status'), default=False,
    )

    is_active = models.BooleanField(
        verbose_name=gettext_lazy('active'), default=True,
    )

    created_at = models.DateTimeField(
        verbose_name=gettext_lazy("created_at"), auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name=gettext_lazy("updated_at"), auto_now=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.account_id

