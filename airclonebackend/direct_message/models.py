from django.db import models
from common.models import CommonModel

class ChattingRoom(CommonModel) :
    
    """ Room Model Definition"""
    
    user = models.ManyToManyField("users.User",) # --> 문제가 됨. rooms에서와 class 이름이 동일한데 같은 user를 받기 때문 *** 같은 이름이라고 문제가 생기는 것이 아님!
    
    def __str__(self) -> str:
        return "Chatting Room"
    
class Message(CommonModel) :
    
    """ Message Model Definition"""
    
    text = models.TextField()
    user = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.SET_NULL)
    room = models.ForeignKey("direct_message.ChattingRoom", on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.user} says : {self.text}"