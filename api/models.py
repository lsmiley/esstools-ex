from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    numworkstation = models.IntegerField(
        db_column='Numworkstation', default='0')
    numserver = models.IntegerField(db_column='Numserver', default='0')
    addlconsole = models.IntegerField(db_column='addlconsole', default='0')
    productcomplexitybase = models.FloatField(
        db_column='ProductComplexityBase', default='550')
    productcomplexityfac = models.FloatField(
        db_column='ProductComplexityFac', default='1.0')

    def __str__(self):
        return self.title
