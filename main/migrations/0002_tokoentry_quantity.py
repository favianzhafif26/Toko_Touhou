# Generated by Django 5.1.1 on 2024-09-10 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tokoentry',
            name='quantity',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
