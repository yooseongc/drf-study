# Generated by Django 4.0 on 2021-12-18 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_permission_role_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='name',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='role',
            name='name',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
    ]
