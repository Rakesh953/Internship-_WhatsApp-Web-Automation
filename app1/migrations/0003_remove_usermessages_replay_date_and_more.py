# Generated by Django 4.1.7 on 2023-07-30 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_profile_usermessages_delete_usermessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermessages',
            name='replay_Date',
        ),
        migrations.RemoveField(
            model_name='usermessages',
            name='replay_Time',
        ),
        migrations.AlterField(
            model_name='usermessages',
            name='send_Date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='usermessages',
            name='send_Time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
