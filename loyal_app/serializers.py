from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    type = TypeSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = '__all__'
