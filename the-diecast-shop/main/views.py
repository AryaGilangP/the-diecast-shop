import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers 
from main.forms import CarItemsForm
from main.models import CarItems

@login_required(login_url='/login')
def show_main(request):
    car_items = CarItems.objects.filter(user=request.user)  

    context = {
        'app': 'FUFUFAFA CARS',
        'name': request.user.username,
        'car_items': car_items,
        'class': 'PBP F',
        'NPM': '2306221970',
        'last_login': request.COOKIES.get('last_login'),
    }

    return render(request, "main.html", context)


def create_car_item(request):
    form = CarItemsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        print("Form valid, menyimpan car_item")  # Debugging
        car_item = form.save(commit=False)
        car_item.user = request.user
        car_item.save()
        return redirect('main:show_main')


    context = {'form': form}
    return render(request, "create_car_item.html", context)

def edit_car(request, id):
    car = CarItems.objects.get(pk=id)
    form = CarItemsForm(request.POST or None, instance=car)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_car.html", context)


def delete_car(request, id):
    # Get car berdasarkan id
    car = CarItems.objects.get(pk = id)
    # Hapus mood
    car.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

def show_xml(request):
    data = CarItems.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = CarItems.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = CarItems.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = CarItems.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response