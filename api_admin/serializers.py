from rest_framework import serializers                                     
from.models import Client, Project, Roof, Room, SitePhotos       
from api_admin.models import * 
from webroot.utilities import *
#import base64

#------------------- septov2 -------------------

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = [
                    'client_id',
                    'name',
                    'contact_person_name',
                    'email_1',
                    'phone_number_1',
                    'secondary_contact_person',
                    'email_2',
                    'phone_number_2',
                    'address',
                    'postal_code',
                    'city',
                    'province',
                    'country',
                    'lattitude',
                    'longitude',
                    'description',
                    'selected_id'
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

# class RoofImageSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = RoofImage
#         fields = [
#                     'client_id',
#                     'images',
#                 ]


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = [
                    'client_id',
                    'name',
                    'project_name',
                    'create_room',
                    'room_name',
                    'add_drawing',
                    'equipments',
                    'wattage',
                    'quantity'
                ]

# class RoomImageSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = RoomImage
#         fields = [
#                     'client_id',
#                     'add_drawing'
#                 ]

class SitePhotosSerializer(serializers.ModelSerializer):

    class Meta:
        model = SitePhotos
        fields = [
                    'client_id',
                    'name',
                    'project_name',
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

# class SiteImageSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = SiteImages
#         fields = [
#                     'client_id',
#                     'fount_of_building',
#                     'array',
#                     'meter_close_up',
#                     'proposed_disconnected_location',
#                     'south_house',
#                     'south_yard',
#                     'electrical_panel_location',
#                     'electrical_panel_circute_breakers',
#                     'roof_pitch_proposed_inverter_and_bank_location',
#                     'proposed_efficiency_upgrade_location'
#                 ]

class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipments_details
        fields = [
                    'client_id',
                    'name',
                    'project_name',
                    'inverter_mounting_type',
                    'ventilated_room',
                    'dc_cable_run_in_m',
                    'building_CAD_drawings_available',
                    'building_electrical_drawings_available'

                ]        


class ElecticalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Electrical_details
        fields = [
                    'client_id',
                    'name',
                    'project_name',
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

# class ElectricalSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = ElectricalImages
#         fields = [
#                     'client_id',
#                     'capture_connection_no',
#                     'previous_monthly_bills_copy',
#                     'capture_breaker_space_image',
#                     'capture_electrical_room',
#                     'capture_connection_number'
#                 ]

class BackupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Backup_details
        fields = [
                    'client_id',
                    'name',     
                    'project_name',
                    'is_backup_generate_available',
                    'make',
                    'capacity_in_KVA',
                    'electrical_phase',
                    'auto_start_option_available',
                    'daily_operations_hours',
                    'change_over_switch_rating'
                ]

class MiscellaneousSerializer(serializers.ModelSerializer):

    class Meta:
        model = Miscellaneous_Details
        fields = [
                    'client_id',
                    'name',
                    'project_name',
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

