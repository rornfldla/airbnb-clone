from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Perk
from .serializers import PerkSerializer
class Perks(APIView) :
    
    def get(self, request) :
        all_perks = Perk.objects.all()
        serializer = PerkSerializer(all_perks, many = True)
        return Response(serializer.data)
    
    def post(self, request) :
        serializer = PerkSerializer(data = request.data)                       
    
class PerkDetail(APIView) :
    
    def get(self, request, pk) :
        pass
    
    def put(self, request, pk) :
        pass
    
    def delete(self, request, pk) :
        pass