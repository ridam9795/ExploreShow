# Generated by Django 4.2 on 2023-05-01 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0009_alter_sport_prices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='language',
        ),
        migrations.AddField(
            model_name='activity',
            name='category',
            field=models.CharField(choices=[('Adventure', 'Adventure'), ('Tourist Attractions', 'Tourist Attractions'), ('NightLife', 'NightLife'), ('Food and Drinks', 'Food and Drinks'), ('Parties', 'Parties'), ('Gaming', 'Gaming')], default='Adventure', max_length=128),
        ),
        migrations.AddField(
            model_name='activity',
            name='prices',
            field=models.CharField(choices=[('Free', 'Free'), ('0-500', '0-500'), ('501-2000', '501-2000'), ('Above 2000', 'Above 2000')], default='Free', max_length=128),
        ),
    ]
