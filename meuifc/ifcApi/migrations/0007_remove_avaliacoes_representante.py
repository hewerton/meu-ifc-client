# Generated by Django 2.2.5 on 2019-10-08 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ifcApi', '0006_auto_20191008_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacoes',
            name='representante',
        ),
    ]
