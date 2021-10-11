from api_admin.views import *                       #import classnames from views.py
from django.urls import path
from api_user.views import *



urlpatterns=[
    path("login/",LoginViews.as_view(),name='login'),
    
    
    path("forgot-password/",ForgotPasswordView.as_view(),name='forgot-password'),

    # path("forgot-password/",UserForgotPasswordView.as_view(),name='forgot-password'),

    path( "task-list/",TaskListView.as_view(),name='task-list'),
    
    path("leaverequest/",LeaveRequestView.as_view(),name='ticket'),

    # path("leave-view/",TicketListView.as_view(),name='ticket-view'),

    path("userleaveresponse/<str:labour_id>/", Leaveresponseview.as_view(), name='leaveresponse'),


]