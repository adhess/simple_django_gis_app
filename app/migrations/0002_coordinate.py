# Generated by Django 3.2.5 on 2021-07-30 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('service_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.servicearea')),
            ],
        ),
    ]
