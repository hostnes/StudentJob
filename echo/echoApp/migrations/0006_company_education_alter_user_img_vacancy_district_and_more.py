# Generated by Django 4.2.7 on 2023-11-13 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('echoApp', '0005_alter_comment_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, upload_to='company')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='echoApp.country')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(blank=True, default='../static/img/none-logo.png', upload_to='user_photo'),
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('celery', models.PositiveIntegerField()),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('USD', 'USD'), ('RUB', 'RUB')], default=None, max_length=255, null=True)),
                ('date_of_create', models.DateField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='echoApp.region')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='echoApp.company')),
                ('place_of_education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='echoApp.education')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='echoApp.region')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='echoApp.user'),
        ),
    ]
