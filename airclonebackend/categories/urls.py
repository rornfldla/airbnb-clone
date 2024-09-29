from django.urls import path
from . import views

urlpatterns = [
    path("", views.CategoryViewSet.as_view(
            {
                "get" : "list",
                "post" : "create"
            }
        ),
    ), #class를 가져오기 위해 as_view() 사용
    path("<int:pk>", views.CategoryViewSet.as_view(
            {
            "get" : "retrieve",
            "put" : "partial_update",
            "delete" : "destroy",
            }
        ),
    ),
]
 