# Generated by Django 4.0.4 on 2022-05-05 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0004_alter_submissions_date_submitted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissions',
            name='date_submitted',
            field=models.DateField(auto_now_add=True),
        ),
    ]