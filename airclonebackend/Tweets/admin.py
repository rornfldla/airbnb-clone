from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Tweet, Like
    
class wfilter(admin.SimpleListFilter) :
    title = "word filter"
    
    parameter_name = "word_filter"
    
    def lookups(self, request, model_admin) :
        return [
            ("elon_musk", "Elon Musk"),
            ("not_elon_musk", "Not Elon Musk"),
        ]
    
    def queryset(self, request, queryset) :
        if self.value() == "elon_musk" :
            return queryset.filter(payload__icontains="Elon Musk")
        elif self.value() == "not_elon_musk":
            return queryset.exclude(payload__icontains="Elon Musk")

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin) :
    list_display = (
        "payload",
        "created_at",
        "updated_at",
    )
    
    list_filter = (
       "created_at",
        wfilter,
    )

    search_fields = (
        "user__username",
        "payload",
    )
    
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin) :
    list_display = (
        "tweet",
        "created_at",
        "updated_at",
    )
    
    list_filter = (
        "created_at",
    )

    search_fields = (
        "user__username",
    )