# Generated by Django 5.0 on 2023-12-16 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='images/me.png', upload_to='images/'),
        ),
    ]
