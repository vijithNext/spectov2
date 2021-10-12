from django.contrib import admin
from api_admin.models import Client, Project, Roof, SitePhotos, Add_Electrical_connection_details, Add_Backup_Generator_details, Room, Add_Equipments_and_working_details, Miscellaneous_Details

# Register your models here.

admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Roof)
admin.site.register(Room)
admin.site.register(SitePhotos)
admin.site.register(Add_Equipments_and_working_details)
admin.site.register(Add_Electrical_connection_details)
admin.site.register(Add_Backup_Generator_details)
admin.site.register(Miscellaneous_Details)


