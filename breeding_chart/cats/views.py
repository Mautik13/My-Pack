from django.http import HttpResponse
from django.template import loader
from .models import Cat, Tomcat, Kitten, Home
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm
from .forms import CatForm


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def home(request):
    context = {
        'home': Home.objects.all()
    }
    return render(request, 'home.html', context)


def cat(request):
    context = {
        'cat': Cat.objects.all(),
    }
    return render(request, 'cat.html', context)


def cat_detail(request, id):
    cat = Cat.objects.get(id=id)
    template = loader.get_template('cat_detail.html')
    context = {
        'cat': cat,
    }
    return HttpResponse(template.render(context, request))


def tomcat(request):
    context = {
        'tomcat': Tomcat.objects.all(),
    }
    return render(request, 'tomcat.html', context)


def tomcat_detail(request, id):
    tomcat = Tomcat.objects.get(id=id)
    template = loader.get_template('tomcat_detail.html')
    context = {
        'tomcat': tomcat,
    }
    return HttpResponse(template.render(context, request))


def kitten(request):
    context = {
        'kitten': Kitten.objects.all(),
    }
    return render(request, 'kitten.html', context)


def kitten_detail(request, id):
    context = {
        'kitten': Kitten.objects.all(),
    }
    return render(request, 'kitten_detail.html', context)


#def cat_list(request):
#    cats = Cat.objects.all()
#   return render(request, 'cat_list.html', {'cats': cats})


def add_cat(request):
    if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cat_list')
    else:
        form = CatForm()
    return render(request, 'add_cat.html', {'form': form})


#def remove_cat(request, cat_id):
 #   cat = get_object_or_404(Cat, id=cat_id)
  #  if request.method == 'POST':
   #     cat.delete()
    #    return redirect('cat_table')
    #return render(request, 'remove_cat.html', {'cat': cat})


def remove_cat(request, cat_id):
    cat = get_object_or_404(Cat, id=cat_id)
    cat.delete()
    return redirect('cat_table')


def edit_cat(request, cat_id):
    cat = get_object_or_404(Cat, id=cat_id)
    if request.method == 'POST':
        form = CatForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            return redirect('cat_list')
    else:
        form = CatForm(instance=cat)
    return render(request, 'edit_cat.html', {'form': form, 'cat': cat})


def users_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def users_logout(request):
    logout(request)
    return redirect('main')


def users_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'cats/profile.html')


def privacy_policy(request):
    return render(request, 'cats/privacy_policy.html')


def cat_table(request):
    cats = Cat.objects.all()
    return render(request, 'cat_list.html', {'cats': cats})
