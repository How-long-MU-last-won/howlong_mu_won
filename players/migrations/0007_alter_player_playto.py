# Generated by Django 5.0 on 2024-01-17 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_alter_player_boughtby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='playTo',
            field=models.DateField(blank=True, null=True),
        ),
    ]
