from django.shortcuts import render, redirect
from accounts.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have been registered successfully!")
            return redirect('home')
    else:
        form = UserCreationForm()
    data = {
        "title": "Register User",
        "form": form,
    }
    
    return render(request, "accounts/register.html", data)
    
