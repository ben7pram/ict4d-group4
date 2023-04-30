from django.db import models

# Create your models here.
class WeatherReport(models.Model):
    Reporting_Time = models.DateTimeField()
    Reported_Weather_Type = models.TextField()

    class Meta:
        managed = False
        db_table = '"public"."Weather_Report"'
        #db_table = "Weather_Report"
