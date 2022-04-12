from django.urls import path

from . import views

app_name = 'votacion'

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:region_id>/',views.candidatos,name='candidatos'),
    path('<int:region_id>/detalles/',views.detalles,name='detalles'),

]