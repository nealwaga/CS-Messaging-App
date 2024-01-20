from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from messaging.forms.authentication import AgentRegistrationForm, AgentLoginForm

# Create here
class AgentRegistration(View):
    template_name = 'authentication/signup.html'

    def get(self, request):
        form = AgentRegistrationForm()

        context = {
            'form': form,
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = AgentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            user.save()
            login(request, user)
            print('Redirecting to login page...')
            return redirect('login')
        else:
            print('Form is not valid:', form.errors)

        context = {
            'form': form,
        }
        return render(request, self.template_name, context)
    

class AgentLogin(View):
    template_name = 'authentication/login.html'

    def get(self, request):
        form = AgentLoginForm()

        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = AgentLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('chats')
            else:
                messages.error(request, 'Invalid email or password.')
                form = AgentLoginForm()
        else:
            print('Form is not valid:', form.errors)
            messages.error(request, f"Invalid form submission: {form.errors}")
        
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    

@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, f"Successfully logged out")
    return redirect('login')