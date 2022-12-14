from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def for_admin(function=None, redirect_field_name=REDIRECT_FIELD_NAME, url='customerlist'):
    '''A decorator to check whether the logged-in user is admin and redirect to the login page if the user is not authenticated.'''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.base_role == "ADMIN",
        url=url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def for_super_admin(function=None, redirect_field_name=REDIRECT_FIELD_NAME, url='customerlist'):
    '''A decorator to check whether the logged-in user is a super admin and redirect to the login page if the user is not authenticated.'''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.base_role == "SUPER_ADMIN",
        url=url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator