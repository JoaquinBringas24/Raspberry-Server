from django.urls import path
from users.views import members

urlpatterns = [
    path('members/', members, name='users-members')
]
