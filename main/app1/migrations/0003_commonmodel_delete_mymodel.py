# Generated by Django 5.0.6 on 2024-06-20 10:52

import app1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_mymodel_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('source', app1.models.PythonCodeField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
