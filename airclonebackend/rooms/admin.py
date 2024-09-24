from django.contrib import admin
from .models import Room, Amenity

@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, rooms) : # 3개의 매개변수 필요 -> 모델 클래스 / request 객체 - 사용자의 요청을 담고 있음 / queryset - 관리자가 현재 선택한 객체들의 목록 
    for room in rooms.all() :
        room.price = 0
        room.save()

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin) :
    
    actions = (reset_prices,)
    
    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created_at",
    )
    
    list_filter = (
        "country",
        "city",
        "price",
        "rooms",
        "toilets",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )
    
    search_fields = (
        "owner__username",
        "^price", # 그냥 -> __contain // ^ -> startswith // = -> 동잃한 값
    )
    
    def total_amenities(self, room) :
        return room.amenities.count()
    
    def rating(self, room) :
        count = room.reviews.count()
        
        if count == 0 :
            return "No Reviews"
        else :
            total_rating = 0
            for review in room.reviews.all().values("rating") :
                total_rating += review["rating"]
            return round(total_rating / count, 2)
            

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin) :
    
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    
    readonly_fields = (
        "created_at",
        "updated_at",
    )
