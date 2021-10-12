from api_admin.views import *                       #import classnames from views.py
from django.urls import path




urlpatterns=[

#----------------------------------------------ADD---------------------------------------------------

    path('add-client/', AddCustomer.as_view(), name='add-customer'),
    path('get-customer/', GetAllCustomer.as_view(), name='get-customer'),
    path('get-customer-id/<int:client_id>/', GetCustomerById.as_view(), name='get-customer-id'),

    path('add-project/', AddProject.as_view(), name='add-project'),
    
    path('add-roof/', AddRoof.as_view(), name='add-roof'),
    path('add-room/', AddRoom.as_view(), name='add-room'),
    path('add-sitephotos/', SitePhotoView.as_view(), name='add-sitephotos'),
    path('add-equipment/', AddEquipmentView.as_view(), name='add-equipment'),
    path('add-electrical-connection/', AddElectricalConnectionView.as_view(), name='add-electical-connection'),
    path('backup-generate-details/', BackupGeneratorView.as_view(), name='backup-generate-details'),
    path('miscellaneous-details/', MiscellaneousDetailsView.as_view(), name='miscellaneous-details'),

#----------------------------------------------GET----------------------------------------------------

    path('get-project-name/<str:name>/', GetProjectNameView.as_view(), name='get-project-name'),
    path('get-roof-name/<str:name>/', GetRoofView.as_view(), name='get-roof-name'),
    path('get-room-name/<str:name>/', GetRoomView.as_view(), name='get-room-name'),
    path('get-sitephotos-name/<str:name>/', GetSitePhotosView.as_view(), name='get-sitephotos-name'),
    path('get-equipment-name/<str:name>/', GetEquipmentView.as_view(), name='get-equipment-name'),
    path('get-electrical-name/<str:name>/', GetElectricalView.as_view(), name='get-electrical-name'),
    path('get-backup-name/<str:name>/', GetBackupView.as_view(), name='get-backup-name'),
    path('get-miscellaneous-name/<str:name>/', GetMiscellaneousView.as_view(), name='get-miscellaneous-name'),

#---------------------------------------------DELETE--------------------------------------------------

    path('delete-room/<str:name>/', DeleteRoomViews.as_view(), name='delete')

]