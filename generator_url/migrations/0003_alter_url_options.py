# Generated by Django 3.2.9 on 2022-07-11 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator_url', '0002_alter_url_short_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='url',
            options={'ordering': ('-created',)},
        ),
    ]
