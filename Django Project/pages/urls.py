from django.urls import path

#from .views import contactPageView

from. import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about')
]