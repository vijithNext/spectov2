from.serializers import RegisterSerializer ,UserLoginSerializer       #imports declared serializers class
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
from webroot.utilities import *
import json
from operator import itemgetter
from api_admin.config import *
from django.shortcuts import get_object_or_404

                                                                                        

############################################*/ Registration */############################################


class RegisterViews(APIView):


    def post(self,request):
            response_data={}
          
       # try:
            #headers
            mandatory_fields = ['email','name','mobile_number']     #decalares mandatory fields
            regex = re.compile('[_!#$%+^&*()<>?/\|}{~:]') 
 
            # #validation                                
            for i in mandatory_fields:
                if i not in request.data.keys():
                    return Response({
                    "status":401,
                    "message":"{} - Key missing in request".format(i)
                })
            if request.data['email']=="" or request.data['name']=="" or request.data['mobile_number']=="":
                return Response({
                    "status":402,
                    "message":"Enter all the credentials"
                })
            
            if("@" not in request.data['email'] or regex.search(request.data['email']) !=None) and request.data['email'] != "":
                return Response({
                    "status":403,
                    "message":"Invalid email"
                })

           
            serializer= RegisterSerializer(data = request.data)   
            if serializer.is_valid(raise_exception=True):             #validating the serializer method when data requested by user
                serializer.save()
                user = Registration.objects.filter(id = serializer.data['id']).first()
                if user:
                    user.user_type ='A'
                    user.save()
                    # if "alter" not in request.data.keys():                    # alter key is added while sending, for tutor and school 

                    #     UserRoles.objects.using(database).create(
                    #         user_id = user.id,
                    #         role_id = request.data['role']
                    #     )
                    if user.mobile_number == "":
                        username = user.email
                    elif user.email =="":
                        username = user.mobile_number
                    else:
                        username = "{} | {}".format(user.email,user.mobile_number)
                    send_mail ('Registration',
                    'username : {} \n password : {}'.format(username,user.dup_password),
                    'atraining23@gmail.com',
                        [user.email],
                        fail_silently=False, 
                    )

                response_data = {
                    "status":status.HTTP_201_CREATED,
                    "message":"User Created Successfully",
                
                }
                return Response(response_data)
        
        # except:
        #     return Response({
        #         "status":405,
        #         "message":"Request Error "
        #     })
    

#####################################################/* LOGIN */#########################################################

class UserLoginViews(APIView):
    """ User Login and Token generated """
    
    def post(self,request):
        response_data = {}
        serializer = UserLoginSerializer(data = request.data)
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

#################################### Forgot- password #############################################
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
        if not Registration.objects.filter(Q(email = request.data['username']) | Q(mobile_number = request.data['username'])).exists():
            return Response({
                "status":401,
                "message":"username - doesnt exists()"
            })

        if request.data['username'].isnumeric() == True:
            return Response({
                "status":403,
                "message":"sms option is not provided - try using email"
            })
        user = Registration.objects.filter(Q(email = request.data['username']) | Q(mobile_number = request.data['username'])).first()
        password = Password_Generator()
        user.set_password(password)
        user.dup_password = password
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



#######################################################################

class ChangePasswordView(APIView):

    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]

    def post(self,request):
        #headers:
        user_id = request.user.id
        mandatory_fields = ['old_password, new_password','confirm_password']
        regex = re.compile('[_!#$%+^&*()<@>?/\|}{~:]') 
        request = json.loads(request.body.decode('utf-8')) 

        #validation:
        if (request['new_password'].isalpha() == True) or (request['new_password'].isnumeric() == True) or (regex.search(request['new_password']) == None):
            return Response({
                "status":400,
                "message":"password should contain alphanumeric value and atleast one special character"
            })
        
        if len(request['new_password']) < PASSWORD_LENGTH:
            return Response({
                "status":402,
                "message":"password should contains min - 8 characters"
            })

        # for i in mandatory_fields:
        #     if i not in request.keys():
        #         return Response({
        #         "status":401,
        #         "message":"{} - Key missing in request".format(i)
        #     })
     
        user = Registration.objects.filter(id = user_id).first()
        if user:
            user.set_password(request['new_password'])
            user.dup_password = request['confirm_password']
            user.save()
            # Notification.objects.create(
            #     first_data = "Password",
            #     middle_data = "is set successfully..",
            #     content_from = "password",
            #     content_id =user.id,
            #     notification_id = request.user.id,
            #     notification_to = "A"
            # )
            return Response({
                "status":202,
                "message":"password updated"
            })
        else:
            return Response({
                "status":204,
                "message":"user not found"
            })




