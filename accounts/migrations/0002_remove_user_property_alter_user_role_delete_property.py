# Generated by Django 5.1.6 on 2025-03-06 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='property',
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('superadmin', 'Super Admin'), ('landlord', 'Landlord'), ('tenant', 'Tenant')], max_length=20),
        ),
        migrations.DeleteModel(
            name='Property',
        ),
    ]
