# Generated by Django 2.2.7 on 2019-11-17 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='publist_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
