# Generated by Django 3.2.6 on 2021-09-19 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_auto_20210919_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jogador',
            name='ativo',
        ),
        migrations.AlterField(
            model_name='jogador',
            name='is_active',
            field=models.BooleanField(default=True, editable=False),
        ),
    ]
