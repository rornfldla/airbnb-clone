# Generated by Django 5.1.1 on 2024-09-22 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default='', max_length=180),
        ),
    ]
