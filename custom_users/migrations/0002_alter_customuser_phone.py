# Generated by Django 5.0.3 on 2024-03-29 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(default='+996', max_length=100, unique=True),
        ),
    ]