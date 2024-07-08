from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def user_dashboard(request):
    return render(request, 'dashboard/user_dashboard.html')

def tasks(request):
    if not request.user.profile.has_paid:
        messages.error(request, "You need to purchase an account to access tasks.")
        return redirect('user_dashboard')
    return render(request, 'dashboard/tasks.html')
@login_required
def profile(request):
    if not request.user.profile.has_paid:
        messages.error(request, "You need to purchase an account to access tasks.")
        return redirect('user_dashboard')
    return render(request, 'dashboard/profile.html')

@login_required
def settings(request):
    return render(request, 'dashboard/settings.html')
def purchase_account(request):
    if request.method == 'POST':
        # Implement your payment processing logic here
        # For demonstration, we'll just set the has_paid flag to True
        request.user.profile.has_paid = True
        request.user.profile.save()
        messages.success(request, "Account purchased successfully!")
        return redirect('tasks')
    return render(request, 'dashboard/purchase_account.html')
