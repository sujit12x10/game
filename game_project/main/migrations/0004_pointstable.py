# Generated by Django 4.0 on 2024-04-08 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_match_loser_alter_match_team1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointsTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points_table', to='main.season')),
            ],
        ),
    ]
