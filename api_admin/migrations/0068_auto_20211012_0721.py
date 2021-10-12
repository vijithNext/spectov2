# Generated by Django 3.0.7 on 2021-10-12 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_admin', '0067_auto_20211012_0458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='images',
            new_name='add_drawing',
        ),
        migrations.RemoveField(
            model_name='roof',
            name='project',
        ),
        migrations.AddField(
            model_name='add_backup_generator_details',
            name='project_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='add_electrical_connection_details',
            name='project_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='add_equipments_and_working_details',
            name='project_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='miscellaneous_details',
            name='project_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='roof',
            name='project_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='project_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='room_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sitephotos',
            name='project_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='add_backup_generator_details',
            name='auto_start_option_available',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='add_backup_generator_details',
            name='electrical_phase',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='add_backup_generator_details',
            name='is_backup_generate_available',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='add_backup_generator_details',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='add_electrical_connection_details',
            name='Electricity_provider',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='add_electrical_connection_details',
            name='Separate_electrical_room_available',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='add_electrical_connection_details',
            name='available_breaker_space',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='add_electrical_connection_details',
            name='cable_routing',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='add_electrical_connection_details',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='add_electrical_connection_details',
            name='other_reason',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='add_electrical_connection_details',
            name='phase',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='add_electrical_connection_details',
            name='sc_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='add_electrical_connection_details',
            name='service',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='add_electrical_connection_details',
            name='voltage',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='add_equipments_and_working_details',
            name='building_CAD_drawings_available',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='add_equipments_and_working_details',
            name='building_electrical_drawings_available',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='add_equipments_and_working_details',
            name='dc_cable_run_in_m',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='add_equipments_and_working_details',
            name='inverter_mounting_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='add_equipments_and_working_details',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='add_equipments_and_working_details',
            name='ventilated_room',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='miscellaneous_details',
            name='availability_of_building_electricion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='miscellaneous_details',
            name='availability_of_crane_service',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='miscellaneous_details',
            name='availability_of_ladder_facility',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='miscellaneous_details',
            name='available_of_wedding_facility_in_site',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='miscellaneous_details',
            name='details',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='miscellaneous_details',
            name='earthing_pit_visibility',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='miscellaneous_details',
            name='easy_access_to_roof',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='miscellaneous_details',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='miscellaneous_details',
            name='need_of_scaffoiding_during_installation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='roof',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='room',
            name='create_room',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='equipments',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='room',
            name='quantity',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='wattage',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sitephotos',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]