# Generated by Django 2.0.6 on 2018-06-21 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='silo_data',
            fields=[
                ('iAutoId', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('info', models.CharField(default=None, max_length=256)),
            ],
        ),
    ]
