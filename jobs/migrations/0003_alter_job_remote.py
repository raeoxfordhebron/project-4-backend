# Generated by Django 4.1.7 on 2023-02-22 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='remote',
            field=models.BooleanField(blank=True),
        ),
    ]