# Generated by Django 4.2.5 on 2023-10-11 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='comment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
