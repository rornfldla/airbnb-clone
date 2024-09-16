from django.db import models

# Create your models here.

class House(models.Model) :

    """House Model"""

    name = models.CharField(max_length=140) # 사용자가 텍스트를 쓰고 싶을 때 약간 짧거나 문자 길이에 제한을 할 떄 많이 사용함
    price = models.PositiveBigIntegerField()
    description = models.TextField() # CharField보다 더 긴 텍스트를 사용자가 입력하게 하고 싶을 때 사용(길이 제한 x)
    address = models.CharField(max_length=140)