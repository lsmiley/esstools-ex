from django.db import models


class Configmaster(models.Model):
    created = models.DateTimeField(db_column='Created:')
    configmastermodifydate = models.DateTimeField(db_column='Modify Date:')
    configmastername = models.CharField(
        db_column='Name:', max_length=150, blank=True, null=True)
    configmasterdesc = models.CharField(
        db_column='Description:',
        max_length=150,
        blank=True,
        null=True)
    configmasternotes = models.CharField(
        db_column='Notes:', max_length=150, blank=True, null=True)

    def __str__(self):
        return self.configmastername
