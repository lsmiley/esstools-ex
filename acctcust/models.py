from django.db import models


class Acctcust(models.Model):
    acctname = models.CharField(
        db_column='AcctName',
        max_length=75,
        blank=True,
        null=True)
    businesssec = models.CharField(
        db_column='BusinessSec',
        max_length=75,
        blank=True,
        null=True)
    regulatory = models.CharField(
        db_column='Regulatory',
        max_length=75,
        blank=True,
        null=True)
    created = models.CharField(db_column='Created', max_length=75)
    address1 = models.CharField(
        db_column='Address1',
        max_length=75,
        blank=True,
        null=True)
    address2 = models.CharField(
        db_column='Address2',
        max_length=75,
        blank=True,
        null=True)
    city = models.CharField(
        db_column='City',
        max_length=75,
        blank=True,
        null=True)
    state = models.CharField(
        db_column='State',
        max_length=75,
        blank=True,
        null=True)
    country = models.CharField(
        db_column='Country',
        max_length=75,
        blank=True,
        null=True)
    contact1name = models.CharField(
        db_column='Contact1Name',
        max_length=75,
        blank=True,
        null=True)
    contact1phone = models.CharField(
        db_column='Contact1Phone',
        max_length=75,
        blank=True,
        null=True)
    contact1email = models.CharField(
        db_column='Contact1Email',
        max_length=75,
        blank=True,
        null=True)
    contact2name = models.CharField(
        db_column='Contact2Name',
        max_length=75,
        blank=True,
        null=True)
    contact2phone = models.CharField(
        db_column='Contact2Phone',
        max_length=75,
        blank=True,
        null=True)
    contact2email = models.CharField(
        db_column='Contact2Email',
        max_length=75,
        blank=True,
        null=True)
    wbsiteurl = models.CharField(
        db_column='WbSiteURL',
        max_length=75,
        blank=True,
        null=True)
    createdby = models.CharField(
        db_column='CreatedBy',
        max_length=75,
        blank=True,
        null=True)
    modifydate = models.CharField(
        db_column='ModifyDate',
        max_length=75,
        blank=True,
        null=True)  # Field name made lowercase

    def __str__(self):
        return self.acctname

    class Meta:
        ordering = ('acctname',)


