# Generated by Django 2.2.3 on 2019-07-24 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appels_sortants', '0004_auto_20190723_1721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='dernier_appel_date',
            new_name='Dernier appel',
        ),
    ]