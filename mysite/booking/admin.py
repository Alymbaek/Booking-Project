from django.contrib import admin
from .models import *

class RoomPhotosInlines(admin.TabularInline):
    model = RoomPhotos
    extra = 1
class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomPhotosInlines]

admin.site.register(Room,RoomAdmin)
admin.site.register(UserProfile)
admin.site.register(Region)
admin.site.register(Hotel)
admin.site.register(Review)
admin.site.register(Booking)