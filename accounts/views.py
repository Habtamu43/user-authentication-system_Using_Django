from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserLoginForm

# User registration view
def register(request):
    # Clear previous messages to prevent stacking errors
    messages.get_messages(request).used = True

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log the user in
            messages.success(request, 'Registration successful!')  # Success message
            return redirect('profile')  # Redirect to the profile page after successful registration
        else:
            # Display form errors if the form is not valid
            if form.errors.get('email'):
                messages.error(request, "Email is already in use.")  # Specific error for email
            # Only display the first error for each field
            for field in form:
                if field.errors:
                    messages.error(request, field.errors[0])  # Display only the first error

    else:
        form = CustomUserCreationForm()  # Display an empty form for GET requests
    
    return render(request, 'accounts/register.html', {'form': form})


# Login view
def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)  # Authenticate using email and password
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next')  # Get 'next' parameter from the URL
                if next_url:
                    return redirect(next_url)  # Redirect to 'next' URL if available
                return redirect('profile')  # Default redirect to the profile page after successful login
            else:
                messages.error(request, 'Invalid email or password')  # Error message for invalid credentials
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)  # Display form errors
    else:
        form = CustomUserLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')  # Logout success message
    return redirect('login')  # Redirect to the login page after logout


# Profile view
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


# User list view
@login_required
def user_list(request):
    User = get_user_model()
    users = User.objects.all()  # Retrieve all registered users
    return render(request, 'accounts/user_list.html', {'users': users})

