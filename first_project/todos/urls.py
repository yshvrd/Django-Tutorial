from django.urls import path 
from . import views
urlpatterns = [
    path('hello', views.hello_world_view, name="hello world"),
    path('python', views.hello_python_view, name="hello python")
]