from rest_framework import serializers

from .models import Carlisting

class CarlistingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carlisting
        fields = ('id','title', 'model','engine_cc','color','car_type','passenger_capacity','gear','manufacture_year','price','Car_image')