# Generated by Django 5.0.6 on 2024-06-20 10:01

import app1.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='source',
            field=app1.models.PythonCodeField(blank=True, null=True),
        ),
    ]