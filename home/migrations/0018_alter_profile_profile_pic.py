# Generated by Django 4.0.2 on 2022-02-11 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='userprofile.png', null=True, upload_to='upload/'),
        ),
    ]