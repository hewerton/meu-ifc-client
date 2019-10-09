# Generated by Django 2.2.5 on 2019-10-08 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ifcApi', '0002_avaliacoes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifcApi.Turma')),
            ],
        ),
    ]
