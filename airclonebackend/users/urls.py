from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/tweets", views.Tweets_by_user.as_view()),
]
