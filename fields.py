import pytz
import jdatetime
from django.conf import settings
from rest_framework.serializers import DateField, DateTimeField, ValidationError

timezone = pytz.timezone(settings.TIME_ZONE)

DATE_FORMAT = '%Y/%m/%d'
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f%z"


class JalaliDateField(DateField):

    datetime_parser = jdatetime.datetime.strptime

    def to_internal_value(self, data):
        try:
            date = jdatetime.datetime.strptime(data, DATE_FORMAT).date()
            return super().to_internal_value(date.togregorian())
        except ValueError:
            raise ValidationError([
                'تاریخ وارد شده نامعتبر است',
                f'باشد {DATE_FORMAT} تاریخ باید در فرمت'
            ])

    def to_representation(self, value):
        jalali_date = jdatetime.date.fromgregorian(date=value)
        return super().to_representation(jalali_date.strftime(DATE_FORMAT))


class JalaliDateTimeField(DateTimeField):

    datetime_parser = jdatetime.datetime.strptime

    def to_internal_value(self, data):
        try:
            date = jdatetime.datetime.strptime(data, DATETIME_FORMAT).astimezone(timezone)
            return super().to_internal_value(date.togregorian())
        except ValueError:
            raise ValidationError([
                'تاریخ و زمان وارد شده نامعتبر میباشد'
                'تاریخ و زمان باید در فرمت ISO 8601 به همراه timezone باشد'
            ])

    def to_representation(self, value):
        jalali_datetime = jdatetime.datetime.fromgregorian(datetime=value.astimezone(timezone))
        return super().to_representation(jalali_datetime.strftime(DATETIME_FORMAT))
