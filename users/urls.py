from django.urls import path, re_path

from users.views import *

urlpatterns = [
    path('', get_user_query),
    path('success/', success_page, name='success'),
    re_path(r'^user/userquery/\d+/resolve', resolve_query, name='resolve_query'),
    re_path(r'^user/userquery/\d+/unresolve', unresolve_query, name='unresolve_query'),
    re_path(r'^user/userquery/\d+/transfer', transfer_query, name='transfer_query')
]
