from django.urls import path

from .views import employee_list,employee_form,employee_delete,employee_update

urlpatterns = [
    path('', employee_list,name='employee_list'),
    path('employee_form/', employee_form,name='employee_form'),
    path('delete/<int:user_id>/', employee_delete,name='employee_delete'),
    path('<int:user_id>/', employee_update,name='employee_update')
]
