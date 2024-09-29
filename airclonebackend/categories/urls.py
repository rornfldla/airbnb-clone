from django.urls import path
from . import views

urlpatterns = [
    path("", views.Categories.as_view()), #class를 가져오기 위해 as_view() 사용
    path("<int:pk>", views.CategoryDetail.as_view())
]
 