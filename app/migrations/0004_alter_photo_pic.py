# Generated by Django 5.1.7 on 2025-04-02 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='pic',
            field=models.ImageField(upload_to='static'),
        ),
    ]
