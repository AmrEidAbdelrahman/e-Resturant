# Generated by Django 3.2.9 on 2021-11-29 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0008_auto_20211129_1738'),
        ('user1', '0007_auto_20211128_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='resturant',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='resturant.resturant'),
            preserve_default=False,
        ),
    ]
