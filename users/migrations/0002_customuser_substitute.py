# Generated by Django 3.2 on 2021-04-24 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openfoodfacts', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='substitute',
            field=models.ManyToManyField(
                to='openfoodfacts.Product'),
        ),
    ]