# Generated by Django 5.1.3 on 2024-11-23 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_farm_product_farm_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='description',
        ),
    ]