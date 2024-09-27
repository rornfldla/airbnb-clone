from django.db import models
from common.models import CommonModel

class Tweet(CommonModel) :
    payload = models.CharField(max_length=180, default="")
    user = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.CASCADE, related_name="tweets")
    
    def __str__(self) -> str:
        return self.payload
    
    def like_count(self):
        return self.likes.count()
    
class Like(CommonModel) :
    name = models.CharField(max_length=150, default="")
    user = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.CASCADE, related_name="like")
    tweet = models.ForeignKey("Tweets.Tweet", on_delete=models.CASCADE, related_name="like")
    
    def __str__(self) -> str:
        return self.name
    
    