# Generated by Django 5.1.2 on 2024-11-21 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='checklist',
            field=models.TextField(default='Not Approved', max_length=10),
        ),
    ]
