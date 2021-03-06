# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import Group



@python_2_unicode_compatible
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('p', 'Patient'),
        ('t', 'Therapist'),
    )

    type = models.CharField(max_length=1, default='p', choices=USER_TYPE_CHOICES)

    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()

        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

