from django.db import models


class Statusstate(models.Model):
    statusstatename = models.CharField(
        db_column='StatusStateName',
        max_length=150,
        blank=True,
        null=True)
    statusstatedesc = models.CharField(
        db_column='StatusStateDesc',
        max_length=150,
        blank=True,
        null=True)
    statusstatetype = models.CharField(
        db_column='StatusStateType',
        max_length=150,
        blank=True,
        null=True)
    memo = models.CharField(
        db_column='Memo',
        max_length=150,
        blank=True,
        null=True)

    def __str__(self):
        return self.statusstatename

