# Generated by Django 3.2.9 on 2021-11-29 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0006_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
