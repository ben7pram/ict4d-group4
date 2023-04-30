from django.db import models

# Create your models here.
class WeatherReport(models.Model):
    Reporting_Time = models.DateTimeField()
    Reported_Weather_Type = models.TextField()
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = '"public"."Weather_Report"'
        #db_table = "Weather_Report"
