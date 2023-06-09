# Generated by Django 4.2 on 2023-04-19 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('desc', models.TextField()),
                ('genre', models.CharField(max_length=50)),
                ('language', models.CharField(choices=[('Hindi', 'Hindi'), ('English', 'English'), ('Kannada', 'Kannada'), ('Bengali', 'Bengali'), ('Marathi', 'Marathi'), ('Tamil', 'Tamil')], max_length=128)),
                ('movieImage', models.ImageField(blank=True, default=None, upload_to='movie')),
            ],
        ),
    ]
