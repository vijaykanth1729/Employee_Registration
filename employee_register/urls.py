from django.urls import path
from .views import employee_list, employee_form, employee_delete
app_name = 'employee_register'

urlpatterns = [
    path('list/', employee_list, name='list'),
    path('', employee_form, name='form'),
    path('<int:id>/', employee_form, name='update'),
    path('delete/<int:id>/', employee_delete, name='delete'),




]
