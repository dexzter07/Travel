# Generated by Django 3.0.2 on 2020-02-26 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20200226_1730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='totalPrice',
            new_name='amount',
        ),
    ]