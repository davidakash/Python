# Generated by Django 3.2.25 on 2024-12-12 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lucky',
            name='Place',
        ),
        migrations.AlterField(
            model_name='lucky',
            name='AccNo',
            field=models.IntegerField(),
        ),
    ]
