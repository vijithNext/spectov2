from rest_framework.views import APIView                               #Decalring the class method in API format
from rest_framework.response import Response                           #Uses to get response messages
from rest_framework import status                                      #import to display status message                 #uses to generate Token
from rest_framework.permissions import AllowAny                #uses to protect the api end point by tokenauthentication                                       #Uses when generate Email trigger                                                       # uses for regex operation
from django.db.models import Q                  
from api_admin.models import *
from api_admin.config import *
from api_admin.serializers import *
from webroot.utilities import *
from api_admin.config import *
from django.shortcuts import get_object_or_404

                                                                                    
#######################################################################

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

class DeleteRoomViews(APIView):

    def delete(self, request, name):
        item = get_object_or_404(Room, name=name)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
