import datetime
import jdatetime
import pytz
from django.conf import settings
from rest_framework import serializers

timezone = pytz.timezone(settings.TIME_ZONE)


class JalaliDateField(serializers.Field):
    date_format = '%Y/%m/%d'

    def to_internal_value(self, data):
        date = jdatetime.datetime.strptime(data, self.date_format).date()
        return date.togregorian()

    def to_representation(self, value):
        return jdatetime.date.fromgregorian(date=value).strftime(self.date_format)


class JalaliDateTimeField(serializers.Field):
    datetime_format = "%Y-%m-%dT%H:%M:%S.%f%z"

    def to_internal_value(self, data):
        date = jdatetime.datetime.strptime(data, self.datetime_format).astimezone(timezone)
        return date.togregorian()

    def to_representation(self, value):
        jalali_datetime = jdatetime.datetime.fromgregorian(datetime=value.astimezone(timezone))
        return jalali_datetime.strftime(self.datetime_format)
