# Generated by Django 3.2.4 on 2021-07-17 20:42

from django.db import migrations

import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
    ]