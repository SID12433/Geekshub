# Generated by Django 4.2.5 on 2024-04-13 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0014_coder_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='project',
        ),
        migrations.AddField(
            model_name='payment',
            name='bid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.bid'),
        ),
    ]