#######################################################################


####################################### Labour-(Add,Update,Delete) ###################################################
class userView(APIView):

    # authentication_classes=[TokenAuthentication,]
    # permission_classes=[IsAuthenticated,]

    def post(self,request):
       # try:
            #headers:
            #database = Requested_database()
            mandatory_fields = ['name','labour_id','email','mobile_number','department','dob']
            regex = re.compile('[_!#$%+^&*()<>?/\|}{~:]')

            #validation:
            for i in mandatory_fields:
                if i not in request.data.keys():
                    return Response({
                    "status":400,
                    "message":"{} - Key missing in request".format(i)
                })
            # try:
            #     token = Token.objects.get(user = request.user)
            # except:
            #     return Response({
            #         "status":401,
            #         "message":"pass valid token"
            #     })
            if Labour.objects.filter(Q(slug = request.data['labour_id'])).exists():
                return Response({
                    "status":408,
                    "message":"Labour ID already exist()"
                })
            if request.data['email'] == "" and request.data['mobile_number'] == "":
                return Response({
                    "status":401,
                    "message":"email or mobile number is mandatory"
                })
            if ("@" not in request.data['email'] or regex.search(request.data['email']) != None) and request.data['email'] != "":
                return Response({
                    "status":402,
                    "message":"invalid email"
                })
            if len(request.data['mobile_number']) != 10 or request.data['mobile_number'].isnumeric() == False:
                return Response({
                    "status":403,
                    "message":"invalid mobile number"
                })
            
            #requests:
            request_data = {
                'name':request.data['name'],
                "email":request.data['email'],
                "mobile_number":request.data['mobile_number']
                }
            # x = requests.post("{}/admin/v1/web/register/".format(settings.IP_NAME),json = request_data)
            serializer = RegisterSerializer(data = request_data)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
            if not Registration.objects.filter(Q(email = request.data['email']) & Q(mobile_number = request.data['mobile_number'])).exists():
                return Response({
                    "status":401,
                    "message":"error - unable to create user"
                })
            else:
                user = Registration.objects.filter(Q(email = request.data['email']) & Q(mobile_number = request.data['mobile_number'])).first()

            labour = Labour.objects.create(
                login_user_id       = user.id,
                name                = request.data['name'],
                slug                = request.data['labour_id'],
                mobile_number       = request.data['mobile_number'],
                email               = request.data['email'],
                labour_id           = request.data['labour_id'],
                dob                 = request.data['dob'],
                department          = request.data['department'],
                )

            #user_type - modified:
            user.user_type = 'L'
            user.save()
            labour = Labour.objects.filter(id = serializer.data['id']).first()
            #email:
            if user:
                if user.mobile_number == "":
                    username = user.email
                elif user.email =="":
                    username = user.mobile_number
                else:
                    username = "{} | {}".format(user.email,user.mobile_number)

                send_mail ('Registration',
                'username : {} \n password : {}'.format(username,user.dup_password),
                'atraining23@gmail.com',
                [user.email],
                fail_silently=False, 
                )

            return Response({
                "status":201,
                "message":"user-added",
                "email":user.email,
                "mobile_number":user.mobile_number,
                "password":user.dup_password
            })
        # except:
        #     return Response({
        #         "status":402,
        #         "message":"RequestError"
        #     })

    def get(self,request,slug):
        # try:
            #headers:
            #database = Requested_database()
            response_data = {}; handler_class = {}; handler_list = []

            #validation:
            if not Labour.objects.filter(slug = slug).exists():
                return Response({
                    "status":400,
                    "message":"not-found"
                })
            
            labour = Labour.objects.filter(slug = slug).first()
            if not Registration.objects.filter(Q(id = labour.login_user_id)).exists():
                return Response({
                    "status":401,
                    "message":"error - not a registered user"
                })
            else:
                user = Registration.objects.filter(Q(id = labour.login_user_id)).first()
            
            if user.mobile_number == "":
                username = user.email
            elif user.email == "":
                username = user.mobile_number
            else:
                username = "{} | {}".format(user.email,user.mobile_number)

            response_data = {
                "id":labour.id,
                "login_user":user.id,
                "name":labour.name,
                "mobile_number":labour.mobile_number,
                "email":labour.email,
                "department":labour.department,
                "slug":labour.slug,
                "labour_id":labour.labour_id,
                "dob":labour.dob,
                "status":labour.status,
                "username" : username,
                "password" : user.dup_password,
                "created_at":labour.created_at,
                "updated_at":labour.updated_at
            }
            return Response({
                "status":200,
                "data":response_data
            })
        # except:
        #     return Response({
        #         "status":402,
        #         "message":"RequestError"
        #     })

    def put(self,request,slug):
        # try:
            #headers:
            #database = Requested_database()
            mandatory_fields = ['name','labour_id','email','mobile_number','department','dob']

            #validation:
            for i in mandatory_fields:
                if i not in request.data.keys():
                    return Response({
                    "status":400,
                    "message":"{} - Key missing in request".format(i)
                })
            # try:
            #     token = Token.objects.get(user = request.user)
            # except:
            #     return Response({
            #         "status":401,
            #         "message":"pass valid token"
                # })
            labour = Labour.objects.filter(slug = slug).first()
            if not labour:
                return Response({
                    "status":403,
                    "message":"not-found"
                })
            if Labour.objects.filter(Q(slug = request.data['labour_id'])).exclude(id = labour.id).exists():
                return Response({
                    "status":408,
                    "message":"Labour ID already exist()"
                })

            Labour.objects.filter(slug = slug).update(
                name                = request.data['name'],
                slug                = request.data['labour_id'],
                mobile_number       = request.data['mobile_number'],
                email               = request.data['email'],
                dob                 = request.data['dob'],
                labour_id           = request.data['labour_id'],
                department          = request.data['department']
                )
            
            return Response({
                "status":202,
                "message":"user-updated"
            })
        # except:
        #     return Response({
        #         "status":405,
        #         "message":"RequestError"
        #     })

    def delete(self,request,slug):
        try:
            #headers:
            #database = Requested_database()
            response_data = {}

            #validation:
            if not Labour.objects.filter(slug = slug).exists():
                return Response({
                    "status":400,
                    "message":"Labour ID not-found"
                })
            
            labour = Labour.objects.filter(slug = slug).first()
            labour.delete()

            return Response({
                "status":200,
                "message":"user-record-deleted"
            })
        except:
            return Response({
                "status":402,
                "message":"RequestError"
            })
