from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages
from .models import categorydb, AddRecord, Feedback
# Create your views here.


def landingpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, "index.html")


@login_required(login_url='login')
def dashboard(request):
    collect_category_list = []
    count = 0
    if request.method == 'POST':
        author = request.user.id
        category = request.POST['category']
        if category == "":
            messages.info(
                request, 'Please enter a category name.')
            return redirect('dashboard')
        else:
            get_user_id = request.user.id
            collect_category = categorydb.objects.filter(author=get_user_id)
            for i in collect_category:
                collect_category_list.append(i.category)
            print("----", collect_category_list)
            for i in collect_category_list:
                if i == category or i.upper() == category.upper() or i.lower() == category.lower() or category == "All" or category.upper() == "ALL" or category.lower() == "all":
                    count += 1
                    break
            print("count:", count)
            if count > 0:
                messages.info(
                    request, 'Category already present, Enter a new category name.')
                return redirect('dashboard')
            else:
                categorySave = categorydb(author=author, category=category)
                categorySave.save()
                return redirect('dashboard')

    else:
        get_user_id = request.user.id
        all_categories = categorydb.objects.filter(author=get_user_id)
        return render(request, "dashboard.html", {'all_categories': all_categories})


@login_required(login_url='login')
def renamecategory(request, category):
    category_name = category



'''TO GET THE FULL CODE EMAIL AT ayushk0412@gmail.com OR CALL ON 6362991410'''



def about(request):
    return render(request, 'about.html')


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username,
                                password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.success(
                    request, 'Username or Password is incorrect')

    context = {}
    return render(request, "accounts/login.html", context)


def logoutpage(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            email = request.POST['email']
            print('email:', email)
            form = CreateUserForm(request.POST)
            existing_email = str(User.objects.filter(email=email))
            if existing_email == "<QuerySet []>" or existing_email == " <QuerySet []> " or existing_email == " <QuerySet []>" or existing_email == "<QuerySet []> ":
                if form.is_valid():
                    form.save()
                    user = form.cleaned_data.get('username')
                    messages.success(
                        request, 'Account was created for ' + user)
                    return redirect('login')
            else:
                messages.info(
                    request, 'Email already registered, Try Again.')
                return redirect('register')
    context = {'form': form}
    return render(request, "accounts/register.html", context)


@login_required(login_url='login')
def settings(request):
    return render(request, 'settings.html')


@login_required(login_url='login')
def UpdatePassword(request):
    form = PasswordChangeForm(user=request.user)

    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(
                request, 'Password successfully updated.')
            return redirect('dashboard')
        else:
            messages.success(
                request, 'Password not updated, Check if old password is correct, also the new password should match in both the fields.')
            return render(request, 'accounts/updatepassword.html', {'form': form, })

    return render(request, 'accounts/updatepassword.html', {'form': form, })
