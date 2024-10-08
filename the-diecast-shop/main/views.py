import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers 
from main.forms import CarItemsForm
from main.models import CarItems
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_main(request):

    context = {
        'app': 'FUFUFAFA CARS',
        'name': request.user.username,
        'class': 'PBP F',
        'NPM': '2306221970',
        'last_login': request.COOKIES.get('last_login'),
    }

    return render(request, "main.html", context)


def create_car_item(request):
    form = CarItemsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        car_item = form.save(commit=False)
        car_item.user = request.user
        car_item.save()
        return redirect('main:show_main')
    

    context = {'form': form}
    return render(request, "create_car_item.html", context)

def edit_car(request, id):
    car = get_object_or_404(CarItems, pk=id)
    form = CarItemsForm(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect('main:show_main')
    context = {'form': form}
    return render(request, "edit_car.html", context)
# def edit_car(request, id):
#     car = CarItems.objects.get(pk=id)
#     form = CarItemsForm(request.POST or None, instance=car)

#     if form.is_valid() and request.method == "POST":
#         form.save()
#         return HttpResponseRedirect(reverse('main:show_main'))

#     context = {'form': form}
#     return render(request, "edit_car.html", context)

def delete_car(request, id):
    car = get_object_or_404(CarItems, pk=id)
    car.delete()
    return redirect('main:show_main')
# def delete_car(request, id):
#     # Get car berdasarkan id
#     car = CarItems.objects.get(pk = id)
#     # Hapus mood
#     car.delete()
#     # Kembali ke halaman awal
#     return HttpResponseRedirect(reverse('main:show_main'))

def show_xml(request):
    data = CarItems.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = CarItems.objects.filter(user=request.user)
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
          messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
@require_POST
def add_car_item_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")  
    description = strip_tags(request.POST.get("description"))
    model_number = request.POST.get("model_number")  
    user_reviews = strip_tags(request.POST.get("user_reviews"))
    user = request.user

    new_car_item = CarItems(
        name=name, 
        price=price, 
        description=description, 
        model_number=model_number, 
        user_reviews=user_reviews,
        user=user
    )
    new_car_item.save()

    return HttpResponse(b"CREATED", status=201)