class UserLoginViews(APIView):
    """ User Login and Token generated """
    
    def post(self,request):
        response_data = {}
        serializer = UserLoginSerializer(data = request.data)
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



class allView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        employee = Labour.objects.all()
        serializer = LabSerializer(employee,many=True)
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})


class stdentleaveview(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format = None):
        leave = Ticket.objects.all()
        serializers = LeaveSerializer(leave, many=True)
        return Response({"data": serializers.data, "code": status.HTTP_200_OK, "message": "OK"})


class studentsleaveview(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, labour_id , format=None):
        emp_instance = Ticket.objects.filter(labour_id=labour_id)
        serializer = LeaveSerializer(emp_instance, many=True) 
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})


class studentleaveresponseview(APIView):
    permission_classes = (AllowAny,)

    def put(self,request):
        # try:
            #headers:
            # database = Requested_database()
            mandatory_fields = ['request_status','labour_id', 'description', 'day_status']

            #validation:
            for i in mandatory_fields:
                if i not in request.data.keys():
                    return Response({
                    "status":400,
                    "message":"{} - Key missing in request".format(i)
                })

            if not Ticket.objects.filter(labour_id = request.data['labour_id']).exists():
                return Response({
                    "status":401,
                    "message":"not-found"
                })
        
            studentleave = Ticket.objects.filter(labour_id = request.data['labour_id']).update(
                request_status      =   request.data['request_status']
            )
            return Response({
                "status":200,
                "message":"response-submitted"
            })

        # except:
        #     return Response({
        #         "status":401,
        #         "message":"RequestError"
        #     })

