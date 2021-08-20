from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

from .managers import ProductManager

CURRENCY = settings.CURRENCY


class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)
    categoryname = models.CharField(
        max_length=200)

    categorynote = models.CharField(

        blank=True,
        null=True,
        max_length=500)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


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


class Product(models.Model):
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=150, unique=True)
    prodvendor = models.ForeignKey(Prodvendor, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    value = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    discount_value = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    final_value = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    qty = models.PositiveIntegerField(default=100000)

    productname = models.CharField(max_length=75)

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

    primarycomplexity = models.FloatField(
        default='0')

    totalcomplexity = models.FloatField(
        default='1')

    component1 = models.BooleanField(default=False)
    component1desc = models.CharField(

        max_length=75,
        blank=True,
        null=True)
    componentcomplexityhrs1 = models.FloatField(
        default='0.0')

    componentcomplexityfac1 = models.FloatField(

        default='0.0')
    ComponentHours1 = models.FloatField(default='0.0')
    Component1_Wkstn = models.BooleanField(default=False)
    Component1_Svr = models.BooleanField(default=False)
    Component1_IP = models.BooleanField(default=False)
    Component1_Qty = models.FloatField(default='0.0')

    memocomponent1note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent1technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component2 = models.BooleanField(default=False)
    component2desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs2 = models.FloatField(
        default='0.0')

    componentcomplexityfac2 = models.FloatField(

        default='0.0')
    ComponentHours2 = models.FloatField(default='0.0')
    Component2_Wkstn = models.BooleanField(default=False)
    Component2_Svr = models.BooleanField(default=False)
    Component2_IP = models.BooleanField(default=False)
    Component2_Qty = models.FloatField(default='0.0')
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
    ComponentHours3 = models.FloatField(default='0.0')
    Component3_Wkstn = models.BooleanField(default=False)
    Component3_Svr = models.BooleanField(default=False)
    Component3_IP = models.BooleanField(default=False)
    Component3_Qty = models.FloatField(default='0.0')
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

    ComponentHours4 = models.FloatField(default='0.0')

    Component4_Wkstn = models.BooleanField(default=False)

    Component4_Svr = models.BooleanField(default=False)

    Component4_IP = models.BooleanField(default=False)

    Component4_Qty = models.FloatField(default='0.0')

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

    ComponentHours5 = models.FloatField(default='0.0')

    Component5_Wkstn = models.BooleanField(default=False)

    Component5_Svr = models.BooleanField(default=False)

    Component5_IP = models.BooleanField(default=False)

    Component5_Qty = models.FloatField(default='0.0')

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

    ComponentHours6 = models.FloatField(default='0.0')

    Component6_Wkstn = models.BooleanField(default=False)

    Component6_Svr = models.BooleanField(default=False)

    Component6_IP = models.BooleanField(default=False)

    Component6_Qty = models.FloatField(default='0.0')

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

    ComponentHours7 = models.FloatField(default='0.0')

    Component7_Wkstn = models.BooleanField(default=False)

    Component7_Svr = models.BooleanField(default=False)

    Component7_IP = models.BooleanField(default=False)

    Component7_Qty = models.FloatField(default='0.0')

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

    ComponentHours8 = models.FloatField(default='0.0')

    Component8_Wkstn = models.BooleanField(default=False)

    Component8_Svr = models.BooleanField(default=False)

    Component8_IP = models.BooleanField(default=False)

    Component8_Qty = models.FloatField(default='0.0')

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

    ComponentHours9 = models.FloatField(default='0.0')

    Component9_Wkstn = models.BooleanField(default=False)

    Component9_Svr = models.BooleanField(default=False)

    Component9_IP = models.BooleanField(default=False)

    Component9_Qty = models.FloatField(default='0.0')

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

    ComponentHours10 = models.FloatField(default='0.0')

    Component10_Wkstn = models.BooleanField(default=False)

    Component10_Svr = models.BooleanField(default=False)

    Component10_IP = models.BooleanField(default=False)

    Component10_Qty = models.FloatField(default='0.0')

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

    ComponentHours11 = models.FloatField(default='0.0')

    Component11_Wkstn = models.BooleanField(default=False)

    Component11_Svr = models.BooleanField(default=False)

    Component11_IP = models.BooleanField(default=False)

    Component11_Qty = models.FloatField(default='0.0')

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

    ComponentHours12 = models.FloatField(default='0.0')

    Component12_Wkstn = models.BooleanField(default=False)

    Component12_Svr = models.BooleanField(default=False)

    Component12_IP = models.BooleanField(default=False)

    Component12_Qty = models.FloatField(default='0.0')

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

    ComponentHours13 = models.FloatField(default='0.0')

    Component13_Wkstn = models.BooleanField(default=False)

    Component13_Svr = models.BooleanField(default=False)

    Component13_IP = models.BooleanField(default=False)

    Component13_Qty = models.FloatField(default='0.0')

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

    ComponentHours14 = models.FloatField(default='0.0')

    Component14_Wkstn = models.BooleanField(default=False)

    Component14_Svr = models.BooleanField(default=False)

    Component14_IP = models.BooleanField(default=False)

    Component14_Qty = models.FloatField(default='0.0')

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

    ComponentHours15 = models.FloatField(default='0.0')

    Component15_Wkstn = models.BooleanField(default=False)

    Component15_Svr = models.BooleanField(default=False)

    Component15_IP = models.BooleanField(default=False)

    Component15_Qty = models.FloatField(default='0.0')

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
    prodimage = models.ImageField(null=True, blank=True)
    addlconsole = models.PositiveIntegerField(default=0)

    objects = models.Manager()
    broswer = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'

    def save(self, *args, **kwargs):
        self.final_value = self.discount_value if self.discount_value > 0 else self.value
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def tag_final_value(self):
        return f'{self.final_value} {CURRENCY}'
    tag_final_value.short_description = 'Value'



