# Generated by Django 4.1.1 on 2022-09-08 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_image_amount_p_image_description_image_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
