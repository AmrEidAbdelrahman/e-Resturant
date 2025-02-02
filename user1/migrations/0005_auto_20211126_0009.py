# Generated by Django 3.2.9 on 2021-11-25 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0004_delete_cart'),
        ('user1', '0004_alter_cart_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='detail',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='item',
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user1.cart')),
                ('item', models.ManyToManyField(to='resturant.Item')),
                ('resturant', models.ManyToManyField(to='resturant.Resturant')),
            ],
        ),
    ]
