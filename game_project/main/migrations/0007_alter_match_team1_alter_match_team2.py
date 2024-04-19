# Generated by Django 4.0 on 2024-04-10 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_match_discription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='team1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='main.team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='team2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='main.team'),
        ),
    ]
