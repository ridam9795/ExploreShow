from rest_framework import serializers
from .models import Movie, Event,Sport,Activity
from django.contrib.auth.models import User
from django.db import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ( 'username', 'password', 'first_name')
    def create(self,validated_data):
        user=User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.first_name=validated_data['first_name']
        user.save()
        return user

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = "__all__"

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"
