from django.db import models

from configmaster.models import *


class Configtable(models.Model):
    configmaster = models.ForeignKey(Configmaster, on_delete=models.DO_NOTHING)
    configcreatedate = models.DateTimeField(db_column='ConfigCreateDate')
    configmodifydate = models.DateTimeField(db_column='ConfigModifyDate')
    configname = models.CharField(
        db_column='ConfigName',
        max_length=150,
        blank=True,
        null=True)
    configdesc = models.CharField(
        db_column='ConfigDesc',
        max_length=150,
        blank=True,
        null=True)
    configtype = models.CharField(
        db_column='ConfigType',
        max_length=150,
        blank=True,
        null=True)
    confignotes = models.CharField(
        db_column='ConfigNotes',
        max_length=150,
        blank=True,
        null=True)
    confignummber = models.FloatField(db_column='ConfigNummber')
    configtext = models.FloatField(db_column='ConfigText')
    configlink = models.CharField(
        db_column='ConfigLink',
        max_length=150,
        blank=True,
        null=True)
    sizemodifier = models.FloatField(db_column='SizeModifier', default='1.0')
    vendormodifier = models.FloatField(
        db_column='VendorModifier', default='1.0')
    hoursmodifier = models.FloatField(db_column='HoursModifier', default='1.0')
    managementmodifier1stline = models.FloatField(
        db_column='ManagementModifier1stLine', default='1.0')
    managementmodifier2ndline = models.FloatField(
        db_column='ManagementModifier2ndLine', default='1.0')
    riskfactor_low = models.FloatField(
        db_column='RiskFactor_Low', default='1.0')
    riskfactor_med = models.FloatField(
        db_column='RiskFactor_Med', default='1.0')
    riskfactor_high = models.FloatField(
        db_column='RiskFactor_High', default='1.0')
    othercost_education = models.FloatField(db_column='OtherCost_Education',
                                            default='0.0')
    othercost_travel = models.FloatField(
        db_column='OtherCost_Travel', default='0.0')
    othercost_equipment = models.FloatField(db_column='OtherCost_Equipment',
                                            default='0.0')
    endpointrangemodifier1 = models.FloatField(
        db_column='EndpointRangeModifier1', default='1.0')
    endpointrangemodifier2 = models.FloatField(
        db_column='EndpointRangeModifier2', default='1.0')
    endpointrangemodifier3 = models.FloatField(
        db_column='EndpointRangeModifier3', default='1.0')
    endpointrangemodifier4 = models.FloatField(
        db_column='EndpointRangeModifier4', default='1.0')
    endpointrangemodifier5 = models.FloatField(
        db_column='EndpointRangeModifier5', default='1.0')
    endpointrangemodifier6 = models.FloatField(
        db_column='EndpointRangeModifier6', default='1.0')
    rpt_biweeklymodifier = models.FloatField(db_column='Rpt_BiWeeklyModifier',
                                             default='1.0')
    rpt_weeklymodifier = models.FloatField(
        db_column='Rpt_WeeklyModifier', default='1.0')
    rpt_dailymodifier = models.FloatField(
        db_column='Rpt_DailyModifier', default='1.0')
    rpt_custommodifier = models.FloatField(
        db_column='Rpt_CustomModifier', default='1.0')
    defaultendpointfac = models.FloatField(
        db_column='DefaultEndpointFac', default='1.0')
    fac_frachrs = models.FloatField(db_column='Fac_FracHrs', default='0.0365')
    fac_adjwkstn = models.FloatField(
        db_column='Fac_AdjWkstn', default='0.0365')
    fac_adjsvrs = models.FloatField(db_column='Fac_AdjSvrs', default='0.0365')
    fac_adjips = models.FloatField(db_column='Fac_AdjIPs', default='0.0365')
    fac_svrcalc = models.FloatField(db_column='Fac_SvrCalc', default='0.0365')
    frm_componentfac1 = models.FloatField(
        db_column='Frm_ComponentFac1', default='1.0')
    frm_componentfac2 = models.FloatField(
        db_column='Frm_ComponentFac2', default='1.0')
    frm_componentfac3 = models.FloatField(
        db_column='Frm_ComponentFac3', default='1.0')
    frm_componentfac4 = models.FloatField(
        db_column='Frm_ComponentFac4', default='1.0')
    frm_componentfac5 = models.FloatField(
        db_column='Frm_ComponentFac5', default='1.0')
    frm_componentfac6 = models.FloatField(
        db_column='Frm_ComponentFac6', default='1.0')
    frm_componentfac7 = models.FloatField(
        db_column='Frm_ComponentFac7', default='1.0')
    frm_componentfac8 = models.FloatField(
        db_column='Frm_ComponentFac8', default='1.0')
    frm_componentfac9 = models.FloatField(
        db_column='Frm_ComponentFac9', default='1.0')
    frm_componentfac10 = models.FloatField(
        db_column='Frm_ComponentFac10', default='1.0')
    frm_componentfac11 = models.FloatField(
        db_column='Frm_ComponentFac11', default='1.0')
    frm_componentfac12 = models.FloatField(
        db_column='Frm_ComponentFac12', default='1.0')

    def __str__(self):
        return self.configname
