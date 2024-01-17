from django.urls import path

from messaging.views import authentication

urlpatterns = [
    # Authentication URLs
    path("", authentication.Index.as_view(), name='index'),
]
