import re
from typing import ClassVar
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers                       
from django.contrib.auth import authenticate                 # use to declare auth model type
from rest_framework import status                            # uses to get status response message
from.models import Client, Project, Registration, Labour, Roof, Room, SitePhotos                              # calls declared class name from the models            
from rest_framework.authtoken.models import Token            # uses while generate token
from api_admin.models import Labour, Miscellaneous_Details, Registration, ImageUpload, DefaultFiles, Ticket, Attachment, Client, Room, Roof, SitePhotos, Add_Equipments_and_working_details, Add_Electrical_connection_details, Add_Backup_Generator_details
from webroot.utilities import*
#import base64


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = [
                    'id',
                    'email',
                    'dup_password',
                    'name',
                    'mobile_number',
                    'status',
                    'created_at',
                    'updated_at'
                   
                
                    
                ]
        read_only_fields = [
                            'status',
                            'dup_password',
                            'created_at',
                            'updated_at'
                            ]

    def create(self,validated_data):

        user = Registration.objects.create_user(                          
        email           =   validated_data['email'],
        password        =   Password_Generator(),
        name            =   validated_data['name'],
        mobile_number   =   validated_data['mobile_number']

    )

        return user

###################################################*/ LOGIN */###########################################################

class UserLoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)

    def validate(self,data):
        email = data.get('email')
        password = data.get('password')
        if email and password:
            user=Registration.objects.filter(email=email).first()
            
        if (user.check_password(password)==True):
            token,created = Token.objects.get_or_create(user = user)
            data['token'] = token.key
        
        return data
class ImageUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageUpload
        fields = [
            'id',
            'image',
            'status',
            'created_at',
            'updated_at'
        ]

        read_only_fields = [
            'status',
            'created_at',
            'updated_at'
        ]


class LabSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()

    class Meta:
        model = Labour
        fields = (
            'login_user','name','department','slug','labour_id','mobile_number', 'email', 'dob', 'status', 'created_at', 'updated_at', 'company_name'
            )

    def get_company_name(self,obj):
        company = Labour.objects.get(name=obj.name)
        return company.company_name 


class LeaveSerializer(serializers.ModelSerializer):
    leavee = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = ('labour_id', 'description', 'ticket_no', 'day_status', 'request_status', 'status', 'created_at', 'updated_at', 'description','leavee')
    
    def get_leavee(self,obj):
        leave_view = Ticket.objects.get(id=obj.labour_id)
        return leave_view.leavee


class AttachmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attachment
        fields = [
            'id',
            'file_name',
            'status',
            'created_at',
            'updated_at'
        ]

        read_only_fields = [
            'status',
            'created_at',
            'updated_at'
        ]
class DefaultAttachmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = DefaultFiles
        fields = [
            'id',
            'file_name',
            'status',
            'created_at',
            'updated_at'
        ]

        read_only_fields = [
            'status',
            'created_at',
            'updated_at'
        ]


############################# ########################### ############################ #############################

#------------------- septov2 -------------------

class AddCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = [
                    'client_id',
                    'name',
                    'email',
                    'phone'
                ]

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = [
                    'client_id',
                    'name',
                    'project_name',
                ]

class RoofSerializer(serializers.ModelSerializer):

    class Meta:
        model = Roof
        fields = [
                    'client_id',
                    'name',
                    'project_name',
                    'field1',
                    'field2',
                    'field3',
                    'images'
                ]


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = [
                    'client_id',
                    'name',
                    'project_name'
                    'create_room',
                    'images',
                    'equipments',
                    'wattage',
                    'quantity'
                ]


class SitePhotosSerializer(serializers.ModelSerializer):

    class Meta:
        model = SitePhotos
        fields = [
                    'client_id',
                    'name',
                    'project_name'
                    'fount_of_building',
                    'array',
                    'meter_close_up',
                    'proposed_disconnected_location',
                    'south_house',
                    'south_yard',
                    'electrical_panel_location',
                    'electrical_panel_circute_breakers',
                    'roof_pitch_proposed_inverter_and_bank_location',
                    'proposed_efficiency_upgrade_location'
                ]

class AddEquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Add_Equipments_and_working_details
        fields = [
                    'client_id',
                    'name',
                    'project_name'
                    'inverter_mounting_type',
                    'ventilated_room',
                    'dc_cable_run_in_m',
                    'building_CAD_drawings_available',
                    'building_electrical_drawings_available'

                ]        


class AddElecticalConnectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Add_Electrical_connection_details
        fields = [
                    'client_id',
                    'name',
                    'project_name'
                    'Electricity_provider',
                    'sc_no',
                    'capture_connection_no',
                    'previous_monthly_bills_copy',
                    'service',
                    'other_reason',
                    'voltage',
                    'phase',
                    'available_breaker_space',
                    'capture_breaker_space_image',
                    'Separate_electrical_room_available',
                    'capture_electrical_room',
                    'cable_routing',
                    'capture_connection_number',
                    'roof_to_electrical_room_cable_length_in_m',
                ] 

class BackupGeneratorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Add_Backup_Generator_details
        fields = [
                    'client_id',
                    'name',
                    'project_name'
                    'is_backup_generate_available',
                    'make',
                    'capacity_in_KVA',
                    'electrical_phase',
                    'auto_start_option_available',
                    'daily_operations_hours',
                    'change_over_switch_rating'
                ]

class MiscellaneousDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Miscellaneous_Details
        fields = [
                    'client_id',
                    'name',
                    'project_name'
                    'earthing_pit_visibility',
                    'details',
                    'easy_access_to_roof',
                    'details',
                    'need_of_scaffoiding_during_installation',
                    'details',
                    'available_of_wedding_facility_in_site',
                    'details',
                    'availability_of_crane_service',
                    'details',
                    'availability_of_ladder_facility',
                    'details',
                    'availability_of_building_electricion',
                    'details'
                ]

#-----------------------------------------------------------------------------------------------------------------------------------

