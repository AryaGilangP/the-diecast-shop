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

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-car-item', create_car_item, name='create_car_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete/<uuid:id>', delete_car, name='delete_car'),
    path('edit_car/<uuid:id>/', edit_car, name='edit_car'),
]