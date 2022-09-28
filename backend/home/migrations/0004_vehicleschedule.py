# Generated by Django 2.2.28 on 2022-09-28 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_vehicle'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True)),
                ('end_time', models.DateTimeField(blank=True)),
                ('from_location', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicleschedule_from_location', to='home.Location')),
                ('to_location', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicleschedule_to_location', to='home.Location')),
                ('vehicle_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicleschedule_vehicle_id', to='home.Vehicle')),
            ],
        ),
    ]
