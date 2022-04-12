
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('votacion/', include('votacion.urls')),
    path('admin/', admin.site.urls),
]
