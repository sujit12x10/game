from django.shortcuts import render, get_object_or_404
from account.forms import UserRegistrationForm, UserEditForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.

def custom_logout(request):
    logout(request.user)

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/registration_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        
        if user_form.is_valid():
            user_form.save()
            return render(request, 'account/edit_done.html', {'user': request.user})

    else:
        user_form = UserEditForm(instance=request.user)

    return render(request, 'account/edit.html', {'user_form': user_form})
