# Generated by Django 4.0 on 2021-12-08 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tntworksheet',
            fields=[
                ('tntid', models.BigAutoField(db_column='TnTId', primary_key=True, serialize=False)),
                ('tntdescription', models.CharField(blank=True, max_length=150, null=True)),
                ('managementmod1stline', models.FloatField(default='0.0')),
                ('managementmod2ndline', models.FloatField(default='0.0')),
                ('totaltransitiontotalfte', models.FloatField(default='0.0')),
                ('totaltransitiontotalhours', models.FloatField(default='0.0')),
                ('totaltransitiontotalband8', models.FloatField(default='0.0')),
                ('totaltransitiontotal1stlinemgr', models.FloatField(default='0.0')),
                ('totaltransitiontotal2ndlinemgr', models.FloatField(default='0.0')),
                ('totaltransitiontotals', models.FloatField(default='0.0')),
                ('totaltransformationtotalfte', models.FloatField(default='0.0')),
                ('totaltransformationtotalhours', models.FloatField(default='0.0')),
                ('totaltransformationtotalband8', models.FloatField(default='0.0')),
                ('totaltransformationtotal1stlinemgr', models.FloatField(default='0.0')),
                ('totaltransformationtotal2ndlinemgr', models.FloatField(default='0.0')),
                ('totaltransformationtotals', models.FloatField(default='0.0')),
                ('transitionhoursfte', models.FloatField(default='0.0')),
                ('transitionfirstlinemanagementband8', models.FloatField(default='0.0')),
                ('transitionsecondlinemanagementband8', models.FloatField(default='0.0')),
                ('transitionfirstlinemanagementband8weeks', models.FloatField(default='0.0')),
                ('transitionsecondlinemanagementband8weeks', models.FloatField(default='0.0')),
                ('transitionsubtotalshours', models.FloatField(default='0.0')),
                ('transitionfirstlinemanagementband8hours', models.FloatField(default='0.0')),
                ('transfortionhoursfte', models.FloatField(default='0.0')),
                ('transformationfirstlinemanagementband8', models.FloatField(default='0.0')),
                ('transformationsecondlinemanagementband8', models.FloatField(default='0.0')),
                ('transformationfirstlinemanagementband8weeks', models.FloatField(default='0.0')),
                ('transformationsecondlinemanagementband8weeks', models.FloatField(default='0.0')),
                ('tranformationsubtotalshours', models.FloatField(default='0.0')),
                ('transformationfirstlinemanagementband8hours', models.FloatField(default='0.0')),
                ('transitionsubtotalshoursitems', models.FloatField(default='0.0')),
                ('transformationsubtotalshoursitems', models.FloatField(default='0.0')),
                ('executetransitionplan_count', models.FloatField(default='1.0')),
                ('executetransitionplan_transitionhoursitem', models.FloatField(default='0.0')),
                ('executetransitionplan_transitionhours', models.FloatField(default='0.0')),
                ('executetransitionplan_transformationhoursitem', models.FloatField(default='250.0')),
                ('executetransitionplan_transformationhours', models.FloatField(default='250.0')),
                ('createbestpracticecustom_count', models.FloatField(default='1.0')),
                ('createbestpracticecustom_transitionhoursitem', models.FloatField(default='40.0')),
                ('createbestpracticecustom_transitionhours', models.FloatField(default='40.0')),
                ('createbestpracticecustom_transformationhoursitem', models.FloatField(default='33.0')),
                ('createbestpracticecustom_transformationhours', models.FloatField(default='33.0')),
                ('testinfrastructurepoc_count', models.FloatField(default='1.0')),
                ('testinfrastructurepoc_transitionhoursitem', models.FloatField(default='40.0')),
                ('testinfrastructurepoc_transitionhours', models.FloatField(default='40.0')),
                ('testinfrastructurepoc_transformationhoursitem', models.FloatField(default='33.0')),
                ('testinfrastructurepoc_transformationhours', models.FloatField(default='33.0')),
                ('troubleshoottune_count', models.FloatField(default='1.0')),
                ('troubleshoottune_transitionhoursitem', models.FloatField(default='40.0')),
                ('troubleshoottune_transitionhours', models.FloatField(default='40.0')),
                ('troubleshoottune_transformationhoursitem', models.FloatField(default='33.0')),
                ('troubleshoottune_transformationhours', models.FloatField(default='33.0')),
                ('installconfigure_count', models.FloatField(default='1.0')),
                ('installconfigure_transitionhoursitem', models.FloatField(default='40.0')),
                ('installconfigure_transitionhours', models.FloatField(default='40.0')),
                ('installconfigure_transformationhoursitem', models.FloatField(default='33.0')),
                ('installconfigure_transformationhours', models.FloatField(default='33.0')),
                ('administratortraining_count', models.FloatField(default='1.0')),
                ('administratortraining_transitionhoursitem', models.FloatField(default='20.0')),
                ('administratortraining_transitionhours', models.FloatField(default='20.0')),
                ('administratortraining_transformationhoursitem', models.FloatField(default='17.0')),
                ('administratortraining_transformationhours', models.FloatField(default='17.0')),
                ('developserviceresponsibilitymatrix_count', models.FloatField(default='1.0')),
                ('developserviceresponsibilitymatrix_transitionhoursitem', models.FloatField(default='16.0')),
                ('developserviceresponsibilitymatrix_transitionhours', models.FloatField(default='16.0')),
                ('developserviceresponsibilitymatrix_transformationhoursitem', models.FloatField(default='13.0')),
                ('developserviceresponsibilitymatrix_transformationhours', models.FloatField(default='13.0')),
                ('establishanyneededserviceaccounts_count', models.FloatField(default='1.0')),
                ('establishanyneededserviceaccounts_transitionhoursitem', models.FloatField(default='16.0')),
                ('establishanyneededserviceaccounts_transitionhours', models.FloatField(default='16.0')),
                ('establishanyneededserviceaccounts_transformationhoursitem', models.FloatField(default='13.0')),
                ('establishanyneededserviceaccounts_transformationhours', models.FloatField(default='13.0')),
                ('researchandsetupemailautomation_count', models.FloatField(default='1.0')),
                ('researchandsetupemailautomation_transitionhoursitem', models.FloatField(default='16.0')),
                ('researchandsetupemailautomation_transitionhours', models.FloatField(default='16.0')),
                ('researchandsetupemailautomation_transformationhoursitem', models.FloatField(default='13.0')),
                ('researchandsetupemailautomation_transformationhours', models.FloatField(default='13.0')),
                ('installconfigureremoteconsoles_count', models.FloatField(default='1.0')),
                ('installconfigureremoteconsoles_transitionhoursitem', models.FloatField(default='16.0')),
                ('installconfigureremoteconsoles_transitionhours', models.FloatField(default='16.0')),
                ('installconfigureremoteconsoles_transformationhoursitem', models.FloatField(default='13.0')),
                ('installconfigureremoteconsoles_transformationhours', models.FloatField(default='13.0')),
                ('workwithsecops_count', models.FloatField(default='1.0')),
                ('workwithsecops_transitionhoursitem', models.FloatField(default='16.0')),
                ('workwithsecops_transitionhours', models.FloatField(default='16.0')),
                ('workwithsecops_transformationhoursitem', models.FloatField(default='13.0')),
                ('workwithsecops_transformationhours', models.FloatField(default='13.0')),
                ('staffingccoordinating_count', models.FloatField(default='1.0')),
                ('staffingccoordinating_transitionhoursitem', models.FloatField(default='10.0')),
                ('staffingccoordinating_transitionhours', models.FloatField(default='10.0')),
                ('staffingccoordinating_transformationhoursitem', models.FloatField(default='8.0')),
                ('staffingccoordinating_transformationhours', models.FloatField(default='8.0')),
                ('identifytestdocument_count', models.FloatField(default='1.0')),
                ('identifytestdocument_transitionhoursitem', models.FloatField(default='10.0')),
                ('identifytestdocument_transitionhours', models.FloatField(default='10.0')),
                ('identifytestdocument_transformationhoursitem', models.FloatField(default='8.0')),
                ('identifytestdocument_transformationhours', models.FloatField(default='8.0')),
                ('obtainnetworkandosaccesswave1_count', models.FloatField(default='1.0')),
                ('obtainnetworkandosaccesswave1_transitionhoursitem', models.FloatField(default='10.0')),
                ('obtainnetworkandosaccesswave1_transitionhours', models.FloatField(default='10.0')),
                ('obtainnetworkandosaccesswave1_transformationhoursitem', models.FloatField(default='8.0')),
                ('obtainnetworkandosaccesswave1_transformationhours', models.FloatField(default='8.0')),
                ('obtainnetworkandosaccesswave2_count', models.FloatField(default='1.0')),
                ('obtainnetworkandosaccesswave2_transitionhoursitem', models.FloatField(default='10.0')),
                ('obtainnetworkandosaccesswave2_transitionhours', models.FloatField(default='10.0')),
                ('obtainnetworkandosaccesswave2_transformationhoursitem', models.FloatField(default='8.0')),
                ('obtainnetworkandosaccesswave2_transformationhours', models.FloatField(default='8.0')),
                ('developprovideagentsoftware_count', models.FloatField(default='1.0')),
                ('developprovideagentsoftware_transitionhoursitem', models.FloatField(default='10.0')),
                ('developprovideagentsoftware_transitionhours', models.FloatField(default='10.0')),
                ('developprovideagentsoftware_transformationhoursitem', models.FloatField(default='8.0')),
                ('developprovideagentsoftware_transformationhours', models.FloatField(default='8.0')),
                ('installconfigureodbc_count', models.FloatField(default='1.0')),
                ('installconfigureodbc_transitionhoursitem', models.FloatField(default='10.0')),
                ('installconfigureodbc_transitionhours', models.FloatField(default='10.0')),
                ('installconfigureodbc_transformationhoursitem', models.FloatField(default='8.0')),
                ('installconfigureodbc_transformationhours', models.FloatField(default='8.0')),
                ('customerreviewsignoff_count', models.FloatField(default='1.0')),
                ('customerreviewsignoff_transitionhoursitem', models.FloatField(default='10.0')),
                ('customerreviewsignoff_transitionhours', models.FloatField(default='10.0')),
                ('customerreviewsignoff_transformationhoursitem', models.FloatField(default='8.0')),
                ('customerreviewsignoff_transformationhours', models.FloatField(default='8.0')),
                ('establishhealthcheck_count', models.FloatField(default='1.0')),
                ('establishhealthcheck_transitionhoursitem', models.FloatField(default='10.0')),
                ('establishhealthcheck_transitionhours', models.FloatField(default='10.0')),
                ('establishhealthcheck_transformationhoursitem', models.FloatField(default='8.0')),
                ('establishhealthcheck_transformationhours', models.FloatField(default='8.0')),
                ('developworkflows_count', models.FloatField(default='1.0')),
                ('developworkflows_transitionhoursitem', models.FloatField(default='10.0')),
                ('developworkflows_transitionhours', models.FloatField(default='10.0')),
                ('developworkflows_transformationhoursitem', models.FloatField(default='8.0')),
                ('developworkflows_transformationhours', models.FloatField(default='8.0')),
                ('operationaldocumentation_count', models.FloatField(default='1.0')),
                ('operationaldocumentation_transitionhoursitem', models.FloatField(default='10.0')),
                ('operationaldocumentation_transitionhours', models.FloatField(default='10.0')),
                ('operationaldocumentation_transformationhoursitem', models.FloatField(default='8.0')),
                ('operationaldocumentation_transformationhours', models.FloatField(default='8.0')),
                ('shadowestablishreviewallprocedures_count', models.FloatField(default='1.0')),
                ('shadowestablishreviewallprocedures_transitionhoursitem', models.FloatField(default='60.0')),
                ('shadowestablishreviewallprocedures_transitionhours', models.FloatField(default='60.0')),
                ('shadowestablishreviewallprocedures_transformationhoursitem', models.FloatField(default='50.0')),
                ('shadowestablishreviewallprocedures_transformationhours', models.FloatField(default='50.0')),
                ('otherdetail_count', models.FloatField(default='1.0')),
                ('otherdetail_transitionhoursitem', models.FloatField(default='249.0')),
                ('otherdetail_transitionhours', models.FloatField(default='249.0')),
                ('otherdetail_transformationhoursitem', models.FloatField(default='208.0')),
                ('otherdetail_transformationhours', models.FloatField(default='208.0')),
                ('specialitem1_count', models.FloatField(default='.01')),
                ('specialitem1_transitionhoursitem', models.FloatField(default='.01')),
                ('specialitem1_transitionhours', models.FloatField(default='.0001')),
                ('specialitem1_transformationhoursitem', models.FloatField(default='.01')),
                ('specialitem1_transformationhours', models.FloatField(default='.0001')),
                ('specialitem2_count', models.FloatField(default='.01')),
                ('specialitem2_transitionhoursitem', models.FloatField(default='.01')),
                ('specialitem2_transitionhours', models.FloatField(default='.0001')),
                ('specialitem2_transformationhoursitem', models.FloatField(default='.01')),
                ('specialitem2_transformationhours', models.FloatField(default='.0001')),
                ('specialitem3_count', models.FloatField(default='.01')),
                ('specialitem3_transitionhoursitem', models.FloatField(default='.01')),
                ('specialitem3_transitionhours', models.FloatField(default='.0001')),
                ('specialitem3_transformationhoursitem', models.FloatField(default='.01')),
                ('specialitem3_transformationhours', models.FloatField(default='.0001')),
                ('specialitem4_count', models.FloatField(default='.01')),
                ('specialitem4_transitionhoursitem', models.FloatField(default='.01')),
                ('specialitem4_transitionhours', models.FloatField(default='.0001')),
                ('specialitem4_transformationhoursitem', models.FloatField(default='.01')),
                ('specialitem4_transformationhours', models.FloatField(default='.0001')),
                ('specialitem5_count', models.FloatField(default='.01')),
                ('specialitem5_transitionhoursitem', models.FloatField(default='.01')),
                ('specialitem5_transitionhours', models.FloatField(default='.0001')),
                ('specialitem5_transformationhoursitem', models.FloatField(default='.01')),
                ('specialitem5_transformationhours', models.FloatField(default='.0001')),
                ('totaltransitionhoursitem', models.FloatField(default='0.0')),
                ('totaltransformationhoursitem', models.FloatField(default='0.0')),
                ('numtransitionweeks', models.FloatField(default='0.0')),
                ('numtransformationweeks', models.FloatField(default='0.0')),
            ],
        ),
    ]
