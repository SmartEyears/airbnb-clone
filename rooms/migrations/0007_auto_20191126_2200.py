# Generated by Django 2.2.5 on 2019-11-26 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_auto_20191124_2334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='amenity',
            new_name='amenities',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='facility',
            new_name='facilities',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='houseRule',
            new_name='house_rules',
        ),
    ]
