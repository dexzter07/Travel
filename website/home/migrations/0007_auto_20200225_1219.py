# Generated by Django 3.0.2 on 2020-02-25 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200225_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='discount',
            field=models.IntegerField(),
        ),
    ]
