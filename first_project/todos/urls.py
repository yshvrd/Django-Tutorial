from django.urls import path 
from . import views
urlpatterns = [
    path('hello', views.hello_world_view, name="hello world"),
    path('python', views.hello_python_view, name="hello python"),
    path('html', views.hello_html_view, name="hello html"),
    path('helloname/<str:name>', views.hello_path, name="hello html"),
    path('postendpoint', views.post_example, name="post_example"),
    path('submitendpoint', views.submit_example, name="post example"),
    path('submitdjango', views.submit_django_form, name="submit_django_example"),
    path('templating', views.template_view, name="template_view"),
]