from django.shortcuts import render
from django.views import View

# Create here
class Index(View):
    template_name = 'authentication/signup.html'

    def get(self, request):
        return render(request, self.template_name)