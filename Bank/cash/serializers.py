from rest_framework.serializers import *
from .models import *

class lucky_serializers(ModelSerializer):
    class Meta:
        model = lucky
        fields = '__all__'

class boss_serializers(ModelSerializer):
    class Meta:
        model = boss
        fields = '__all__'
