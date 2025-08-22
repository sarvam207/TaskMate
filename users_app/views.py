from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('register')  # Redirect to a success page or login page after registration
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})  