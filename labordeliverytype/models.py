from django.db import models


class Labordeliverytype(models.Model):
    deliverytypename = models.CharField(
        db_column='DeliveryTypeName',
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
        return self.deliverytypename
