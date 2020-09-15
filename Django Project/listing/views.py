from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CarlistingSerializer

# Create your views here.
from .models import Carlisting
from django.http import HttpResponse


def listing(request):
    cars = Carlisting.objects.all()
    context = {'mycars': cars}
    return render(request, 'listing/listing.html',context)

class CarViewSet(viewsets.ModelViewSet):
    queryset = Carlisting.objects.all().order_by('title')
    serializer_class = CarlistingSerializer
