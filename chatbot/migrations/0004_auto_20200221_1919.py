# Generated by Django 3.0.3 on 2020-02-21 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0003_order_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='toppings',
            field=models.ManyToManyField(null=True, related_name='toppings', to='chatbot.Toppings'),
        ),
    ]
