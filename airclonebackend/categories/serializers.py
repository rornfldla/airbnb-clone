from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer) :
    
    class Meta :
        model = Category
        fields = "__all__" # fields -> 무엇을 포함할지 // exclude -> 무엇을 제외할지(나머지는 다 포함) // __all__ 모두 선택