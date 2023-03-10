# Generated by Django 4.1.7 on 2023-03-02 06:47

from django.db import migrations, models
import django.db.models.deletion
import hotels.hotel_model


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('checkin_date', models.DateField(blank=True, null=True)),
                ('checkout_date', models.DateField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('image', models.ImageField(upload_to=hotels.hotel_model.PathAndRename('hotels'))),
            ],
            options={
                'verbose_name_plural': 'Hotels',
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Room Types',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(blank=True, max_length=50, null=True)),
                ('capacity', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('check_in_date', models.DateField(blank=True, null=True)),
                ('check_out_date', models.DateField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('image', models.ImageField(upload_to=hotels.hotel_model.PathAndRename('rooms'))),
                ('hotel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.hotel')),
                ('room_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.roomtype')),
            ],
            options={
                'verbose_name_plural': 'Rooms',
            },
        ),
    ]
