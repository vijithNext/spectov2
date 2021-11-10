from django.contrib import admin
from api_admin.models import *

# Register your models here.

admin.site.register(Client)
admin.site.register(Project)

class PostImageAdmin(admin.StackedInline):
    model = RoofImage
 
@admin.register(Roof)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = Roof
 
@admin.register(RoofImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

# -------------------------------------------

class PostImageAdmin(admin.StackedInline):
    model = RoomImage
 
@admin.register(Room)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = Room
 
@admin.register(RoomImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

# -------------------------------------------

class PostImageAdmin(admin.StackedInline):
    model = SiteImages
 
@admin.register(SitePhotos)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = SitePhotos
 
@admin.register(SiteImages)
class PostImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Equipments_details)

# -------------------------------------------

class PostImageAdmin(admin.StackedInline):
    model = ElectricalImages
 
@admin.register(Electrical_details)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = Electrical_details
 
@admin.register(ElectricalImages)
class PostImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Backup_details)
admin.site.register(Miscellaneous_Details)


