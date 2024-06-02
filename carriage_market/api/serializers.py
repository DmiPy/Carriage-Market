from rest_framework import serializers
from .models import Wagon

class WagonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wagon
        fields = ('id','name','description','price','category','image','created_at','updated_at')
