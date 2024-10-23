from django.contrib import admin
from .models import Item, item_gallery # Import the model

@admin.register(item_gallery)
class item_galleryAdmin(admin.ModelAdmin):
    list_display = ('Location',)  # Fields to display in the list view


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'discounted_price','image')  # Fields to display in the list view
    search_fields = ('name',)  # Search functionality
    list_filter = ('price', 'discounted_price')  # Filtering options
