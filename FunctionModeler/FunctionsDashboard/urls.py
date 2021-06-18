from django.urls import path

from . import views as app_views

app_name = 'FunctionsDashboard'

urlpatterns = [
    path('', app_views.index, name='index'),
]
