# Generated by Django 5.1.4 on 2024-12-07 19:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clients', '0001_initial'),
        ('Produits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('commantaire', models.TextField(blank=True, null=True)),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients.client')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avis', to='Produits.produit')),
            ],
        ),
    ]
