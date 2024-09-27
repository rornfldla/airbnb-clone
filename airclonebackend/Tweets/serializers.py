from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.Serializer) :
    class Meta:
        model = Tweet
        fields = '__all__'
