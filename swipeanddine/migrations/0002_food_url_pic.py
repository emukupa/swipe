# Generated by Django 2.0.7 on 2018-07-11 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swipeanddine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='url_pic',
            field=models.CharField(default='', max_length=200),
        ),
    ]
