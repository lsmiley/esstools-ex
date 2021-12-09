# Generated by Django 4.0 on 2021-12-08 21:27

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prodcategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('categoryname', models.CharField(max_length=200, unique=True)),
                ('categorynote', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'ordering': ('categoryname',),
            },
        ),
        migrations.CreateModel(
            name='Prodvendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendorname', models.CharField(max_length=150, unique=True)),
                ('vendorcodename', models.CharField(blank=True, max_length=150, null=True)),
                ('vendorcategory', models.CharField(blank=True, max_length=150, null=True)),
                ('numvendorproducts', models.CharField(blank=True, default='0', max_length=150, null=True)),
                ('vendornote', models.CharField(blank=True, max_length=150, null=True)),
                ('vendorweburl', models.CharField(blank=True, max_length=150, null=True)),
                ('contact1name', models.CharField(blank=True, max_length=150, null=True)),
                ('contact1phone', models.CharField(blank=True, max_length=150, null=True)),
                ('contact1email', models.CharField(blank=True, max_length=150, null=True)),
                ('contact2name', models.CharField(blank=True, max_length=150, null=True)),
                ('contact2phone', models.CharField(blank=True, max_length=150, null=True)),
                ('contact2email', models.CharField(blank=True, max_length=150, null=True)),
                ('contractnum', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'ordering': ('vendorname',),
            },
        ),
        migrations.CreateModel(
            name='Avproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=75, unique=True)),
                ('productdesc', models.CharField(blank=True, max_length=75, null=True)),
                ('producttype', models.CharField(blank=True, max_length=75, null=True)),
                ('producttypefamily', models.CharField(blank=True, max_length=75, null=True)),
                ('productnote', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('productcomplexitybase', models.IntegerField(default='550')),
                ('productcomplexityfac', models.FloatField(default='1.0')),
                ('numcomponent', models.IntegerField(default='0')),
                ('primarycomp', models.CharField(blank=True, max_length=75, null=True)),
                ('primarycompdesc', models.CharField(blank=True, max_length=75, null=True)),
                ('primarycomplexity', models.IntegerField(default='1.0')),
                ('totalcomplexity', models.FloatField(default='1.0')),
                ('component1', models.BooleanField(db_column='Component1')),
                ('component1desc', models.CharField(blank=True, max_length=75, null=True)),
                ('componentcomplexityhrs1', models.FloatField(default='0.0')),
                ('componentcomplexityfac1', models.FloatField(default='0.0')),
                ('memocomponent1note', models.CharField(blank=True, max_length=150, null=True)),
                ('memocomponent1technote', models.CharField(blank=True, max_length=150, null=True)),
                ('component2', models.BooleanField(db_column='Component2')),
                ('component2desc', models.CharField(blank=True, max_length=150, null=True)),
                ('componentcomplexityhrs2', models.FloatField(default='0.0')),
                ('componentcomplexityfac2', models.FloatField(default='0.0')),
                ('memocomponent2note', models.CharField(blank=True, max_length=150, null=True)),
                ('memocomponent2technote', models.CharField(blank=True, max_length=150, null=True)),
                ('component3', models.BooleanField(default=False)),
                ('component3desc', models.CharField(blank=True, db_column='Component3Desc', max_length=150, null=True)),
                ('componentcomplexityhrs3', models.FloatField(default='0.0')),
                ('componentcomplexityfac3', models.FloatField(default='0.0')),
                ('memocomponent3note', models.CharField(blank=True, max_length=150, null=True)),
                ('memocomponent3technote', models.CharField(blank=True, max_length=150, null=True)),
                ('component4', models.BooleanField(default=False)),
                ('component4desc', models.CharField(blank=True, max_length=150, null=True)),
                ('componentcomplexityhrs4', models.FloatField(default='0.0')),
                ('componentcomplexityfac4', models.FloatField(default='0.0')),
                ('memocomponent4note', models.CharField(blank=True, max_length=150, null=True)),
                ('memocomponent4technote', models.CharField(blank=True, max_length=150, null=True)),
                ('component5', models.BooleanField(default=False)),
                ('component5desc', models.CharField(blank=True, max_length=150, null=True)),
                ('componentcomplexityhrs5', models.FloatField(default='0.0')),
                ('componentcomplexityfac5', models.FloatField(default='0.0')),
                ('memocomponent5note', models.CharField(blank=True, max_length=150, null=True)),
                ('memocomponent5technote', models.CharField(blank=True, max_length=150, null=True)),
                ('component6', models.BooleanField(default=False)),
                ('component6desc', models.CharField(blank=True, max_length=150, null=True)),
                ('componentcomplexityhrs6', models.FloatField(default='0.0')),
                ('componentcomplexityfac6', models.FloatField(default='0.0')),
                ('memocomponent6note', models.CharField(blank=True, max_length=150, null=True)),
                ('memocomponent6technote', models.CharField(blank=True, max_length=150, null=True)),
                ('component7', models.BooleanField(default=False)),
                ('component7desc', models.CharField(blank=True, max_length=150, null=True)),
                ('componentcomplexityhrs7', models.FloatField(default='0.0')),
                ('componentcomplexityfac7', models.FloatField(default='0.0')),
                ('memocomponent7note', models.CharField(blank=True, max_length=150, null=True)),
                ('memocomponent7technote', models.CharField(blank=True, max_length=150, null=True)),
                ('component8', models.BooleanField(default=False)),
                ('component8desc', models.CharField(blank=True, max_length=150, null=True)),
                ('componentcomplexityhrs8', models.FloatField(default='0.0')),
                ('componentcomplexityfac8', models.FloatField(default='0.0')),
                ('memocomponent8note', models.CharField(blank=True, max_length=150, null=True)),
                ('memocomponent8technote', models.CharField(blank=True, max_length=150, null=True)),
                ('component9', models.BooleanField(default=False)),
                ('component9desc', models.CharField(blank=True, max_length=150, null=True)),
                ('componentcomplexityhrs9', models.FloatField(default='0.0')),
                ('componentcomplexityfac9', models.FloatField(default='0.0')),
                ('memocomponent9note', models.CharField(blank=True, max_length=150, null=True)),
                ('memocomponent9technote', models.CharField(blank=True, max_length=150, null=True)),
                ('component10', models.BooleanField(default=False)),
                ('component10desc', models.CharField(blank=True, max_length=150, null=True)),
                ('componentcomplexityhrs10', models.FloatField(default='0.0')),
                ('componentcomplexityfac10', models.FloatField(default='0.0')),
                ('memocomponent10note', models.CharField(blank=True, max_length=150, null=True)),
                ('memocomponent10technote', models.CharField(blank=True, max_length=150, null=True)),
                ('component11', models.BooleanField(default=False)),
                ('component11desc', models.CharField(blank=True, max_length=150, null=True)),
                ('componentcomplexityhrs11', models.FloatField(default='0.0')),
                ('componentcomplexityfac11', models.FloatField(default='0.0')),
                ('memocomponent11note', models.CharField(blank=True, max_length=150, null=True)),
                ('memocomponent11technote', models.CharField(blank=True, max_length=150, null=True)),
                ('component12', models.BooleanField(default=False)),
                ('component12desc', models.CharField(blank=True, max_length=150, null=True)),
                ('componentcomplexityhrs12', models.FloatField(default='0.0')),
                ('componentcomplexityfac12', models.FloatField(default='0.0')),
                ('memocomponent12note', models.CharField(blank=True, max_length=150, null=True)),
                ('memocomponent12technote', models.CharField(blank=True, max_length=150, null=True)),
                ('component13', models.BooleanField(default=False)),
                ('component13desc', models.CharField(blank=True, max_length=150, null=True)),
                ('componentcomplexityhrs13', models.FloatField(default='0.0')),
                ('componentcomplexityfac13', models.FloatField(default='0.0')),
                ('memocomponent13note', models.CharField(blank=True, max_length=150, null=True)),
                ('memocomponent13technote', models.CharField(blank=True, max_length=150, null=True)),
                ('component14', models.BooleanField(default=False)),
                ('component14desc', models.CharField(blank=True, max_length=150, null=True)),
                ('componentcomplexityhrs14', models.FloatField(default='0.0')),
                ('componentcomplexityfac14', models.FloatField(default='0.0')),
                ('memocomponent14note', models.CharField(blank=True, max_length=150, null=True)),
                ('memocomponent14technote', models.CharField(blank=True, max_length=150, null=True)),
                ('component15', models.BooleanField(default=False)),
                ('component15desc', models.CharField(blank=True, max_length=150, null=True)),
                ('componentcomplexityhrs15', models.FloatField(default='0.0')),
                ('componentcomplexityfac15', models.FloatField(default='0.0')),
                ('memocomponent15note', models.CharField(blank=True, max_length=150, null=True)),
                ('memocomponent15technote', models.CharField(blank=True, max_length=150, null=True)),
                ('componentcomplexityhrstotal', models.FloatField(default='0.0')),
                ('memoproductnote', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('memotechnicalnote', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('endpoint_ip', models.BooleanField(blank=True, default=False, null=True)),
                ('active', models.BooleanField(blank=True, default=False, null=True)),
                ('prodimage', models.ImageField(blank=True, null=True, upload_to='')),
                ('addlconsole', models.PositiveIntegerField(default=0)),
                ('qty', models.PositiveIntegerField(default=0)),
                ('prodcategory', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='avproduct.prodcategory')),
                ('prodvendor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='avproduct.prodvendor')),
            ],
            options={
                'ordering': ('productname',),
            },
        ),
    ]