# Generated by Django 5.0 on 2024-01-03 20:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0003_coach_staturl_alter_coach_leadfrom_and_more'),
        ('players', '0003_player_price_alter_player_playto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='boughtBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coaches.coach'),
        ),
        migrations.AlterField(
            model_name='player',
            name='statURL',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
