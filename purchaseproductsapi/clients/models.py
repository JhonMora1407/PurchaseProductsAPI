from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)


class ClientManager(BaseUserManager):

    def create_user(self, first_name, last_name, email, document, password=None):

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        client = self.model(first_name=first_name, last_name=last_name, 
                            email=email, document= document)
        client.set_password(password)
        client.save(using=self._db)

        return client

    def create_superuser(self, first_name, last_name, email, document, password):
        client = self.create_user(first_name, last_name, email, document, password)
        client.is_superuser = True
        client.save(using=self._db)

        return client


class Client(AbstractBaseUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    document = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=40, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ClientManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'document']

    def save(self, *args, **kwargs):
        super(Client, self).save(*args, **kwargs)
