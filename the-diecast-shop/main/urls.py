from django.urls import path
from main.views import show_main
from main.views import show_main, create_car_item
from main.views import show_main, create_car_item, show_xml
from main.views import show_main, create_car_item, show_xml, show_json
from main.views import show_main, create_car_item, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_car
from main.views import delete_car
from main.views import add_car_item_ajax
from . import views

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('create-car-item', views.create_car_item, name='create_car_item'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<str:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', views.show_json_by_id, name='show_json_by_id'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('delete/<uuid:id>/', views.delete_car, name='delete_car'),  # Changed to <uuid:id>
    path('edit_car/<uuid:id>/', views.edit_car, name='edit_car'),    # Changed to <uuid:id>
    path('create-car-item-ajax', views.add_car_item_ajax, name='add_car_item_ajax'),
]