from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Cars', views.CarViewSet)


urlpatterns = [
    path('', views.listing, name='listing'),
    path('router/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]