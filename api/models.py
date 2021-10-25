from django.db import models
from django.conf import settings

class Sheet_Title(models.Model):
    name = models.CharField(max_length=250)
    field_title_1 = models.CharField(max_length=30, blank=True, null=True)
    field_title_2 = models.CharField(max_length=30, blank=True, null=True)
    field_title_3 = models.CharField(max_length=30, blank=True, null=True)
    field_title_4 = models.CharField(max_length=30, blank=True, null=True)
    field_title_5 = models.CharField(max_length=30, blank=True, null=True)
    field_title_6 = models.CharField(max_length=30, blank=True, null=True)
    field_title_7 = models.CharField(max_length=30, blank=True, null=True)
    field_title_8 = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    # def __dict__(self) -> dict:
    #     return {
    #         "${FIELD_TITLE_1}": self.field_title_1,
    #         "${FIELD_TITLE_2}": self.field_title_2,
    #         "${FIELD_TITLE_3}": self.field_title_3,
    #         "${FIELD_TITLE_4}": self.field_title_4,
    #         "${FIELD_TITLE_5}": self.field_title_5,
    #         "${FIELD_TITLE_6}": self.field_title_6,
    #         "${FIELD_TITLE_7}": self.field_title_7,
    #         "${FIELD_TITLE_8}": self.field_title_8,
    #     }

class Sheet_Value(models.Model):
    date = models.DateField() 
    field_value_1 = models.CharField(max_length=100, blank=True, null=True)
    field_value_2 = models.CharField(max_length=100, blank=True, null=True)
    field_value_3 = models.CharField(max_length=100, blank=True, null=True)
    field_value_4 = models.CharField(max_length=100, blank=True, null=True)
    field_value_5 = models.CharField(max_length=100, blank=True, null=True)
    field_value_6 = models.CharField(max_length=100, blank=True, null=True)
    field_value_7 = models.CharField(max_length=100, blank=True, null=True)
    field_value_8 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.field_value_1 + self.date)

    # def key_words(self):
    #     year = self.date.year
    #     month = self.date.month
    #     return {
    #         "${FIELD_DATE}": (datetime.date(year, month, 1).strftime('%B')).swapcase() + "/" + str(year),
    #         "${FIELD_VALUE_1}": self.field_value_1,
    #         "${FIELD_VALUE_2}": self.field_value_2,
    #         "${FIELD_VALUE_3}": self.field_value_3,
    #         "${FIELD_VALUE_4}": self.field_value_4,
    #         "${FIELD_VALUE_5}": self.field_value_5,
    #         "${FIELD_VALUE_6}": self.field_value_6,
    #         "${FIELD_VALUE_7}": self.field_value_7,
    #         "${FIELD_VALUE_8}": self.field_value_8,
    #     }

class Not_Working_Day(models.Model):
    description = models.CharField(max_length=40, verbose_name="Descrição")
    day = models.IntegerField(blank=False, null=False)

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
            "HM1": self.morning_entry_time,
            "HM2": self.morning_departure_time,
            "HV1": self.afternoon_entry_time,
            "HV2": self.afternoon_departure_time,
        }

class Sheet(models.Model):
    not_working_days = models.ForeignKey(Not_Working_Day(), on_delete=models.CASCADE, blank=True, null=True)
    titles_fields = models.ForeignKey(Sheet_Title, on_delete=models.CASCADE)
    values_fields = models.ForeignKey(Sheet_Value, on_delete=models.CASCADE, blank=True, null=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    path = "/docs/modelo.docx"
    save_path = "/docs/save_docs/"
    