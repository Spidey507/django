# Generated by Django 4.2.2 on 2023-06-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distillery',
            fields=[
                ('distillery_name', models.CharField(max_length=50)),
                ('distillery_country', models.CharField(max_length=50)),
                ('distillery_description', models.CharField(max_length=1000)),
                ('distillery_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.CharField(max_length=300)),
                ('size', models.IntegerField()),
                ('product_image', models.ImageField(default='product_images/suntory.jpg', upload_to='product_images/')),
            ],
        ),
    ]
