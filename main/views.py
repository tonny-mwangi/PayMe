from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.utils.timezone import now

def landing_page(request):
    return render(request, 'main/landing_page.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')  # Name of the login URL
        else:
            # Print form errors to console for debugging
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def register_view(request):
    context = {'form': form, 'timestamp': now().timestamp()}
    return render(request, 'registration/register.html', context)
def register_view(request):
    context = {'form': form, 'timestamp': now().timestamp()}
    return render(request, 'registration/login.html', context)


    
    