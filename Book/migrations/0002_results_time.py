# Generated by Django 3.2.5 on 2022-05-15 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='time',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
