# Generated by Django 4.2.2 on 2023-07-01 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suntory', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='distillery',
            name='distillery_image',
            field=models.ImageField(default='distillery_images/default.jpg', upload_to='distillery_images/'),
        ),
    ]
