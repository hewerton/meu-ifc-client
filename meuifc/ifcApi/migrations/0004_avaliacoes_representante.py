# Generated by Django 2.2.5 on 2019-10-08 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ifcApi', '0003_representante_turma'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacoes',
            name='representante',
            field=models.ForeignKey(default='df', on_delete=django.db.models.deletion.CASCADE, to='ifcApi.Representante'),
        ),
    ]
