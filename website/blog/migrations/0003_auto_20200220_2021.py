# Generated by Django 3.0.2 on 2020-02-20 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200220_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='images',
            field=models.ImageField(default='', upload_to='blog/pics'),
        ),
    ]
