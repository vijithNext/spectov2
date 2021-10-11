from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser             #package which is used to inherit properties from basemanager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.db.models.lookups import Transform              # package which is used to set working logic and stores in DB
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token                   #use to generate token
#from app.storage import OverwriteStorage

class RegisterManager(BaseUserManager):

    def create_user(self,email,password ,**data):
        user = self.model(
        name             =   data.get('name'),
        mobile_number    =   data.get('mobile_number'),
        email            =   email,
        )
        
        user.set_password(password)
        user.dup_password=password
        user.save(using = self._db)
        return user

    def create_superuser(self,email,password , **data):       
        user = self.create_user(email,password , **data)
        user.is_superuser = True
        user.user_type = 'A'
        user.save(using = self._db)
        return user

class ImageUpload(models.Model):
    image           =   models.ImageField(max_length=5000, upload_to='image/', blank=True, null=True)
    status          =   models.IntegerField(default = 1)
    created_at      =   models.DateTimeField(auto_now_add=True,null=True)
    updated_at      =   models.DateTimeField(auto_now=True,null=True)


class Registration(AbstractBaseUser,PermissionsMixin):
    """ New User registration """

    email           =   models.EmailField(unique= True)                       # default command
    password        =   models.CharField(max_length=255)
    dup_password    =   models.CharField(max_length=255)
    name            =   models.CharField(max_length=255, null=True, blank=True, default=None)
    mobile_number   =   models.CharField(max_length=255,null=True, blank=True)
    user_type       =   models.CharField(max_length=255,null=True, blank=True)
    status          =   models.IntegerField(default=1)
    created_at      =   models.DateTimeField(auto_now_add=True)
    updated_at      =   models.DateTimeField(auto_now=True)
    



    objects = RegisterManager()

    USERNAME_FIELD = 'email'                                                                #declares email as a username
    REQUIRED_FIELDS = ['name','mobile_number']

    def __str__(self):
        return self.email
@receiver(post_save, sender=settings.AUTH_USER_MODEL)                                        #declares authuser at decoration
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        


class Labour(models.Model):
    login_user          =   models.ForeignKey(Registration, on_delete = models.CASCADE)
    name                =   models.CharField(max_length=255, null=True, blank=True)
    department          =   models.CharField(max_length=255, null=True, blank=True)
    slug                =   models.CharField(max_length=255, null=True, blank=True)
    labour_id           =   models.CharField(max_length=255, null=True, blank=True)
    mobile_number       =   models.CharField(max_length=255, null=True, blank=True)
    email               =   models.CharField(max_length=255, null=True, blank=True)
    dob                 =   models.CharField(max_length=255, null=True, blank=True)
    status              =   models.IntegerField(default = 1)
    created_at          =   models.DateTimeField(auto_now_add=True,null=True)
    updated_at          =   models.DateTimeField(auto_now=True,null=True)
    company_name        =   models.CharField(max_length=255, null=True, blank=True)

    
class TaskAssign(models.Model):
    labour_id                   =   models.CharField(max_length=255,null=True,blank=True)
    description                 =   models.CharField(max_length=255,null=True,blank=True)
    created_at                  =   models.DateTimeField(auto_now_add=True,null=True)
    updated_at                  =   models.DateTimeField(auto_now=True,null=True)
    status                      =   models.IntegerField(default = 1)

class Ticket(models.Model):
    #login_user                  =   models.ForeignKey(Registration, on_delete=models.CASCADE)
    labour_id                   =   models.CharField(max_length=255,null=True,blank=True)
    description                 =  models.CharField(max_length=255,null=True,blank=True)
    ticket_no                   =   models.CharField(max_length=255,null=True,blank=True)
    # from_date                 =   models.DateField()
    # to_date                   =   models.DateField()
    day_status                  =   models.CharField(max_length=255,default = "full") #full or half
    request_status              =   models.CharField(max_length=255,default = "pending") #pending, on_hold, rejected, approved
    status                      =   models.IntegerField(default=1)
    created_at                  =   models.DateTimeField(auto_now_add=True,null=True)
    updated_at                  =   models.DateTimeField(auto_now=True,null=True)
    leavee                      = models.CharField(max_length=255, null=True, blank=True)

    # description = models.CharField(max_length=255,null=True,blank=True)

# class User(AbstractBaseUser,PermissionsMixin):
#     """ New User registration """

#     first_name      =   models.CharField(max_length=255, null=True, blank=True)
#     last_name       =   models.CharField(max_length=255,null=True, blank=True)
#     email           =   models.CharField(max_length=255,null=True, blank=True)
#     mobile_number   =   models.CharField(max_length=255,null=True, blank=True)
#     password        =   models.CharField(max_length=255)
#     dup_password    =   models.CharField(max_length=255,null = True)
#     user_type       =   models.CharField(max_length=255,null=True, blank=True)    # A - admin, S - student, T - Tutor, SA - Super Admin
    
#     code            =   models.CharField(max_length=255,unique = True) 
#     status          =   models.IntegerField(default = 1)
#     created_at      =   models.DateTimeField(auto_now_add=True,null=True)
#     updated_at      =   models.DateTimeField(auto_now=True,null=True)


#     objects = RegisterManager()

#     USERNAME_FIELD = 'code'
#     REQUIRED_FIELDS = ['first_name','last_name']

#     def __str__(self):
#         return self.codes
class Attachment(models.Model):
    file_name       =   models.FileField(max_length=5000, upload_to='file/', blank=True, null=True)
    status          =   models.IntegerField(default = 1)
    created_at      =   models.DateTimeField(auto_now_add=True,null=True)
    updated_at      =   models.DateTimeField(auto_now=True,null=True)
