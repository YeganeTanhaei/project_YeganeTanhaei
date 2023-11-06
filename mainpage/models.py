from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Image(models.Model):
    title_photo = models.CharField(max_length=250, null=True, blank=True, verbose_name='عنوان عکس')
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return f'{self.title_photo}'

    class Meta:
        verbose_name = 'بارگذاری عکس'
        verbose_name_plural = 'بارگذاری عکس ها'


class VehicleTitle(models.Model):
    title = models.CharField(max_length=200, verbose_name='دسته بندی خودرو')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'دسته بندی خودرو'
        verbose_name_plural = 'دسته بندی خودروها'


class FireFightingVehicle(models.Model):
    img = models.ManyToManyField(Image, null=True, blank=True, verbose_name='عکس')
    title = models.ForeignKey(VehicleTitle, on_delete=models.CASCADE, null=True, blank=True,
                              verbose_name='دسته بندی خودرها')
    image_title = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name='عکس اصلی')
    uses = models.CharField(max_length=200, null=True, blank=True, verbose_name='موارد استفاده')
    dimension = models.CharField(max_length=200, null=True, blank=True, verbose_name='ابعاد(میلیمتر)(ارتفاع*عرض*طول)')
    chassis = models.CharField(max_length=100, verbose_name='شاسی')
    chassis_english = models.CharField(max_length=150, verbose_name='شاسی به انگلیسی', null=True, blank=True)
    extinguishing_system = models.TextField(null=True, blank=True, verbose_name='سیستم اطفا')
    water_pump = models.CharField(max_length=200, null=True, blank=True, verbose_name='پمپ آب')
    water_tank = models.CharField(max_length=500, null=True, blank=True, verbose_name='مخزن آب')
    foam_tank = models.CharField(max_length=200, null=True, blank=True, verbose_name='مخزن فوم')
    monitor = models.CharField(max_length=500, null=True, blank=True, verbose_name='مانیتور')
    hose_reel = models.CharField(max_length=500, null=True, blank=True, verbose_name='هوزریل')
    cabin = models.TextField(verbose_name='کابین')
    roller_shutter = models.CharField(max_length=300, null=True, blank=True, verbose_name='کرکره ها')
    powder_system = models.TextField(null=True, blank=True, verbose_name='سیستم پودر')
    equipment = models.TextField(verbose_name='تجهیزات')
    slug = models.SlugField(max_length=400, unique=True, default='', null=False, db_index=True,
                            verbose_name='عنوان در url')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.chassis_english)
        super().save()

    def __str__(self):
        return f'{self.chassis}'

    class Meta:
        verbose_name = 'خودرو آتش نشانی'
        verbose_name_plural = 'خودرو های آتش نشانی'

    def get_absolute_url(self):
        return reverse('single', args={self.slug})


class MunicipalityVehicle(models.Model):
    img = models.ManyToManyField(Image, null=True, blank=True, verbose_name='عکس')
    title = models.ForeignKey(VehicleTitle, on_delete=models.CASCADE, null=True, blank=True,
                              verbose_name='دسته بندی خودرها')
    image_title = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name='عکس اصلی')
    uses = models.CharField(max_length=400, null=True, blank=True, verbose_name='موارد استفاده')
    dimension = models.CharField(max_length=200, null=True, blank=True, verbose_name='ابعاد(میلیمتر)(ارتفاع*عرض*طول)')
    chassis = models.CharField(max_length=100, verbose_name='شاسی')
    chassis_english = models.CharField(max_length=150, verbose_name='شاسی به انگلیسی', null=True, blank=True)
    cooling_system = models.TextField(null=True, blank=True, verbose_name='سیستم خنک کننده')
    hydraulic_pump = models.CharField(max_length=200, null=True, blank=True, verbose_name='پمپ هیدرولیک')
    tank = models.CharField(max_length=300, null=True, blank=True, verbose_name='مخزن')
    refuse_tank = models.CharField(max_length=300, null=True, blank=True, verbose_name='مخزن زباله')
    hopper = models.CharField(max_length=300, null=True, blank=True, verbose_name='هاپر')
    been_off_load_mechanism = models.CharField(max_length=350, null=True, blank=True, verbose_name='مکانیزم تخلیه سطل')
    drain_shovel = models.CharField(max_length=350, null=True, blank=True, verbose_name='بیل تخلیه')
    hydraulic_equipment = models.TextField(null=True, blank=True, verbose_name='تجهیزات هیدرولیکی')
    pressing_system = models.CharField(max_length=200, null=True, blank=True, verbose_name='سیستم پرس زباله')
    water_pump = models.CharField(max_length=200, null=True, blank=True, verbose_name='پمپ آب')
    water_tank = models.CharField(max_length=500, null=True, blank=True, verbose_name='مخزن آب')
    cabin = models.TextField(null=True, blank=True, verbose_name='کابین')
    door = models.TextField(null=True, blank=True, verbose_name='درب ها')
    roller_shutter = models.CharField(max_length=300, null=True, blank=True, verbose_name='کرکره ها')
    powder_system = models.TextField(null=True, blank=True, verbose_name='سیستم پودر')
    equipment = models.TextField(verbose_name='تجهیزات')
    slug = models.SlugField(max_length=400, unique=True, default='', null=False, db_index=True,
                            verbose_name='عنوان در url')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.chassis_english)
        super().save()

    def __str__(self):
        return f'{self.chassis}'

    class Meta:
        verbose_name = 'خودرو خدمات شهری'
        verbose_name_plural = 'خودرو های خدمات شهری'

    def get_absolute_url(self):
        return reverse('municipality_single', args={self.slug})


