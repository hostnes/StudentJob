# Generated by Django 4.2.7 on 2023-11-22 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('echoApp', '0026_remove_summary_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
