# Generated by Django 4.2.6 on 2023-10-18 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geographyapp', '0003_alter_country_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='description',
            field=models.TextField(help_text='Enter an interesting fact about the country'),
        ),
        migrations.AlterField(
            model_name='country',
            name='population',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='country',
            name='square',
            field=models.FloatField(),
        ),
    ]
