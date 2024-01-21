# Generated by Django 5.0.1 on 2024-01-21 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(max_length=200)),
                ('tipo', models.CharField(choices=[('opcao1', 'Medicamento'), ('opcao2', 'Alimento'), ('opcao3', 'Limpeza')], max_length=20)),
                ('marca', models.TextField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
