# Generated by Django 4.2.16 on 2024-11-06 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enquiry',
            options={'ordering': ['created_on'], 'verbose_name_plural': 'Enquiries'},
        ),
    ]