# Generated by Django 3.0.3 on 2020-02-21 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0002_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
