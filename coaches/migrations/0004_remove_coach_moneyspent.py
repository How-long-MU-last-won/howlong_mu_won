# Generated by Django 5.0 on 2024-01-14 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0003_coach_staturl_alter_coach_leadfrom_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coach',
            name='moneySpent',
        ),
    ]
