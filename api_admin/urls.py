from api_admin.views import *                       #import classnames from views.py
from django.urls import path


urlpatterns=[

#----------------------------------------------ADD---------------------------------------------------

    path('add-client/', AddCustomer.as_view(), name='add-customer'),
    path('add-project/', AddProject.as_view(), name='add-project'),
    path('add-roof/', AddRoof.as_view(), name='add-roof'),
    path('add-room/', AddRoom.as_view(), name='add-room'),
    path('add-sitephotos/', SitePhotoView.as_view(), name='add-sitephotos'),
    path('add-equipment/', AddEquipmentView.as_view(), name='add-equipment'),
    path('add-electrical-connection/', AddElectricalConnectionView.as_view(), name='add-electical-connection'),
    path('add-backup-generate-details/', BackupGeneratorView.as_view(), name='backup-generate-details'),
    path('add-miscellaneous-details/', MiscellaneousDetailsView.as_view(), name='miscellaneous-details'),

# ------------------------------------------ADD IMAGES-----------------------------------------------

    # path('add-roof-image/', AddRoofImage.as_view(), name='add-roof-image'),
    # path('add-room-image/', AddRoomImage.as_view(), name='add-room-image'),
    # path('add-sitephoto-images/', AddSiteImages.as_view(), name='add-sitephoto-images'),
    # path('add-electrical-images/', AddElectricalImages.as_view(), name='add-electical-images'),

#----------------------------------------------GET----------------------------------------------------

    path('get-client/', GetAllCustomer.as_view(), name='get-customer'),
    path('get-client-id/<int:client_id>/', GetCustomerById.as_view(), name='get-customer-id'),
    path('get-project/<str:name>/', GetProjectNameView.as_view(), name='get-project-name'),
    path('get-roof/<str:name>/', GetRoofView.as_view(), name='get-roof-name'),
    path('get-room/<str:name>/', GetRoomView.as_view(), name='get-room-name'),
    path('get-sitephotos/<str:name>/', GetSitePhotosView.as_view(), name='get-sitephotos-name'),
    path('get-equipment/<str:name>/', GetEquipmentView.as_view(), name='get-equipment-name'),
    path('get-electrical/<str:name>/', GetElectricalView.as_view(), name='get-electrical-name'),
    path('get-backup/<str:name>/', GetBackupView.as_view(), name='get-backup-name'),
    path('get-miscellaneous/<str:name>/', GetMiscellaneousView.as_view(), name='get-miscellaneous-name'),

#---------------------------------------------DELETE--------------------------------------------------

    path('delete-room/<int:client_id>/', DeleteRoomViews.as_view(), name='delete')

]