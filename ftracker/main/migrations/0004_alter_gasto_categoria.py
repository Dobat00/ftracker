# Generated by Django 5.0.4 on 2024-04-19 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_gasto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='categoria',
            field=models.CharField(choices=[('Contas do mes', 'Contas do mes'), ('Lazer', 'Lazer'), ('Compras', 'Compras')], max_length=200, null=True),
        ),
    ]
