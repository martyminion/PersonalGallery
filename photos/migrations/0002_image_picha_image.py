# Generated by Django 3.0.6 on 2020-05-24 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='picha_image',
            field=models.ImageField(default='no picture', upload_to='photos/'),
            preserve_default=False,
        ),
    ]
