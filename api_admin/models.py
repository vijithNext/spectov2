from django.db import models
from django.db.models.fields.files import ImageField         # package which is used to set working logic and stores in DB               #use to generate token

# ----------===============------------- SPECTO V2 ---------------===============-------------

class Client(models.Model):
    client_id                = models.CharField(unique=True, max_length=50)
    name                     = models.CharField(max_length=255)
    contact_person           = models.CharField(max_length=255,null=True,blank=True)
    email_1                  = models.CharField(max_length=255)
    phone_number_1           = models.CharField(max_length=255,null=True,blank=True)
    secondary_contact_person = models.CharField(max_length=255,null=True,blank=True)
    email_2                  = models.CharField(max_length=255, null=True, blank=True)
    phone_number_2           = models.CharField(max_length=255,null=True,blank=True)
    address                  = models.CharField(max_length=255,null=True,blank=True)
    postal_code              = models.CharField(max_length=255,null=True,blank=True)
    city                     = models.CharField(max_length=255,null=True,blank=True)
    province                 = models.CharField(max_length=255,null=True,blank=True)
    country                  = models.CharField(max_length=255,null=True,blank=True)
    lattitude                = models.CharField(max_length=255,null=True,blank=True)
    longitude                = models.CharField(max_length=255,null=True,blank=True)
    description              = models.TextField(default='',null=True,blank=True)
    selected_id              = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.client_id

class Project(models.Model):
    client_id    = models.ForeignKey(Client, on_delete=models.CASCADE)
    name         = models.CharField(max_length=255)
    project_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Roof(models.Model):
    client_id    = models.ForeignKey(Client, on_delete=models.CASCADE)
    name         = models.CharField(max_length=255)
    project_name = models.CharField(max_length=255, blank=True, null=True)
    field1       = models.CharField(max_length=255,null=True,blank=True)
    field2       = models.CharField(max_length=255,null=True,blank=True)
    field3       = models.CharField(max_length=255,null=True,blank=True)
    images       = models.ImageField(upload_to = 'images_api/roof_img/')

    def __str__(self):
        return self.name

class Room(models.Model):
    client_id    = models.ForeignKey(Client, on_delete=models.CASCADE)
    name         = models.CharField(max_length=255)
    project_name = models.CharField(max_length=255, blank=True, null=True)
    create_room  = models.CharField(max_length=255, blank=True, null=True)
    room_name    = models.CharField(max_length=255, blank=True, null=True)
    add_drawing  = models.ImageField(upload_to = 'images_api/room_img/')
    equipments   = models.CharField(max_length=255,null=True,blank=True)
    wattage      = models.CharField(max_length=255,null=True,blank=True)
    quantity     = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name

class SitePhotos(models.Model):
    client_id                                      = models.ForeignKey(Client, on_delete=models.CASCADE)
    name                                           = models.CharField(max_length=255)
    project_name                                   = models.CharField(max_length=255, blank=True, null=True)
    fount_of_building                              = ImageField(upload_to = 'images_api/front_building/')
    array                                          = ImageField(upload_to = 'images_api/array/')
    meter_close_up                                 = ImageField(upload_to = 'images_api/meter_close_up/')
    proposed_disconnected_location                 = ImageField(upload_to = 'images_api/proposed/')
    south_house                                    = ImageField(upload_to = 'images_api/south_house')
    south_yard                                     = ImageField(upload_to = 'images_api/south_yard')
    electrical_panel_location                      = ImageField(upload_to = 'images_api/electrical_panel')
    electrical_panel_circute_breakers              = ImageField(upload_to = 'images_api/electrical_panel_breakes')
    roof_pitch_proposed_inverter_and_bank_location = ImageField(upload_to = 'images_api/roof_pitch')
    proposed_efficiency_upgrade_location           = ImageField(upload_to = 'images_api/proposed_effiency')

    def __str__(self):
        return self.name