#########################################################################################






########################################################################################

class userListView(generics.ListAPIView):

    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    pagination_class = LabourListPagination

    def post(self,request):
        try:
            #headers:
            # database = Requested_database()
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

            laboour = Labour.objects.filter((Q(name__icontains = request['search_name']) | Q(labour_id__icontains = request['search_name'])) & Q(status = 1))
            for k in laboour:
                created_date = k.created_at.strftime("%d %b %Y")
                updated_date = k.updated_at.strftime("%d %b %Y")
                if k.mobile_number == "":
                    mobile_number = "-"
                else:
                    mobile_number = k.mobile_number
                if k.email == "":
                    email = "-"
                else:
                    email = k.email
                if k.status == 1:
                    status = "active"
                else:
                    status = "inactive"
                response_data = {
                    "id":k.id,
                    "slug":k.slug,
                    "labour_id":k.labour_id,
                    "name":"{}".format(k.name),
                    "email":email,
                    "department":k.department,
                    "dob":k.dob,
                    "mobile_number":mobile_number,
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

            if "order_name" in request.keys(): 
                if request['order_name'] != '':             # order_name (0-reverse or 1)
                    if request['order_name'] == "1":
                        newlist = sorted(response_list, key=itemgetter('name')) 
                    elif request['order_name'] == "0":
                        newlist = sorted(response_list, key=itemgetter('name'),reverse = True) 
            if "order_status" in request.keys(): 
                if request['order_status'] != '':            # order_status (0-reverse or 1)
                    if request['order_status'] == "1":
                        newlist = sorted(response_list, key=itemgetter('status')) 
                    elif request['order_status'] == "0":
                        newlist = sorted(response_list, key=itemgetter('status'),reverse = True) 
            if "order_email" in request.keys(): 
                if request['order_email'] != '':             # order_email (0-reverse or 1)
                    if request['order_email'] == "1":
                        newlist = sorted(response_list, key=itemgetter('email')) 
                    elif request['order_email'] == "0":
                        newlist = sorted(response_list, key=itemgetter('email'),reverse = True) 
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

        except:
            return Response({
                "status":401,
                "message":"RequestError"
            })
###################################### Task-Assign  ################################################################################
class TaskAssignView(APIView):

    # authentication_classes=[TokenAuthentication,]
    # permission_classes=[IsAuthenticated,]

    def post(self,request): #request = qn_file, subject_id, tutor_id, group_ids, section_ids, student_ids, date, time, duration, name, description
        # try:
            #headers
            #database=Requested_database()
            mandatory_fields=['labour_id','description']
            request_list = []; request_data = {}

             #validation
            for i in mandatory_fields:
                if i not in request.data.keys():
                    return Response({
                        "status":400,
                        "message":"{} - Key Missing in request" .format(i)
                    })


            # if (type(request.data['group_ids']) != list) or (type(request.data['section_ids']) != list) or (type(request.data['student_ids']) != list):
            #     return Response({
            #         "status":401,
            #         "message":"group_ids,section_ids,student_ids -  fields should be list!!!"
            #     })
            
            #assessment = TaskAssign.objects.filter((time = request.data['time'])).first()
            # if assessment:
            #     set_1 = set(assessment.group_ids)
            #     set_2 = set(assessment.section_ids)
            #     set_3 = set(assessment.student_ids)
            #     print(bool(set_1.intersection(request.data['group_ids'])))
            #     if (bool(set_1.intersection(request.data['group_ids'])) == True) or (bool(set_2.intersection(request.data['section_ids'])) == True) or (bool(set_3.intersection(request.data['student_ids'])) == True):
            #         return Response({
            #             "status":402,
            #             "message":"Already assessment is made in this timing!!!"
            #         })


            TaskAssign.objects.create(
                
                labour_id               =   request.data['labour_id'],
               # duration               =   request.data['duration'],
               # date                   =   request.data['date'],
               # time                   =   request.data['time'],
               # name                   =   request.data['name'],
                description            =   request.data['description']
                )

            return Response({
                "status":201,
                "message":"Task-Assigned"
            })
                
        # except:
        #     return Response({
        #         "status":407,
        #          "message":"RequestError"
        #     })

class TicketResponseView(generics.ListAPIView):
    # authentication_classes= [TokenAuthentication,]
    # permission_classes= [IsAuthenticated,]

    def post(self,request):
        # try:
            #headers:
            # database = Requested_database()
            mandatory_fields = ['request_status','labour_id']

            #validation:
            for i in mandatory_fields:
                if i not in request.data.keys():
                    return Response({
                    "status":400,
                    "message":"{} - Key missing in request".format(i)
                })

            if not Ticket.objects.filter(labour_id = request.data['labour_id']).exists():
                return Response({
                    "status":401,
                    "message":"not-found"
                })
        
            ticket = Ticket.objects.filter(labour_id = request.data['labour_id']).update(
                request_status      =   request.data['request_status']
            )
            return Response({
                "status":200,
                "message":"ticket-response-submitted"
            })
        # except:
        #     return Response({
        #         "status":401,
        #         "message":"RequestError"
        #     })


class ImageUploadView(APIView):
    
    def post(self,request):
        try:
            #headers:
            #database = Requested_database()
            mandatory_fields = ['image']

            #validation:
            for i in mandatory_fields:
                if i not in request.data.keys():
                    return Response({
                    "status":406,
                    "message":"{} - Key missing in request".format(i)
                })

            if request.FILES:
                serializer = ImageUploadSerializer(data = request.data)
                if serializer.is_valid(raise_exception = True):
                    serializer.save()
                    return Response({
                        "status":201,
                        "message":"image-uploaded",
                        "data":serializer.data
                    })
                else:
                    return Response({
                        "status":400,
                        "message":"upload-failed"
                    })
            else:
                return Response({
                        "status":200,
                        "message":"no-change",
                        "data":request.data
                    })
        except:
            return Response({
                        "status":401,
                        "message":"ImageFormatError"
                    })


        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})
