# Generated by Django 3.0.2 on 2020-02-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200220_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='images',
            field=models.ImageField(blank='True', upload_to='blog/pics'),
        ),
    ]
