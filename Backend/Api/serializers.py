from datetime import timezone
from django.db import models
from django.utils.translation import check_for_language
from rest_framework import fields, serializers
from .models import Contact
from .models import Customer

class Contactserializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=['id','name','email','phone','desc']


class Customerserializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['id','username','email','password','Age','phone','weight','height','allergies','Med1','Med2','Med3','Med4','Med5','Med6','Med8','Med7','time_1','time_2','time_3','time_4','time_5','time_6','time_7','time_8','pills_1','pills_2','pills_3','pills_4','pills_5','pills_6','pills_7','pills_8']

