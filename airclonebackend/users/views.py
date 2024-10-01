from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from .models import User
from .serializers import UserSerializer
from Tweets.models import Tweet
from Tweets.serializers import TweetSerializer

class Users(APIView) :

  def get(self, request) :
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


class UsersDetail(APIView) :

  def get_object(self, pk) :
    try :
      return User.objects.get(pk=pk)
    except User.DoesNotExist :
      raise NotFound

  def get(self, request, pk) :
    user = self.get_object(pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


class UsersTweets(APIView) :

  def get_object(self, pk) :
    try :
      return User.objects.get(pk=pk)
    except User.DoesNotExist :
      raise NotFound

  def get(self, request, pk) :
    user = self.get_object(pk)
    tweets = Tweet.objects.filter(user=user)
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)