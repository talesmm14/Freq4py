from django.db import models
import datetime

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class SheetTitle(models.Model):
    name = models.CharField(max_length=250)
    field_title_1 = models.CharField(
        max_length=30, blank=True, null=True, default="")
    field_title_2 = models.CharField(
        max_length=30, blank=True, null=True, default="")
    field_title_3 = models.CharField(
        max_length=30, blank=True, null=True, default="")
    field_title_4 = models.CharField(
        max_length=30, blank=True, null=True, default="")
    field_title_5 = models.CharField(
        max_length=30, blank=True, null=True, default="")
    field_title_6 = models.CharField(
        max_length=30, blank=True, null=True, default="")
    field_title_7 = models.CharField(
        max_length=30, blank=True, null=True, default="")
    field_title_8 = models.CharField(
        max_length=30, blank=True, null=True, default="")

    def __str__(self):
        return self.name


class SheetValue(models.Model):
    field_value_1 = models.CharField(
        max_length=100, blank=True, null=True, default="")
    field_value_2 = models.CharField(
        max_length=100, blank=True, null=True, default="")
    field_value_3 = models.CharField(
        max_length=100, blank=True, null=True, default="")
    field_value_4 = models.CharField(
        max_length=100, blank=True, null=True, default="")
    field_value_5 = models.CharField(
        max_length=100, blank=True, null=True, default="")
    field_value_6 = models.CharField(
        max_length=100, blank=True, null=True, default="")
    field_value_7 = models.CharField(
        max_length=100, blank=True, null=True, default="")
    field_value_8 = models.CharField(
        max_length=100, blank=True, null=True, default="")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.field_value_1)


class Schedule(models.Model):
    afternoon_entry_time = models.TimeField(blank=True, null=True)
    afternoon_departure_time = models.TimeField(blank=True, null=True)
    morning_entry_time = models.TimeField(blank=True, null=True)
    morning_departure_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return (str(self.morning_entry_time.strftime("%H:%M")) + " -> " +
                str(self.morning_departure_time.strftime("%H:%M")) + " : " +
                str(self.afternoon_entry_time.strftime("%H:%M")) + " -> " +
                str(self.afternoon_departure_time.strftime("%H:%M")))

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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    titles_fields = models.ForeignKey(SheetTitle, on_delete=models.CASCADE)
    values_fields = models.ForeignKey(
        SheetValue, on_delete=models.CASCADE, blank=True, null=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    path = "/docs/modelo.docx"
    save_path = "/docs/save_docs/"
    img_path = models.ImageField(upload_to="img_sheet", height_field=2.67,
                                 width_field=6.94, max_length=100, blank=True, null=True)
    title = models.CharField(blank=True, null=True, max_length=250)

    def __str__(self):
        if self.title:
            return self.title + ' : ' + str(self.date) + ' > ' + str(self.schedule)
        elif self.values_fields:
            return self.values_fields.field_value_1 + ' : ' + str(self.date) + ' > ' + str(self.schedule)
        return str(self.date) + ' : ' + str(self.schedule)


class NotWorkType(models.Model):
    description = models.CharField(max_length=40, verbose_name="Nome")

    def __str__(self):
        return self.description


class NotWorkingDay(models.Model):
    sheet = models.ForeignKey(
        Sheet(), on_delete=models.CASCADE, blank=True, null=True)
    description = models.ForeignKey(NotWorkType, on_delete=models.CASCADE)
    day = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.description.description + ' -> ' + str(self.day) + ' : ' + str(self.sheet)
