# Generated by Django 3.2.9 on 2022-07-11 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator_url', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(max_length=250, null=True, unique=True),
        ),
    ]