class ContactUs(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام ')
    email = models.EmailField(max_length=200, verbose_name='ایمیل')
    title = models.CharField(max_length=300, verbose_name='عنوان')
    message = models.TextField(verbose_name='متن')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس های با ما'

class AmbulanceVehicle(models.Model):
    img = models.ManyToManyField(Image, null=True, blank=True, verbose_name='عکس')
    title = models.ForeignKey(VehicleTitle, on_delete=models.CASCADE, null=True, blank=True,
                              verbose_name='دسته بندی خودرها')
    image_title = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name='عکس اصلی')
    chassis = models.CharField(max_length=100,null=True,blank=True, verbose_name='شاسی')
    chassis_english = models.CharField(max_length=150, verbose_name='شاسی به انگلیسی', null=True, blank=True)
    sick_cabin=models.TextField(null=True,blank=True,verbose_name='کابین بیمار')
    electricity_lighting_system=models.TextField(null=True,blank=True,verbose_name='سیستم برق و روشنایی ')
    cooling_heating_system=models.CharField(max_length=400,null=True,blank=True,verbose_name='سیستم سرمایش و گرمایش ')
    ambulance_signs=models.TextField(null=True,blank=True,verbose_name='سیستم آلارم و آژیر و علائم ظاهری آمبولانس')
    medical_equipment=models.TextField(null=True,blank=True,verbose_name='تجهیزات پزشکی')
    slug = models.SlugField(max_length=400, unique=True, default='', null=False, db_index=True,
                            verbose_name='عنوان در url')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.chassis_english)
        super().save()

    def __str__(self):
        return f'{self.chassis}'

    class Meta:
        verbose_name='خودرو آمبولانس'
        verbose_name_plural='خودرهای آمبولانس'

    def get_absolute_url(self):
        return reverse('ambulance_single', args={self.slug})

class Pump(models.Model):
    img = models.ManyToManyField(Image, null=True, blank=True, verbose_name='عکس')
    title = models.ForeignKey(VehicleTitle, on_delete=models.CASCADE, null=True, blank=True,
                              verbose_name='دسته بندی خودرها')
    image_title = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name='عکس اصلی')
    pump_model=models.CharField(max_length=100,verbose_name='مدل پمپ')
    pump_type=models.CharField(max_length=100,null=True,blank=True,verbose_name='نوع پمپ')
    body_material=models.CharField(max_length=300,null=True,blank=True,verbose_name='جنس بدنه پمپ')
    shaft_material=models.CharField(max_length=200,null=True,blank=True,verbose_name='جنس شفت')
    Kind_butterfly=models.CharField(max_length=100,null=True,blank=True,verbose_name='جنس پروانه')
    flow_direction=models.CharField(max_length=100,null=True,blank=True,verbose_name='جهت گردش')
    maximum_pressure=models.CharField(max_length=300,null=True,blank=True,verbose_name='حداکثر فشار بسته')
    Output_flow_rate=models.CharField(max_length=400,null=True,blank=True,verbose_name='دبی خروجی')
    required_distance=models.CharField(max_length=150,null=True,blank=True,verbose_name='دور مورد نیاز پمپ')
    Vacuum_type=models.CharField(max_length=100,null=True,blank=True,verbose_name='نوع خلاء')
    preparation_speed=models.CharField(max_length=100,null=True,blank=True,verbose_name='سرعت آماده سازی پمپ')
    maximum_suction_depth=models.CharField(max_length=50,null=True,blank=True,verbose_name='حداکثر عمق مکش')
    description=models.TextField(verbose_name='توضیحات')
    slug = models.SlugField(max_length=400, unique=True, default='', null=False, db_index=True,
                            verbose_name='عنوان در url')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.pump_model)
        super().save()

    def __str__(self):
        return f'{self.pump_model}'

    class Meta:
        verbose_name='پمپ آتش نشانی'
        verbose_name_plural='پمپ های آتش نشانی'

    def get_absolute_url(self):
        return reverse('pump_single', args={self.slug})