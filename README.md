# تبدیل تاریخ میلادی به شمسی در Django Rest Framework
این ریپو شامل 2 تا Field کاستوم برای Serializer ها در DRF می باشد تا تاریخ ها به صورت میلادی با ناحیه زمانی UTC در دیتابیس ذخیره شده و هنگام نمایش یا همان represent کردن, تاریخ ها به صورت شمسی و با ناحیه زمانی Asia/Tehran نمایش داده شوند.

## دپندنسی های استفاده شده
برای این پروژه از پکیج [jdatetime](https://pypi.org/project/jdatetime/) استفاده شده است

## نحوه استفاده:
jdatetime را نصب کنید:
```shell
pip install jdatetime
```
تنظیمات زیر را به فایل settings.py اضافه کنید:
```python
TIME_ZONE = 'Asia/Tehran'

USE_TZ = True
```
### مثال:
```python

class Model(serializers.ModelSerializer):
    date = JalaliDateField()
    created = JalaliDateTimeField()

    class Meta:
        model = Model
        fields = ['id', 'date', 'created']

```
