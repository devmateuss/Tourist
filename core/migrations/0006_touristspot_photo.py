# Generated by Django 2.1.7 on 2019-03-18 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_touristspot_adresses'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspot',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='touristic_point'),
        ),
    ]