class Imagelist(APIView):
    authentication_classes= [TokenAuthentication,]
    permission_classes= [IsAuthenticated,]
    

    def get(self, request, format=None):
        commpany = ImageUpload.objects.all()
        serializer = ImageUploadSerializer(commpany,many=True)
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})
class usesview(APIView):
   authentication_classes= [TokenAuthentication,]
   permission_classes= [IsAuthenticated,]

   def get(self, request, format=None):
        usser = user.objects.all()
        serializer =userSerializer(usser,many=True)
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})
   

class imageview(APIView):
   authentication_classes= [TokenAuthentication,]
   permission_classes= [IsAuthenticated,]
    
    
   def get(self, request, pk, format=None):
        company = ImageUpload.objects.get(id=pk)
        serializer = ImageUploadSerializer(company)
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})

   def deleteimage(request, pk):
    prod = ImageUpload.objects.get(id=pk)
    if len(prod.image) > 0:
        prod.delete()
    serializer = ImageUploadSerializer(prod,many=True)
    return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})


# class Imagedelete(APIView):
#     def delete(self,request,pk):
#         Image= ImageUpload.objects.get(id=pk)
        
#         try:
#             #headers:
#             #database = Requested_database()
#             mandatory_fields = ['id']

#             #validation:
#             for i in mandatory_fields:
#                 if i not in request.data.keys():
#                     return Response({
#                     "status":400,
#                     "message":"{} - Key missing in request".format(i)
#                 })
#             if len(request.data['id']) == 0:
#                 return Response({
#                     "status":401,
#                     "message":"pass session ids to delete it"
#                 })
#             for k in request.data['id']:
#                 if isinstance(k, int) == False:
#                     return Response({
#                     "status":402,
#                     "message":"Invlaid ID is present in the list - ID should be an integer"
#                 })
            
