# Generated by Django 2.2.3 on 2019-07-23 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appels_sortants', '0002_auto_20190723_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='adresse_postal',
        ),
        migrations.AddField(
            model_name='contact',
            name='adresse',
            field=models.TextField(blank=True, null=True),
        ),
    ]
