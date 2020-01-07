#### Project Urls...........

from django.contrib import admin
from django.urls import path, include
from .routers import  router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee_register.urls', namespace='employee')),
    path('api/', include(router.urls)),

]
