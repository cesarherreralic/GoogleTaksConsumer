# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    completed = models.NullBooleanField(blank=True)

class UserManager(BaseUserManager):

    def create_user(
            self,
            username,
            email,
            firstname=None,
            lastname=None,
            password=None,
            is_active=True,
    ):
        """ Creates and saves a User with the given email, RIF , password. """

        if not username:
            raise ValueError(
                u'Users must have a username'
            )

        if not email:
            raise ValueError(
                u'Users must have email'
            )


        user = self.model(
            username = username,
            lastname=lastname,
            email=UserManager.normalize_email(
                email
            ),
            # is_superuser=is_superuser,
            firstname=firstname,
            is_active=True,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
            self,
            username,
            email,
            password,
            firstname=None,
            lastname=None,
            is_active=True,
    ):
        """ Creates and saves a superuser with the given email and password. """

        user = self.create_user(
            username=username,
            firstname=firstname,
            lastname=lastname,
            email=email,
            is_active=True
            # is_superuser=True
            # password=password
        )

        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, unique=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    is_active = models.BooleanField(_('active'), default=True)
    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.firstname, self.lastname)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.firstname

    def get_email(self):
        "Returns the short name for the user."
        return self.email
