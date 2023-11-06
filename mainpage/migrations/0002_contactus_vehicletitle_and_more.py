# Generated by Django 4.2.6 on 2023-10-27 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام ')),
                ('email', models.EmailField(max_length=200, verbose_name='ایمیل')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان')),
                ('message', models.TextField(verbose_name='متن')),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'تماس های با ما',
            },
        ),
        migrations.CreateModel(
            name='VehicleTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='دسته بندی خودرو')),
            ],
            options={
                'verbose_name': 'دسته بندی خودرو',
                'verbose_name_plural': 'دسته بندی خودروها',
            },
        ),
        migrations.RemoveField(
            model_name='firefightingvehicle',
            name='image_title',
        ),
        migrations.RemoveField(
            model_name='firefightingvehicle',
            name='specification',
        ),
        migrations.AddField(
            model_name='firefightingvehicle',
            name='chassis_english',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='شاسی به انگلیسی'),
        ),
        migrations.AddField(
            model_name='firefightingvehicle',
            name='image_for_title',
            field=models.ImageField(default='exit', upload_to='media/', verbose_name='عکس اصلی'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='title_photo',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='عنوان عکس'),
        ),
        migrations.RemoveField(
            model_name='firefightingvehicle',
            name='img',
        ),
        migrations.CreateModel(
            name='MunicipalityVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.ImageField(upload_to='media1/', verbose_name='عکس اصلی')),
                ('uses', models.CharField(blank=True, max_length=400, null=True, verbose_name='موارد استفاده')),
                ('dimension', models.CharField(blank=True, max_length=200, null=True, verbose_name='ابعاد(میلیمتر)(ارتفاع*عرض*طول)')),
                ('chassis', models.CharField(max_length=100, verbose_name='شاسی')),
                ('chassis_english', models.CharField(blank=True, max_length=150, null=True, verbose_name='شاسی به انگلیسی')),
                ('cooling_system', models.TextField(blank=True, null=True, verbose_name='سیستم خنک کننده')),
                ('hydraulic_pump', models.CharField(blank=True, max_length=200, null=True, verbose_name='پمپ هیدرولیک')),
                ('tank', models.CharField(blank=True, max_length=300, null=True, verbose_name='مخزن')),
                ('refuse_tank', models.CharField(blank=True, max_length=300, null=True, verbose_name='مخزن زباله')),
                ('hopper', models.CharField(blank=True, max_length=300, null=True, verbose_name='هاپر')),
                ('been_off_load_mechanism', models.CharField(blank=True, max_length=350, null=True, verbose_name='مکانیزم تخلیه سطل')),
                ('drain_shovel', models.CharField(blank=True, max_length=350, null=True, verbose_name='بیل تخلیه')),
                ('hydraulic_equipment', models.TextField(blank=True, null=True, verbose_name='تجهیزات هیدرولیکی')),
                ('pressing_system', models.CharField(blank=True, max_length=200, null=True, verbose_name='سیستم پرس زباله')),
                ('water_pump', models.CharField(blank=True, max_length=200, null=True, verbose_name='پمپ آب')),
                ('water_tank', models.CharField(blank=True, max_length=500, null=True, verbose_name='مخزن آب')),
                ('cabin', models.TextField(blank=True, null=True, verbose_name='کابین')),
                ('door', models.TextField(blank=True, null=True, verbose_name='درب ها')),
                ('roller_shutter', models.CharField(blank=True, max_length=300, null=True, verbose_name='کرکره ها')),
                ('powder_system', models.TextField(blank=True, null=True, verbose_name='سیستم پودر')),
                ('equipment', models.TextField(verbose_name='تجهیزات')),
                ('slug', models.SlugField(default='', max_length=400, unique=True, verbose_name='عنوان در url')),
                ('img', models.ManyToManyField(blank=True, null=True, to='mainpage.image', verbose_name='عکس')),
                ('title', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainpage.vehicletitle', verbose_name='دسته بندی خودرها')),
            ],
            options={
                'verbose_name': 'خودرو خدمات شهری',
                'verbose_name_plural': 'خودرو های خدمات شهری',
            },
        ),
        migrations.AddField(
            model_name='firefightingvehicle',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainpage.vehicletitle', verbose_name='دسته بندی خودرها'),
        ),
        migrations.AddField(
            model_name='firefightingvehicle',
            name='img',
            field=models.ManyToManyField(blank=True, null=True, to='mainpage.image', verbose_name='عکس'),
        ),
    ]
