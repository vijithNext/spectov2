from django.shortcuts import render
#from.serializers import RegisterSerializer ,UserLoginSerializer        #imports declared serializers class
from rest_framework.views import APIView                               #Decalring the class method in API format
from rest_framework.response import Response                           #Uses to get response messages
from rest_framework import status                                      #import to display status message
from rest_framework.authtoken.models import Token                      #uses to generate Token
from rest_framework.permissions import AllowAny, IsAuthenticated                 #uses to protect the api end point by tokenauthentication            
from rest_framework .authentication import TokenAuthentication         #uses to implement tokenauthemtication
# from django.core.mail import send_mail                               #Uses when generate Email trigger     
import re                                                              # uses for regex operation
from django.db.models import Q                  
from api_admin.models import *
from rest_framework import generics
from api_admin.config import *
from api_admin.serializers import *
from api_user.serializers import *
from webroot.utilities import *
import json
from operator import itemgetter



class LoginViews(APIView):
    """ User Login and Token generated """
    
    def post(self,request):
        response_data = {}
        serializer = LoginSerializer(data = request.data)
        try:

            if serializer.is_valid(raise_exception = True):
                token = serializer.validated_data['token']
            
                response_data = {
                    "status":status.HTTP_202_ACCEPTED,
                    "message":"Login Successful",
                    "token":token
                }
                return Response(response_data)
        except:
            return  Response({
                "status":status.HTTP_204_NO_CONTENT,
                "message": "invalid data"
            })


########################################### Forgot-password #################################################################


class ForgotPasswordView(APIView):

    def post(self,request):
        #headers:
        mandatory_fields = ['username']
        response_data = {}; 

        #validation:
        for i in mandatory_fields:
            if i not in request.data.keys():
                return Response({
                "status":400,
                "message":"{} - Key missing in request".format(i)
            })
        if (request.data['username'].isnumeric() == False) and ('@' not in request.data['username']):
            return Response({
                "status":402,
                "message":"username is invalid"
            })
        if not Labour.objects.filter(Q(email = request.data['username']) | Q(mobile_number = request.data['username'])).exists():
            return Response({
                "status":401,
                "message":"username - doesnt exists()"
            })

        if request.data['username'].isnumeric() == True:
            return Response({
                "status":403,
                "message":"sms option is not provided - try using email"
            })
        user = Labour.objects.filter(Q(email = request.data['username']) | Q(mobile_number = request.data['username'])).first()
        user.set_password(Password_Generator())
        user.save()
        if user.mobile_number == "":
            username = user.email
        elif user.email =="":
            username = user.mobile_number
        else:
            username = "{} | {}".format(user.email,user.mobile_number)

        send_mail ('Reset-password',
        'Ur account has been reset with the following credentials.Please, Login with this credential: username : {} \n password : {}'.format(username,user.dup_password),
        'atraining23@gmail.com',
            [user.email],
            fail_silently=False, 
        )
        
        return Response({
            "status":202,
            "message":"mail has been sent to registered mailID"
        })

##################################### Task-List  ##################################################################################


