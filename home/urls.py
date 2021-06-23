
from django.urls import path
from .views import *
app_name="home"
urlpatterns = [
    path('', home, name='home'),
    path('about/', about,name='about'),
    path('bloghome/',bloghome,name='bloghome'),
    path('blogsingle/', blogsingle,name='blogsingle'),
    path('contact/', contact,name='contact'),
    path('elements/', elements,name='elements'),
    path('portfolio/', portfolio,name ='portfolio'),
    path('price/', price,name='price'),
    path('services/', services,name='services'),
]