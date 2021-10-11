from api_admin.views import *                       #import classnames from views.py
from django.urls import path




urlpatterns=[
    
    path( "registration/",RegisterViews.as_view(),name = 'register'),
              # declares the name of api end points
    path("login/",UserLoginViews.as_view(),name='login'),

    path( "imageupload/",ImageUploadView.as_view(),name = 'image'),

    path( "alllabour/",usesview.as_view(),name = 'image'), 

    path( "imagelist/",Imagelist.as_view(),name = 'image'), 
   
    path( "fileupload/",AttachmentView.as_view(),name = 'fileupload'),

    path( "fileall/<str:name>/",fileview.as_view(),name = 'fileupload'),

    path( "fileall/",fileview.as_view(),name = 'fileall'),

    path( "defaultfile/",defaultFilesView.as_view(),name = 'defaultfile'),
    
    path( "defaultall/",defaultallview.as_view(),name = 'default'),
    
   #  path('payment/',PaymentView.as_view(),name="payment"),
    # path('token/',TokenObjectView.as_view(),name="payment"),


    path("forgot-password/",ForgotPasswordView.as_view(),name='forgot-password'),



    path( "list/",allView.as_view(),name='user-view'),


    path('allleavelist/', stdentleaveview.as_view(), name='leave-list'),

    path('leavelist/<str:labour_id>/', studentsleaveview.as_view(), name='leave-list'),

    path('leaveresponse/', studentleaveresponseview.as_view(), name='leave-list'),

    path('change-password/', ChangePasswordView.as_view(), name='change-password'),


    path( "user-add/",userView.as_view(),name='user-add'),

    # path( "user-add/",userView.as_view(),name='user-add'),

    path("user-add/<slug:slug>/",userView.as_view(),name='user-view'),

    path( "user-list/",userListView.as_view(),name='user-view'),

    #----------------------------------------------------------------------------------

    # path("dayactivity/<str:labour_id>/",dayactivityView.as_view(), name='dayactivity')

    #-----------------------------------------------------------------------------------


# --------------------------------------- SPECTO V2----------------------------------

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




    # path('list-client/<int:client_id>', ListClient.as_view(), name='list-client'),



]