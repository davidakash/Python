# Generated by Django 3.2.25 on 2024-12-20 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0004_boss_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='boss',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
