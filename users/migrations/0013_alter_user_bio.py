# Generated by Django 4.0.4 on 2022-05-10 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_remove_user_submissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.CharField(default='Add your bio here', max_length=1000),
        ),
    ]
