from django.db import models

# Create your models here.

class House(models.Model) :

    """House Model"""

    name = models.CharField(max_length=140) # 사용자가 텍스트를 쓰고 싶을 때 약간 짧거나 문자 길이에 제한을 할 떄 많이 사용함
    price_per_night = models.PositiveBigIntegerField(verbose_name= "Price", help_text= "Positive number only") # 양수 input 필드
    description = models.TextField() # CharField보다 더 긴 텍스트를 사용자가 입력하게 하고 싶을 때 사용(길이 제한 x)
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        verbose_name= "Pets Allowed?",
        default=True, 
        help_text="Does this house allow pets?")

    def __str__(self) :
        return self.name
    

a = ["asfdasfd", "asdfsadfsafd", "asfsdafsadf"]