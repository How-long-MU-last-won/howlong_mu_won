# Generated by Django 5.0 on 2024-01-15 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0005_coach_moneyspent'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='numPlayersUsed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coach',
            name='shortDesc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
