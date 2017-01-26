# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from .models import User


class UserAdmin(AuthUserAdmin):
    list_display = ('username', 'type', 'get_full_name', 'is_superuser')
    search_fields = ['name']

    fieldsets = (
        (None, {'fields': ('username', 'password', 'type', 'first_name', 'last_name', 'email',
                           'is_staff', 'is_superuser')
        }),
    )


admin.site.register(User, UserAdmin)
