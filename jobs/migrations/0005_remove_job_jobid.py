# Generated by Django 4.1.7 on 2023-02-23 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_alter_job_remote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='jobid',
        ),
    ]