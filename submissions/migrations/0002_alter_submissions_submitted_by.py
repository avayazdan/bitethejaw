# Generated by Django 4.0.4 on 2022-05-03 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_email_user_password'),
        ('submissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissions',
            name='submitted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='submitted_by', to='users.user'),
        ),
    ]
