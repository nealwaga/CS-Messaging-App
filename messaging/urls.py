from django.urls import path

from messaging.views import authentication

# Create here
urlpatterns = [
    # Authentication URLs
    path("", authentication.AgentRegistration.as_view(), name='register'),
    path("login/", authentication.AgentLogin.as_view(), name='login'),
]
