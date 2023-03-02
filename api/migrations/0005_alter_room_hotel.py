# Generated by Django 4.1.7 on 2023-03-02 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_customer_is_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='api.hotel'),
        ),
    ]