# Generated by Django 3.2.9 on 2021-11-29 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0008_auto_20211129_1738'),
        ('user1', '0013_alter_cart_resturant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='resturant',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='resturant.resturant'),
        ),
    ]
