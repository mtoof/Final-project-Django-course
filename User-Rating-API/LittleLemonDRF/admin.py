from django.contrib import admin
from .models import Rating
from .models import MenuItem

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
	list_display = ('menuitem_id', 'rating', 'user')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description', 'price')