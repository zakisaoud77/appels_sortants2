# Generated by Django 2.2.3 on 2019-07-25 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appels_sortants', '0011_auto_20190725_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='adresse',
            field=models.TextField(blank=True, default='0', null=True),
        ),
    ]
