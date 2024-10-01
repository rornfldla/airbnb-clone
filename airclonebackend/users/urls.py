from django.urls import path
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("<int:pk>", views.UsersDetail.as_view()),
    path("<int:pk>/tweets", views.UsersTweets.as_view()),
]
