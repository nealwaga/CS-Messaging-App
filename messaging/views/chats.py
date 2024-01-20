from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create here
class ChatsView(LoginRequiredMixin, View):
    template_name = 'messaging/chats.html'

    def get(self, request):

        return render(request, self.template_name)