class TaskListView(generics.ListAPIView):

    # authentication_classes=[TokenAuthentication,]
    # permission_classes=[IsAuthenticated,]
    pagination_class = TaskListPagination

    def post(self,request):
        #try:
            #headers:
            mandatory_fields = ['search_name']
            request = json.loads(request.body.decode('utf-8'))
            response_list = []; newlist = []

            #validation:
            for i in mandatory_fields:
                if i not in request.keys():
                    return Response({
                    "status":400,
                    "message":"{} - Key missing in request".format(i)
                })

            labour = TaskAssign.objects.filter((Q(description__icontains = request['search_name']) | Q(labour_id__icontains = request['search_name'])) & Q(status = 1))
            for k in labour:
                created_date = k.created_at.strftime("%d %b %Y")
                updated_date = k.updated_at.strftime("%d %b %Y")
                if k.description == "":
                    description = "-"
                else:
                    description = k.description
                if k.labour_id == "":
                    labour_id = "-"
                else:
                    labour_id = k.labour_id
                if k.status == 1:
                    status = "active"
                else:
                    status = "inactive"
                response_data = {
                    "id":k.id,
                    "labour_id":k.labour_id,
                    "description":k.description,
                    "status":status,
                    "created_at":created_date,
                    "updated_at":updated_date
                }
                response_list.append(response_data)
            newlist = sorted(response_list, key=itemgetter('updated_at'),reverse = True)

            k = 1        
            for i in newlist:
                i['serial_no'] = k
                k = k+1

            
            if "order_status" in request.keys(): 
                if request['order_status'] != '':            # order_status (0-reverse or 1)
                    if request['order_status'] == "1":
                        newlist = sorted(response_list, key=itemgetter('status')) 
                    elif request['order_status'] == "0":
                        newlist = sorted(response_list, key=itemgetter('status'),reverse = True)  
            if "order_labour_number" in request.keys(): 
                if request['order_labour_number'] != '':       # order_emp_number (0-reverse or 1)
                    if request['order_labour_number'] == "1":
                        newlist = sorted(response_list, key=itemgetter('labour_id')) 
                    elif request['order_labour_number'] == "0":
                        newlist = sorted(response_list, key=itemgetter('labour_id'),reverse = True) 
            if "order_created" in request.keys(): 
                if request['order_created'] != '':          # order_created (0-reverse or 1)
                    if request['order_created'] == "1":
                        newlist = sorted(response_list, key=itemgetter('created_at')) 
                    elif request['order_created'] == "0":
                        newlist = sorted(response_list, key=itemgetter('created_at'),reverse = True) 
            if "order_updated" in request.keys(): 
                if request['order_updated'] != '':          # order_updated (0-reverse or 1)
                    if request['order_updated'] == "1":
                        newlist = sorted(response_list, key=itemgetter('updated_at')) 
                    elif request['order_updated'] == "0":
                        newlist = sorted(response_list, key=itemgetter('updated_at'),reverse = True) 
            
            page = self.paginate_queryset(newlist)
            return self.get_paginated_response(page)

        # except:
        #     return Response({
        #         "status":401,
        #         "message":"RequestError"
        #     })

################################ Ticket ###################################################################################


class LeaveRequestView(generics.ListAPIView):
    # authentication_classes= [TokenAuthentication,]
    # permission_classes= [IsAuthenticated,]

    def post(self,request):
        # try:
            #headers:
            #database = Requested_database()
            mandatory_fields = ['labour_id','description', 'day_status',]
            tutor_list = []

            #validation:
            for i in mandatory_fields:
                if i not in request.data.keys():
                    return Response({
                    "status":400,
                    "message":"{} - Key missing in request".format(i)
                })

            # if not Labour.objects.filter(login_user_id = request.user.id).exists():
            #     return Response({
            #         "status":401,
            #         "message":"Cant fetch tutor data"
            #     })

            labourr = Labour.objects.filter(login_user_id = request.user.id).first()
        
            ticket = Ticket.objects.create(
                #login_user_id               =   labour.id,
                labour_id                   =   request.data['labour_id'],
                description                 =   request.data['description'],
                day_status                  =   request.data['day_status'],
                ticket_no                   =   Code_Generator()
            )

            username = "{} \n {} \n  {}".format(ticket.labour_id,ticket.description,ticket.ticket_no)
            send_mail ('Ticket-Raised',
        'Complaint Raised from our Client: labour_id & complaint & TicketNumber: {} \n day_status : {}'.format(username,ticket.day_status),
        'atraining23@gmail.com',
           ['atraining23@gmail.com'],
            fail_silently=False, 
        )
            return Response({
                "status":201,
                "message":"leave-Raised",
                # "ticket_no":Ticket.ticket_no
            })
        # except:
        #     return Response({
        #         "status":401,
        #         "message":"RequestError"
        #     })


