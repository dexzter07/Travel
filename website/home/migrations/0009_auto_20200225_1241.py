# Generated by Django 3.0.2 on 2020-02-25 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200225_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='offer',
            new_name='orginalPrice',
        ),
    ]
