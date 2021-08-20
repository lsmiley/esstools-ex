from django.db import models
from labordeliverytype.models import *


class Labordelivery(models.Model):
    labordeliverytype = models.ForeignKey(
        Labordeliverytype,
        on_delete=models.DO_NOTHING)
    regionnumber = models.IntegerField(db_column='RegionNumber')
    regions = models.CharField(
        db_column='Regions',
        max_length=150,
        blank=True,
        null=True)
    deliveryoption = models.CharField(
        db_column='DeliveryOption',
        max_length=150,
        blank=True,
        null=True)

    currencytype = models.CharField(
        db_column='CurrencyType',
        max_length=150,
        blank=True,
        null=True)
    defaultfte_year = models.FloatField(
        db_column='DefaultFTE_Year', default='1795.0')
    workweek = models.FloatField(db_column='WorkWeek', default='40.0')
    deliveryctrcostfactor = models.FloatField(
        db_column='DeliveryCtrCostFactor', default='1.0')
    band2 = models.FloatField(db_column='Band2', default='0.0')
    band2name = models.CharField(
        db_column='Band2Name',
        max_length=150,
        blank=True,
        null=True, default='Band #2')
    band2count = models.FloatField(db_column='Band2Count', default='0.0')
    band2percentage = models.FloatField(
        db_column='Band2Percentage', default='0.0')
    band3 = models.FloatField(db_column='Band3', default='0.0')
    band3name = models.CharField(
        db_column='Band3Name',
        max_length=150,
        blank=True,
        null=True, default='Band #3')
    band3count = models.FloatField(db_column='Band3Count', default='0.0')
    band3percentage = models.FloatField(
        db_column='Band3Percentage', default='0.0')
    band4 = models.FloatField(db_column='Band4', default='0.0')
    band4name = models.CharField(
        db_column='Band4Name',
        max_length=150,
        blank=True,
        null=True, default='Band #4')
    band4count = models.FloatField(db_column='Band4Count', default='0.0')
    band4percentage = models.FloatField(
        db_column='Band4Percentage', default='0.0')
    band5 = models.FloatField(db_column='Band5', default='0.0')
    band5name = models.CharField(
        db_column='Band5Name',
        max_length=150,
        blank=True,
        null=True, default='Band #5')
    band5count = models.FloatField(db_column='Band5Count', default='0.0')
    band5percentage = models.FloatField(
        db_column='Band5Percentage', default='0.0')
    band6 = models.FloatField(db_column='Band6', default='0.0')
    band6name = models.CharField(
        db_column='Band6Name',
        max_length=150,
        blank=True,
        null=True, default='Band #6')
    band6count = models.FloatField(db_column='Band6Count', default='0.0')
    band6percentage = models.FloatField(
        db_column='Band6Percentage', default='0.0')
    band7 = models.FloatField(db_column='Band7', default='0.0')
    band7name = models.CharField(
        db_column='Band7Name',
        max_length=150,
        blank=True,
        null=True, default='Band #7')
    band7count = models.FloatField(db_column='Band7Count', default='0.0')
    band7percentage = models.FloatField(
        db_column='Band7Percentage', default='0.0')
    band8 = models.FloatField(db_column='Band8', default='0.0')
    band8name = models.CharField(
        db_column='Band8Name',
        max_length=150,
        blank=True,
        null=True, default='Band #8')
    band8count = models.FloatField(db_column='Band8Count', default='0.0')
    band8percentage = models.FloatField(
        db_column='Band8Percentage', default='0.0')
    band9 = models.FloatField(db_column='Band9', default='0.0')
    band9name = models.CharField(
        db_column='Band9Name',
        max_length=150,
        blank=True,
        null=True, default='Band #9')
    band9count = models.FloatField(db_column='Band9Count', default='0.0')
    band9percentage = models.FloatField(
        db_column='Band9Percentage', default='0.0')
    band10 = models.FloatField(db_column='Band10', default='0.0')
    band10name = models.CharField(
        db_column='Band10Name',
        max_length=150,
        blank=True,
        null=True, default='Band #10')
    band10count = models.FloatField(db_column='Band10Count', default='0.0')
    band10percentage = models.FloatField(
        db_column='Band10Percentage', default='0.0')
    bandstotalcount = models.FloatField(
        db_column='BandsTotalCount', default='0.0')
    deliverytype = models.CharField(
        db_column='DeliveryType',
        max_length=150,
        blank=True,
        null=True)
    deliveryusedescription = models.CharField(
        db_column='DeliveryUseDescription',
        max_length=150,
        blank=True,
        null=True)
    memodeliverynote1 = models.CharField(
        db_column='MemoDeliveryNote1',
        max_length=150,
        blank=True,
        null=True)
    deliveryownerfirstname = models.CharField(
        db_column='DeliveryOwnerFirstName',
        max_length=150,
        blank=True,
        null=True)
    deliveryownerlastname = models.CharField(
        db_column='DeliveryOwnerLastName',
        max_length=150,
        blank=True,
        null=True)
    deliveryownerfullname = models.CharField(
        db_column='DeliveryOwnerFullName',
        max_length=150,
        blank=True,
        null=True)
    deliveryowneremail = models.CharField(
        db_column='DeliveryOwnerEmail',
        max_length=150,
        blank=True,
        null=True)
    createby = models.CharField(
        db_column='CreateBy',
        max_length=150,
        blank=True,
        null=True)

    def __str__(self):
        return self.regions