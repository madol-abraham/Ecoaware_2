# Generated by Django 5.0.7 on 2024-07-18 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_created_at_donation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
