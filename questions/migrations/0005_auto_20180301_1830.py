# Generated by Django 2.0.2 on 2018-03-01 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20180301_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='correct',
            field=models.IntegerField(),
        ),
    ]