#             ImageUpload.objects.filter(id__in = request.data['id']).delete()
#             return Response({
#                         "status":202,
#                         "message":"session-deleted"
#                     })
#         except:
#             return Response({
#                 "status":403,
#                 "message":"RequestError"
#             })

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
        if not Registration.objects.filter(Q(email = request.data['username']) | Q(mobile_number = request.data['username'])).exists():
            return Response({
                "status":401,
                "message":"username - doesnt exists()"
            })

        if request.data['username'].isnumeric() == True:
            return Response({
                "status":403,
                "message":"sms option is not provided - try using email"
            })
        user = Registration.objects.filter(Q(email = request.data['username']) | Q(mobile_number = request.data['username'])).first()
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

        
class AttachmentView(APIView):                      #database
    
    def post(self,request):
        try:
            #headers:
           # database = Requested_database()
            mandatory_fields = ['file_name']

            #validation:
            for i in mandatory_fields:
                if i not in request.data.keys():
                    return Response({
                    "status":406,
                    "message":"{} - Key missing in request".format(i)
                })

            if request.FILES:
                serializer = AttachmentSerializer(data = request.data)
                if serializer.is_valid(raise_exception = True):
                    serializer.save()
                    return Response({
                        "status":201,
                        "message":"file-uploaded",
                        "data":serializer.data
                    })
                else:
                    return Response({
                        "status":400,
                        "message":"upload-failed"
                    })
            else:
                return Response({
                        "status":201,
                        "message":"no-change",
                        "data":request.data
                    })
        except:
            return Response({
                        "status":401,
                        "message":"FileFormatError"
                    })
class fileview(APIView):
   authentication_classes= [TokenAuthentication,]
   permission_classes= [IsAuthenticated,]
    

   def get(self, request, format=None):
        employee = Attachment.objects.all()
        serializer = AttachmentSerializer(employee,many=True)
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})
    

    
   def delete(self,request,file_name):
        try:
            #headers:
            #database = Requested_database()
            response_data = {}

            #validation:
            if not Attachment.objects.filter(file_name = file_name).exists():
                return Response({
                    "status":400,
                    "message":"file not-found"
                })
            
            labour = Attachment.objects.filter(file_name = file_name).first()
            labour.delete()

            return Response({
                "status":200,
                "message":"file-record-deleted"
            })
        except:
            return Response({
                "status":402,
                "message":"RequestError"
            })
class defaultFilesView(APIView):                      #database
    
    def post(self,request):
        # try:
            #headers:
            mandatory_fields = ['file_name']

            #validation:
            for i in mandatory_fields:
                if i not in request.data.keys():
                    return Response({
                    "status":406,
                    "message":"{} - Key missing in request".format(i)
                })

            if request.FILES:
                serializer = DefaultAttachmentSerializer(data = request.data)
                if serializer.is_valid(raise_exception = True):
                    serializer.save()
                    return Response({
                        "status":201,
                        "message":"file-uploaded",
                        "data":serializer.data
                    })
                else:
                    return Response({
                        "status":400,
                        "message":"upload-failed"
                    })
            else:
                return Response({
                        "status":201,
                        "message":"no-change",
                        "data":request.data
                    })
        # except:
        #     return Response({
        #                 "status":401,
        #                 "message":"FileFormatError"
        #             })

class defaultallview(APIView):
   authentication_classes= [TokenAuthentication,]
   permission_classes= [IsAuthenticated,]
    

   def get(self, request, format=None):
        employee = DefaultFiles.objects.all()
        serializer = DefaultAttachmentSerializer(employee,many=True)
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})
#payment:
import razorpay
client = razorpay.Client(auth=(MODE_KEY,SECRET_KEY))

class ImageUploadView(APIView):
    
    def post(self,request):
        try:
            #headers:
          #  database = Requested_database()
            mandatory_fields = ['image']

            #validation:
            for i in mandatory_fields:
                if i not in request.data.keys():
                    return Response({
                    "status":406,
                    "message":"{} - Key missing in request".format(i)
                })

            if request.FILES:
                serializer = ImageUploadSerializer(data = request.data)
                if serializer.is_valid(raise_exception = True):
                    serializer.save()
                    return Response({
                        "status":201,
                        "message":"image-uploaded",
                        "data":serializer.data
                    })
                else:
                    return Response({
                        "status":400,
                        "message":"upload-failed"
                    })
            else:
                return Response({
                        "status":200,
                        "message":"no-change",
                        "data":request.data
                    })
        except:
            return Response({
                        "status":401,
                        "message":"ImageFormatError"
                    })

