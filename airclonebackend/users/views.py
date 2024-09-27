from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.exceptions import NotFound
from .models import User
from Tweets.models import Tweet
from Tweets.serializers import TweetSerializer

class Tweets_by_user(APIView):

  def get_object(self, pk):
    try:
      return User.objects.get(pk=pk)
    except User.DoesNotExist:
      raise NotFound

  def get(self, request, pk):
    user = self.get_object(pk)
    tweets = Tweet.objects.filter(user=user)
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)