class DefaultFiles(models.Model):
    file_name       =   models.FileField(max_length=5000, upload_to='default/', blank=True, null=True)
    status          =   models.IntegerField(default = 1)
    created_at      =   models.DateTimeField(auto_now_add=True,null=True)
    updated_at      =   models.DateTimeField(auto_now=True,null=True)


# ----------===============------------- SPECTO V2 ---------------===============-------------


class Client(models.Model):
    client_id = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=255,null=True,blank=True)

class Project(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    project_name = models.CharField(max_length=250, blank=True, null=True)

class Roof(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    project = models.CharField(max_length=200)
    field1 = models.CharField(max_length=255,null=True,blank=True)
    field2 = models.CharField(max_length=255,null=True,blank=True)
    field3 = models.CharField(max_length=255,null=True,blank=True)
    images = models.ImageField(upload_to = 'images_api/roof_img/')


class Room(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    create_room = models.CharField(max_length=200, blank=True, null=True)
    images = models.ImageField(upload_to = 'images_api/room_img/')
    equipments = models.CharField(max_length=200,null=True,blank=True)
    wattage = models.CharField(max_length=200,null=True,blank=True)
    quantity = models.CharField(max_length=200,null=True,blank=True)

class SitePhotos(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)	
    fount_of_building = ImageField(upload_to = 'images_api/front_building/')
    array = ImageField(upload_to = 'images_api/array/')
    meter_close_up = ImageField(upload_to = 'images_api/meter_close_up/')
    proposed_disconnected_location = ImageField(upload_to = 'images_api/proposed/')
    south_house = ImageField(upload_to = 'images_api/south_house')
    south_yard = ImageField(upload_to = 'images_api/south_yard')
    electrical_panel_location = ImageField(upload_to = 'images_api/electrical_panel')
    electrical_panel_circute_breakers = ImageField(upload_to = 'images_api/electrical_panel_breakes')
    roof_pitch_proposed_inverter_and_bank_location = ImageField(upload_to = 'images_api/roof_pitch')
    proposed_efficiency_upgrade_location = ImageField(upload_to = 'images_api/proposed_effiency')

class Add_Equipments_and_working_details(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)	
    inverter_mounting_type = models.CharField(max_length=200, blank=True, null=True)
    ventilated_room = models.CharField(max_length=200, null=True, blank=True)
    dc_cable_run_in_m = models.CharField(max_length=200, blank=True, null=True)
    building_CAD_drawings_available = models.CharField(max_length=200, blank=True, null=True)
    building_electrical_drawings_available = models.CharField(max_length=200, blank=True, null=True)

class Add_Electrical_connection_details(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)	
    Electricity_provider = models.CharField(max_length=200, blank=True, null=True)
    sc_no = models.CharField(max_length=200, blank=True, null=True)
    capture_connection_no = models.ImageField(upload_to = 'images_api/connection_no/')
    previous_monthly_bills_copy = models.ImageField(upload_to = 'images_api/mothly_bills/')
    service = models.CharField(max_length=200)
    other_reason = models.CharField(max_length=200, blank=True, null=True)
    voltage = models.CharField(max_length=100)
    phase = models.CharField(max_length=150)
    available_breaker_space = models.CharField(max_length=200)
    capture_breaker_space_image = models.ImageField(upload_to = 'images_api/breaker_space_image/')
    Separate_electrical_room_available = models.CharField(max_length=100)
    capture_electrical_room = models.ImageField(upload_to = 'images_api/capture_electrical_room/')
    cable_routing = models.CharField(max_length=100)
    capture_connection_number = models.ImageField(upload_to = 'images/api/capture_connection_no/')
    roof_to_electrical_room_cable_length_in_m = models.CharField(max_length=255)

class Add_Backup_Generator_details(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)	
    is_backup_generate_available = models.CharField(max_length=155, blank=True, null=True)
    make = models.CharField(max_length=255, blank=True, null=True)
    capacity_in_KVA = models.CharField(max_length=255, null=True, blank=True)
    electrical_phase = models.CharField(max_length=155, blank=True, null=True)
    auto_start_option_available = models.CharField(max_length=155, blank=True, null=True)
    daily_operations_hours = models.CharField(max_length=255, blank=True, null=True)
    change_over_switch_rating = models.CharField(max_length=255, blank=True, null=True)

class Miscellaneous_Details(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)	
    earthing_pit_visibility = models.CharField(max_length=155)
    details = models.CharField(max_length=255, blank=True, null=True)
    easy_access_to_roof = models.CharField(max_length=155, blank=True, null=True)
    details = models.CharField(max_length=255, blank=True, null=True)
    need_of_scaffoiding_during_installation = models.CharField(max_length=200, blank=True, null=True)
    details = models.CharField(max_length=200, blank=True, null=True)
    available_of_wedding_facility_in_site = models.CharField(max_length=200, blank=True, null=True)
    details = models.CharField(max_length=200, blank=True, null=True)
    availability_of_crane_service = models.CharField(max_length=200, blank=True, null=True)
    details = models.CharField(max_length=200, blank=True, null=True)
    availability_of_ladder_facility = models.CharField(max_length=200, blank=True, null=True)
    details = models.CharField(max_length=200, blank=True, null=True)
    availability_of_building_electricion = models.CharField(max_length=200, blank=True, null=True)
    details = models.CharField(max_length=200, blank=True, null=True)
    