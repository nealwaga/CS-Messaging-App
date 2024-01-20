from django.urls import path

from messaging.views import authentication, chats

# Create here
urlpatterns = [
    # Authentication URLs
    path("", authentication.AgentRegistration.as_view(), name='register'),
    path("login/", authentication.AgentLogin.as_view(), name='login'),
    path("logout/", authentication.logout, name='logout'),

    path("chats/", chats.ChatsView.as_view(), name='chats'),
]
