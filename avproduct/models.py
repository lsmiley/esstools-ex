from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Prodvendor(models.Model):
    vendorname = models.CharField(max_length=150, unique=True)
    vendorcodename = models.CharField(max_length=150, blank=True, null=True)
    vendorcategory = models.CharField(max_length=150, blank=True, null=True)
    numvendorproducts = models.CharField(
        max_length=150, default='0', blank=True, null=True)
    vendornote = models.CharField(max_length=150, blank=True, null=True)
    vendorweburl = models.CharField(max_length=150, blank=True, null=True)
    contact1name = models.CharField(max_length=150, blank=True, null=True)
    contact1phone = models.CharField(max_length=150, blank=True, null=True)
    contact1email = models.CharField(max_length=150, blank=True, null=True)
    contact2name = models.CharField(max_length=150, blank=True, null=True)
    contact2phone = models.CharField(max_length=150, blank=True, null=True)
    contact2email = models.CharField(max_length=150, blank=True, null=True)
    contractnum = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.vendorname

    class Meta:
        ordering = ('vendorname',)


class Prodcategory(models.Model):
    id = models.AutoField(primary_key=True)
    categoryname = models.CharField(
        max_length=200,
        unique=True)

    categorynote = models.CharField(
        max_length=200,
        blank=True,
        null=True)

    def __str__(self):
        return self.categoryname

    class Meta:
        ordering = ('categoryname',)


class Avproduct(models.Model):
    prodvendor = models.ForeignKey(Prodvendor, on_delete=models.DO_NOTHING)
    prodcategory = models.ForeignKey(Prodcategory, on_delete=models.DO_NOTHING)
    productname = models.CharField(max_length=75, unique=True,)

    productdesc = models.CharField(

        max_length=75,
        blank=True,
        null=True)
    producttype = models.CharField(

        max_length=75,
        blank=True,
        null=True)
    producttypefamily = models.CharField(

        max_length=75,
        blank=True,
        null=True)
    productnote = RichTextUploadingField(blank=True, null=True)

    productcomplexitybase = models.IntegerField(
        default='550')
    productcomplexityfac = models.FloatField(
        default='1.0')

    numcomponent = models.IntegerField(default='0')
    primarycomp = models.CharField(

        max_length=75,
        blank=True,
        null=True)
    primarycompdesc = models.CharField(

        max_length=75,
        blank=True,
        null=True)

    primarycomplexity = models.IntegerField(
        default='1.0')

    totalcomplexity = models.FloatField(
        default='1.0')

    component1 = models.BooleanField(db_column='Component1')
    component1desc = models.CharField(

        max_length=75,
        blank=True,
        null=True)
    componentcomplexityhrs1 = models.FloatField(
        default='0.0')

    componentcomplexityfac1 = models.FloatField(

        default='0.0')
    memocomponent1note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent1technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component2 = models.BooleanField(db_column='Component2')
    component2desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs2 = models.FloatField(
        default='0.0')

    componentcomplexityfac2 = models.FloatField(

        default='0.0')
    memocomponent2note = models.CharField(
        max_length=150,
        blank=True,
        null=True)
    memocomponent2technote = models.CharField(
        max_length=150,
        blank=True,
        null=True)

    component3 = models.BooleanField(default=False)
    component3desc = models.CharField(
        db_column='Component3Desc',
        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs3 = models.FloatField(
        default='0.0')

    componentcomplexityfac3 = models.FloatField(

        default='0.0')
    memocomponent3note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent3technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component4 = models.BooleanField(default=False)
    component4desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs4 = models.FloatField(
        default='0.0')

    componentcomplexityfac4 = models.FloatField(

        default='0.0')
    memocomponent4note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent4technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component5 = models.BooleanField(default=False)
    component5desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    componentcomplexityhrs5 = models.FloatField(
        default='0.0')

    componentcomplexityfac5 = models.FloatField(

        default='0.0')
    memocomponent5note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent5technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component6 = models.BooleanField(default=False)
    component6desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs6 = models.FloatField(
        default='0.0')

    componentcomplexityfac6 = models.FloatField(

        default='0.0')

    memocomponent6note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent6technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component7 = models.BooleanField(default=False)
    component7desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs7 = models.FloatField(
        default='0.0')

    componentcomplexityfac7 = models.FloatField(

        default='0.0')
    memocomponent7note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent7technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    component8 = models.BooleanField(default=False)
    component8desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs8 = models.FloatField(
        default='0.0')

    componentcomplexityfac8 = models.FloatField(

        default='0.0')
    memocomponent8note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent8technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component9 = models.BooleanField(default=False)
    component9desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs9 = models.FloatField(
        default='0.0')

    componentcomplexityfac9 = models.FloatField(

        default='0.0')
    memocomponent9note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent9technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component10 = models.BooleanField(default=False)
    component10desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs10 = models.FloatField(
        default='0.0')

    componentcomplexityfac10 = models.FloatField(

        default='0.0')
    memocomponent10note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent10technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component11 = models.BooleanField(default=False)
    component11desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs11 = models.FloatField(
        default='0.0')

    componentcomplexityfac11 = models.FloatField(

        default='0.0')
    memocomponent11note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent11technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component12 = models.BooleanField(default=False)
    component12desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs12 = models.FloatField(
        default='0.0')

    componentcomplexityfac12 = models.FloatField(

        default='0.0')
    memocomponent12note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent12technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component13 = models.BooleanField(default=False)
    component13desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs13 = models.FloatField(
        default='0.0')
    componentcomplexityfac13 = models.FloatField(

        default='0.0')
    memocomponent13note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent13technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component14 = models.BooleanField(default=False)
    component14desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs14 = models.FloatField(
        default='0.0')

    componentcomplexityfac14 = models.FloatField(

        default='0.0')
    memocomponent14note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent14technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component15 = models.BooleanField(default=False)
    component15desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs15 = models.FloatField(
        default='0.0')
    componentcomplexityfac15 = models.FloatField(

        default='0.0')
    memocomponent15note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent15technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrstotal = models.FloatField(
        default='0.0')

    # numcomponents = models.IntegerField(default=False)

    memoproductnote = RichTextUploadingField(blank=True, null=True)
    memotechnicalnote = RichTextUploadingField(blank=True, null=True)
    endpoint_ip = models.BooleanField(default=False, null=True, blank=True)
    active = models.BooleanField(default=False, null=True, blank=True)
    prodimage = models.ImageField(null=True, blank=True)
    addlconsole = models.PositiveIntegerField(default=0)
    qty = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.productname

    class Meta:
        ordering = ('productname',)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