class PaymentView(APIView):

    def post(self,request):
        try:
            #headers:
           # database = Requested_database()
            mandatory_fields = ['amount','currency','receipt']

            #validation:
            for i in mandatory_fields:
                if i not in request.data.keys():
                    return Response({
                    "status":400,
                    "message":"{} - Key missing in request".format(i)
                })
            if (request.data['amount'] == 0) or (type(request.data['amount']) != int):
                return Response({
                    "status":401,
                    "message":"Enter a valid amount"
                })
            if request.data['currency'] != "INR":
                return Response({
                    "status":402,
                    "message":"Pass INR in currency"
                })
            amount = (request.data['amount'])*100
            DATA = {
                    "amount" : amount,
                    "currency" : request.data['currency'],
                    "receipt" : request.data['receipt'],
                    "notes" : request.data['notes']
                }
            payment = client.order.create(data = DATA) 
            return Response({
                "key":MODE_KEY,
                "name":"ABC School",
                "description":"test mode",
                "address":"chennai",
                "image":"http://",
                "payment":payment
            })  
        except:
            return Response({
                "status":401,
                "message":"RequestError"
            })  


class TutorTokenObjectView(APIView):
    """ Retrieve user by token during refresh """

    def post(self,request):
        # try:
            #headers:
          #  database = Requested_database()
            request = json.loads(request.body.decode('utf-8'))

            #validation:
            try:
                user = Labour.objects.get(key=request['token']).user
            except Token.DoesNotExist:
                raise Http404

            if not Labour.objects.select_related('login_user').filter(login_user = user).exists():
                return Response({
                    "status":401,
                    "message":"Token passed - doesnt belongs to tutor!!"
                })

            tutor = Labour.objects.select_related('login_user').filter(login_user = user).first()
            response_data = {
                "id":Labour.login_user.id,
                "name":Labour.login_user.first_name,
                
                "email":Labour.login_user.email,
                
                "mobile_number":Labour.login_user.mobile_number,
               # "user_type":tutor.login_user.user_type[0],
                "labour_id":Labour.labour_id,
                "slug":Labour.slug,
               
                "token":request['token']
            }
            return Response({
                "status":200,
                "data":response_data
            })
        # except:
        #     return Response({
        #         "status":404,
        #         "message":"RequestError"
        #     })



#-------------------------------------------------------------------------------------

# class dayactivityView(generics.ListAPIView):
#     # authentication_classes= [TokenAuthentication,]
#     # permission_classes= [IsAuthenticated,]

#     def post(self,request):
#         # try:
#             #headers:
#             #database = Requested_database()
#             mandatory_fields = ['labour_id','description','status','day_status','name']
#             tutor_list = []

#             #validation:
#             for i in mandatory_fields:
#                 if i not in request.data.keys():
#                     return Response({
#                     "status":400,
#                     "message":"{} - Key missing in request".format(i)
#                 })

#             # if not Labour.objects.filter(login_user_id = request.user.id).exists():
#             #     return Response({
#             #         "status":401,
#             #         "message":"Cant fetch tutor data"
#             #     })

#             labour = Labour.objects.filter(login_user_id = request.user.id).first()
        
#             ticket = TaskAssign.objects.create(
#                 # login_user_id               =   labour_id.id,
#                 labour_id                   =   request.data['labour_id'],
#                 name= request.data['name'],
#                    description                =   request.data['description'],
#                 status                  =   request.data['status'],
#                 day_status=request.data['day_status']
                
#                 ticket_no                   =   Code_Generator()
#             )

#         #     username = "{} \n {} \n  {}".format(ticket.labour_id,ticket.complaint,ticket.ticket_no)
#         #     send_mail ('Ticket-Raised',
#         # 'Complaint Raised from our Client: labour_id & complaint & TicketNumber: {} \n day_status : {}'.format(username,ticket.status),
#         # 'atraining23@gmail.com',
#         #    ['atraining23@gmail.com'],
#         #     fail_silently=False, 
#         # )
#             return Response({
#                 "status":201,
#                 "message":"Task-Raised"
#             })
#         # except:
#         #     return Response({
#         #         "status":401,
#         #         "message":"RequestError"
#         #     })


# ------------------------------------- SPECTO V2----------------------------------



