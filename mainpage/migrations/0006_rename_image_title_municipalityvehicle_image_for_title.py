# Generated by Django 4.2.6 on 2023-10-28 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_alter_firefightingvehicle_image_for_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='municipalityvehicle',
            old_name='image_title',
            new_name='image_for_title',
        ),
    ]