# -------------------------------------------------------


class Leaveresponseview(APIView):
    
    permission_classes = (AllowAny,)

    def get(self, request, labour_id , format=None):
        emp_instance = Ticket.objects.filter(labour_id=labour_id)
        serializer = LeaveSerializer(emp_instance, many=True) 
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})


# ======================================================

###################################  TicketNumber-view   #######################################################################
# class TicketListView(generics.ListAPIView):

#     # authentication_classes=[TokenAuthentication,]
#     # permission_classes=[IsAuthenticated,]
#     # pagination_class = TaskListPagination

#     def post(self,request):
#         #try:
#             #headers:
#             mandatory_fields = ['search_name']
#             request = json.loads(request.body.decode('utf-8'))
#             response_list = []; newlist = []

#             #validation:
#             for i in mandatory_fields:
#                 if i not in request.keys():
#                     return Response({
#                     "status":400,
#                     "message":"{} - Key missing in request".format(i)
#                 })

#             ticket = Ticket.objects.filter((Q(ticket_no__icontains = request['search_name']) | Q(labour_id__icontains = request['search_name'])) & Q(status = 1))
#             for k in ticket:
#                 created_date = k.created_at.strftime("%d %b %Y")
#                 updated_date = k.updated_at.strftime("%d %b %Y")
#                 if k.ticket_no == "":
#                     ticket_no = "-"
#                 else:
#                     ticket_no = k.ticket_no
#                 if k.labour_id == "":
#                     labour_id = "-"
#                 else:
#                     labour_id = k.labour_id
#                 if k.status == 1:
#                     status = "active"
#                 else:
#                     status = "inactive"
#                 response_data = {
#                     "id":k.id,
#                     "ticket_no":k.ticket_no,
#                     "labour_id":k.labour_id,
#                     "request_status":k.request_status,
#                     "status":status,
#                     "created_at":created_date,
#                     "updated_at":updated_date
#                 }
#                 response_list.append(response_data)
#             newlist = sorted(response_list, key=itemgetter('updated_at'),reverse = True)

#             k = 1        
#             for i in newlist:
#                 i['serial_no'] = k
#                 k = k+1

            
#             if "order_status" in request.keys(): 
#                 if request['order_status'] != '':            # order_status (0-reverse or 1)
#                     if request['order_status'] == "1":
#                         newlist = sorted(response_list, key=itemgetter('status')) 
#                     elif request['order_status'] == "0":
#                         newlist = sorted(response_list, key=itemgetter('status'),reverse = True)  
#             if "order_labour_number" in request.keys(): 
#                 if request['order_labour_number'] != '':       # order_emp_number (0-reverse or 1)
#                     if request['order_labour_number'] == "1":
#                         newlist = sorted(response_list, key=itemgetter('labour_id')) 
#                     elif request['order_labour_number'] == "0":
#                         newlist = sorted(response_list, key=itemgetter('labour_id'),reverse = True) 
#             if "order_created" in request.keys(): 
#                 if request['order_created'] != '':          # order_created (0-reverse or 1)
#                     if request['order_created'] == "1":
#                         newlist = sorted(response_list, key=itemgetter('created_at')) 
#                     elif request['order_created'] == "0":
#                         newlist = sorted(response_list, key=itemgetter('created_at'),reverse = True) 
#             if "order_updated" in request.keys(): 
#                 if request['order_updated'] != '':          # order_updated (0-reverse or 1)
#                     if request['order_updated'] == "1":
#                         newlist = sorted(response_list, key=itemgetter('updated_at')) 
#                     elif request['order_updated'] == "0":
#                         newlist = sorted(response_list, key=itemgetter('updated_at'),reverse = True) 
            
#             page = self.paginate_queryset(newlist)
#             return self.get_paginated_response(page)

#         # except:
#         #     return Response({
#         #         "status":401,
#         #         "message":"RequestError"
#         #     })


################################################################################



