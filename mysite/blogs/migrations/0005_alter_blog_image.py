# Generated by Django 5.0 on 2023-12-16 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='images/me.png', upload_to='images/blogs/'),
        ),
    ]
