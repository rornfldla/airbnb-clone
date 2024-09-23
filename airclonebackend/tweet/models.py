from django.db import models
from common.models import CommonModel

class Tweet(CommonModel) :
    content = models.CharField(max_length=150)
    user = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.CASCADE, related_name="tweet")
    likes = models.PositiveIntegerField(default=0)
    
    def __str__(self) -> str:
        return self.content