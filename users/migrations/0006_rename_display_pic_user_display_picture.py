# Generated by Django 4.0.4 on 2022-05-04 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_display_pic_alter_user_bio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='display_pic',
            new_name='display_picture',
        ),
    ]
