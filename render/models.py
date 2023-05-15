from django.db import models

# Create your models here.
class WeatherReport(models.Model):
    Reporting_Time = models.DateTimeField()
    Reported_Weather_Type = models.TextField()
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = '"public"."Weather_Report"'
       
class WeatherInfo(models.Model):
    Day = models.TextField()
    Weather_Type = models.TextField()
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = '"public"."Weather_Info"'

class CropSeeding(models.Model):
    Crop_Name = models.TextField()
    Seeding_Day = models.TextField()
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = '"public"."Crop_Seeding"'        