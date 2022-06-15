from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# Function to create a user creation form
def register(request):
    # check if the request method is POST
    if request.method == 'POST':
        # create a user registration form by passing the POST request
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # To display messages in django
            messages.success(request, f'Account created for {username}!')
            # redirect to the profile page
            return redirect('profile')
    else:
        # create a user registration form
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# Function to create a profile page for the user
# login tag added to perform the login check for the user
@login_required()
def profile(request):
    # check if the request method is POST
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
