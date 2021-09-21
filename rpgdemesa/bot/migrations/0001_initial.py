# Generated by Django 3.2.6 on 2021-09-21 00:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco_sugerido', models.FloatField(max_length=100)),
                ('qualidade', models.CharField(choices=[(None, '<selecione>'), ('ruim', 'Ruim'), ('pobre', 'Pobre'), ('medio', 'Médio'), ('bom', 'Bom'), ('excelente', 'Excelente')], max_length=100)),
                ('categoria', models.CharField(choices=[(None, '<selecione>'), ('alimentos', 'Alimentos'), ('transporte', 'Transporte'), ('academico', 'Acadêmico'), ('agricultura', 'Agricultura'), ('casa', 'Casa'), ('equipamento', 'Equipamento'), ('luxo', 'Luxo')], max_length=100)),
                ('descricao', models.CharField(max_length=100)),
                ('ativo', models.BooleanField(default=True, editable=False)),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'itens',
            },
        ),
        migrations.CreateModel(
            name='Personagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('raca', models.CharField(choices=[(None, '<selecione>'), ('humano', 'Humano'), ('anão', 'Anão'), ('dahllan', 'Dahllan'), ('elfo', 'Elfo'), ('goblin', 'Goblin'), ('lefou', 'Lefou'), ('minotauro', 'Minotauro'), ('qareen', 'Qareen'), ('golem', 'Golem'), ('hynne', 'Hynne'), ('kliren', 'Kliren'), ('medusa', 'Medusa'), ('osteon', 'Osteon'), ('sereia/tritão', 'Sereia/Tritão'), ('silfide', 'Silfide'), ('aggelos', 'Aggelos'), ('sufulre', 'Sufulre'), ('trog', 'Trog')], max_length=100, verbose_name='Raça')),
                ('classe', models.CharField(choices=[(None, '<selecione>'), ('mago', 'Mago'), ('bruxo', 'Bruxo'), ('feiticeiro', 'Feiticeiro'), ('bárbaro', 'Bárbaro'), ('bardo', 'Bardo'), ('caçador', 'Caçador'), ('cavaleiro', 'Cavaleiro'), ('clérigo', 'Clérigo'), ('druída', 'Druída'), ('guerreiro', 'Guerreiro'), ('inventor', 'Inventor'), ('ladino', 'Ladino'), ('lutador', 'Lutador'), ('nobre', 'Nobre'), ('paladino', 'Paladino')], max_length=100)),
                ('tipo', models.CharField(choices=[('jogador', 'Jogador'), ('npc', 'NPC')], default='Jogador', editable=False, max_length=100)),
                ('ativo', models.BooleanField(default=True, editable=False)),
                ('dono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'personagem',
                'verbose_name_plural': 'personagens',
            },
        ),
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Loja')),
                ('responsavel', models.ForeignKey(limit_choices_to={'ativo': True}, on_delete=django.db.models.deletion.CASCADE, to='bot.personagem', verbose_name='Responsável')),
            ],
            options={
                'verbose_name': 'loja',
                'verbose_name_plural': 'lojas',
            },
        ),
    ]