class AddCustomer(APIView):

    def post(self, request):
        serializer = AddCustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})
        else:
            return Response({"errors": serializer.errors, "code": status.HTTP_400_BAD_REQUEST, "message": "errors"})

class GetAllCustomer(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        customer = Client.objects.all()
        serializer = AddCustomerSerializer(customer, many=True) 
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})

class GetCustomerById(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, client_id, format=None):
        customer = Client.objects.filter(client_id=client_id)
        serializer = AddCustomerSerializer(customer, many=True) 
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})

class AddProject(APIView):

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})
        else:
            return Response({"errors": serializer.errors, "code": status.HTTP_400_BAD_REQUEST, "message": "errors"})

class AddRoof(APIView):

    def post(self, request):
        serializer = RoofSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})
        else:
            return Response({"errors": serializer.errors, "code": status.HTTP_400_BAD_REQUEST, "message": "errors"})

class AddRoom(APIView):

    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})
        else:
            return Response({"errors": serializer.errors, "code": status.HTTP_400_BAD_REQUEST, "message": "errors"})

class SitePhotoView(APIView):

    def post(self, request):
        serializer = SitePhotosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})
        else:
            return Response({"errors": serializer.errors, "code": status.HTTP_400_BAD_REQUEST, "message": "errors"})

class AddEquipmentView(APIView):

    def post(self, request):
        serializer = AddEquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})
        else:
            return Response({"errors": serializer.errors, "code": status.HTTP_400_BAD_REQUEST, "message": "errors"})


class AddElectricalConnectionView(APIView):

    def post(self, request):
        serializer = AddElecticalConnectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})
        else:
            return Response({"errors": serializer.errors, "code": status.HTTP_400_BAD_REQUEST, "message": "errors"})


class BackupGeneratorView(APIView):

    def post(self, request):
        serializer = BackupGeneratorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})
        else:
            return Response({"errors": serializer.errors, "code": status.HTTP_400_BAD_REQUEST, "message": "errors"})

class MiscellaneousDetailsView(APIView):

    def post(self, request):
        serializer = MiscellaneousDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})
        else:
            return Response({"errors": serializer.errors, "code": status.HTTP_400_BAD_REQUEST, "message": "errors"})


#--------------------------------------------------------------------------------------------------------------------------------

#get

class GetProjectNameView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, name, format=None):
        names = Project.objects.filter(name=name)
        serializer = ProjectSerializer(names, many=True) 
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})

class GetRoofView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, name, format=None):
        roofs = Roof.objects.filter(name=name)
        serializer = RoofSerializer(roofs, many=True) 
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})

class GetRoomView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, name, format=None):
        room = Room.objects.filter(name=name)
        serializer = RoomSerializer(room, many=True) 
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})

class GetSitePhotosView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, name, format=None):
        photos = SitePhotos.objects.filter(name=name)
        serializer = SitePhotosSerializer(photos, many=True) 
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})

class GetEquipmentView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, name, format=None):
        equipment = Add_Equipments_and_working_details.objects.filter(name=name)
        serializer = AddEquipmentSerializer(equipment, many=True) 
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})

class GetElectricalView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, name, format=None):
        electrical = Add_Electrical_connection_details.objects.filter(name=name)
        serializer = AddElecticalConnectionSerializer(electrical, many=True) 
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})

class GetBackupView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, name, format=None):
        backup = Add_Backup_Generator_details.objects.filter(name=name)
        serializer = BackupGeneratorSerializer(backup, many=True) 
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})

class GetMiscellaneousView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, name, format=None):
        details = Miscellaneous_Details.objects.filter(name=name)
        serializer = MiscellaneousDetailsSerializer(details, many=True) 
        return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "OK"})


#-----------------------------------------------------------------------------------------------

#put

# class PutProjectView(APIView):
#     permission_classes = (AllowAny,)

#     def put(self, request, name, format=None):
#         names = Project.objects.filter(name=name)
#         serializer = ProjectSerializer(names, many=True) 
#         return Response({"data": serializer.data, "code": status.HTTP_200_OK, "message": "Updated"})


#------------------------------------------------------------------------------------------------

#delete

class DeleteRoomViews(APIView):

    def delete(self, request, name):
        item = get_object_or_404(Room, name=name)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
