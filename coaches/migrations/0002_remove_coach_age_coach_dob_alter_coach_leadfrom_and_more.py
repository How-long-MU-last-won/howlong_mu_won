# Generated by Django 5.0 on 2024-01-01 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coach',
            name='age',
        ),
        migrations.AddField(
            model_name='coach',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coach',
            name='leadFrom',
            field=models.DateField(default=0),
        ),
        migrations.AlterField(
            model_name='coach',
            name='leadTo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coach',
            name='moneySpent',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coach',
            name='numLosses',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coach',
            name='numTies',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coach',
            name='numTrophies',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coach',
            name='numWins',
            field=models.IntegerField(default=0),
        ),
    ]