class Add_Equipments_and_working_details(models.Model):
    client_id                              = models.ForeignKey(Client, on_delete=models.CASCADE)
    name                                   = models.CharField(max_length=255)
    project_name                           = models.CharField(max_length=255, blank=True, null=True)
    inverter_mounting_type                 = models.CharField(max_length=255, blank=True, null=True)
    ventilated_room                        = models.CharField(max_length=255, null=True, blank=True)
    dc_cable_run_in_m                      = models.CharField(max_length=255, blank=True, null=True)
    building_CAD_drawings_available        = models.CharField(max_length=255, blank=True, null=True)
    building_electrical_drawings_available = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class Add_Electrical_connection_details(models.Model):
    client_id                                 = models.ForeignKey(Client, on_delete=models.CASCADE)
    name                                      = models.CharField(max_length=255)
    project_name                              = models.CharField(max_length=255, blank=True, null=True)
    Electricity_provider                      = models.CharField(max_length=255, blank=True, null=True)
    sc_no                                     = models.CharField(max_length=255, blank=True, null=True)
    capture_connection_no                     = models.ImageField(upload_to = 'images_api/connection_no/')
    previous_monthly_bills_copy               = models.ImageField(upload_to = 'images_api/mothly_bills/')
    service                                   = models.CharField(max_length=255)
    other_reason                              = models.CharField(max_length=255, blank=True, null=True)
    voltage                                   = models.CharField(max_length=255, blank=True, null=True)
    phase                                     = models.CharField(max_length=255, blank=True, null=True)
    available_breaker_space                   = models.CharField(max_length=255)
    capture_breaker_space_image               = models.ImageField(upload_to = 'images_api/breaker_space_image/')
    Separate_electrical_room_available        = models.CharField(max_length=255)
    capture_electrical_room                   = models.ImageField(upload_to = 'images_api/capture_electrical_room/')
    cable_routing                             = models.CharField(max_length=255)
    capture_connection_number                 = models.ImageField(upload_to = 'images/api/capture_connection_no/')
    roof_to_electrical_room_cable_length_in_m = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Add_Backup_Generator_details(models.Model):
    client_id                    = models.ForeignKey(Client, on_delete=models.CASCADE)
    name                         = models.CharField(max_length=255)
    project_name                 = models.CharField(max_length=255, blank=True, null=True)
    is_backup_generate_available = models.CharField(max_length=255, blank=True, null=True)
    make                         = models.CharField(max_length=255, blank=True, null=True)
    capacity_in_KVA              = models.CharField(max_length=255, null=True, blank=True)
    electrical_phase             = models.CharField(max_length=255, blank=True, null=True)
    auto_start_option_available  = models.CharField(max_length=255, blank=True, null=True)
    daily_operations_hours       = models.CharField(max_length=255, blank=True, null=True)
    change_over_switch_rating    = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class Miscellaneous_Details(models.Model):
    client_id                               = models.ForeignKey(Client, on_delete=models.CASCADE)
    name                                    = models.CharField(max_length=255)
    project_name                            = models.CharField(max_length=255, blank=True, null=True)
    earthing_pit_visibility                 = models.CharField(max_length=255)
    details                                 = models.CharField(max_length=255, blank=True, null=True)
    easy_access_to_roof                     = models.CharField(max_length=255, blank=True, null=True)
    details                                 = models.CharField(max_length=255, blank=True, null=True)
    need_of_scaffoiding_during_installation = models.CharField(max_length=255, blank=True, null=True)
    details                                 = models.CharField(max_length=255, blank=True, null=True)
    available_of_wedding_facility_in_site   = models.CharField(max_length=255, blank=True, null=True)
    details                                 = models.CharField(max_length=255, blank=True, null=True)
    availability_of_crane_service           = models.CharField(max_length=255, blank=True, null=True)
    details                                 = models.CharField(max_length=255, blank=True, null=True)
    availability_of_ladder_facility         = models.CharField(max_length=255, blank=True, null=True)
    details                                 = models.CharField(max_length=255, blank=True, null=True)
    availability_of_building_electricion    = models.CharField(max_length=255, blank=True, null=True)
    details                                 = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.name