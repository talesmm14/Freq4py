from django.db import models
from django.conf import settings
import datetime

class Sheet_Title(models.Model):
    name = models.CharField(max_length=250)
    field_title_1 = models.CharField(max_length=30, blank=True, null=True, default="")
    field_title_2 = models.CharField(max_length=30, blank=True, null=True, default="")
    field_title_3 = models.CharField(max_length=30, blank=True, null=True, default="")
    field_title_4 = models.CharField(max_length=30, blank=True, null=True, default="")
    field_title_5 = models.CharField(max_length=30, blank=True, null=True, default="")
    field_title_6 = models.CharField(max_length=30, blank=True, null=True, default="")
    field_title_7 = models.CharField(max_length=30, blank=True, null=True, default="")
    field_title_8 = models.CharField(max_length=30, blank=True, null=True, default="")

    def __str__(self):
        return self.name

class Sheet_Value(models.Model):
    field_value_1 = models.CharField(max_length=100, blank=True, null=True, default="")
    field_value_2 = models.CharField(max_length=100, blank=True, null=True, default="")
    field_value_3 = models.CharField(max_length=100, blank=True, null=True, default="")
    field_value_4 = models.CharField(max_length=100, blank=True, null=True, default="")
    field_value_5 = models.CharField(max_length=100, blank=True, null=True, default="")
    field_value_6 = models.CharField(max_length=100, blank=True, null=True, default="")
    field_value_7 = models.CharField(max_length=100, blank=True, null=True, default="")
    field_value_8 = models.CharField(max_length=100, blank=True, null=True, default="")

    def __str__(self):
        return str(self.field_value_1)

class Schedule(models.Model):
    afternoon_entry_time = models.TimeField(blank=True, null=True)
    afternoon_departure_time = models.TimeField(blank=True, null=True)
    morning_entry_time = models.TimeField(blank=True, null=True)
    morning_departure_time = models.TimeField(blank=True, null=True)

    def key_words(self):
        return {
            "AM1": "",
            "AM2": "",
            "AV1": "",
            "AV2": "",
            "HM1": str(self.morning_entry_time.strftime("%H:%M")),
            "HM2": str(self.morning_departure_time.strftime("%H:%M")),
            "HV1": str(self.afternoon_entry_time.strftime("%H:%M")),
            "HV2": str(self.afternoon_departure_time.strftime("%H:%M")),
        }

class Sheet(models.Model):
    date = models.DateField(default=datetime.date.today)
    titles_fields = models.ForeignKey(Sheet_Title, on_delete=models.CASCADE)
    values_fields = models.ForeignKey(Sheet_Value, on_delete=models.CASCADE, blank=True, null=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    path = "/docs/modelo.docx"
    save_path = "/docs/save_docs/"
 
class Not_Work_Type(models.Model):
    description = models.CharField(max_length=40, verbose_name="Nome")

    def __str__(self):
        return self.description
   
class Not_Working_Day(models.Model):
    sheet = models.ForeignKey(Sheet(), on_delete=models.CASCADE, blank=True, null=True)
    description = models.ForeignKey(Not_Work_Type, on_delete=models.CASCADE)
    day = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.description.description + ' -> ' + str(self.day) + ' : ' + str(self.sheet)