from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, SignInForm, LibrarianForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Customer, Librarian
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            phonenumber = form.cleaned_data.get('phone_number')
            national_code = form.cleaned_data.get('national_code')
            user = authenticate(username=username, password=raw_password)
            if not user:
                user = User(username=username, email=email)
                user.set_password(raw_password)
                user.save()
                customer = Customer(user = user, phone_number = phonenumber, national_code = national_code)
                customer.save()
                login(request, user)
                return redirect('library:book_list')
    else:
        form = SignUpForm()
    return render(request, 'registration/accounts/signup.html', {'form': form , 'access':True})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('library:book_list')
    else:
        form = SignInForm()
    return render(request, 'registration/accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('account:login')


@login_required
def signup_librarian(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = LibrarianForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                email = form.cleaned_data.get('email')
                phonenumber = form.cleaned_data.get('phone_number')
                national_code = form.cleaned_data.get('national_code')
                user = authenticate(username=username, password=raw_password)
                if not user:
                    user = User(username=username, email=email)
                    user.set_password(raw_password)
                    user.is_admin = True
                    user.is_staff = True
                    user.is_superuser = True
                    user.save()
                    librarian = Librarian(user = user, phone_number = phonenumber, national_code = national_code)
                    librarian.save()
                    login(request, user)
                    return redirect('library:book_list')
        else:
            form = LibrarianForm()
        return render(request, 'registration/accounts/signup.html', {'form': form, 'access':True})
    else:
        return render(request, 'registration/accounts/signup.html', {'access':False})