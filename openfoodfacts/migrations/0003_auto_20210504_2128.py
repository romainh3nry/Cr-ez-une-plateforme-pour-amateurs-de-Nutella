# Generated by Django 3.2 on 2021-05-04 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfoodfacts', '0002_substitute'),
    ]

    operations = [
        migrations.RenameField(
            model_name='substitute',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='substitute',
            old_name='substitute_id',
            new_name='substitute',
        ),
        migrations.RenameField(
            model_name='substitute',
            old_name='user_id',
            new_name='user',
        ),
    ]
