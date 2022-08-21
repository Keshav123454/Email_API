# Generated by Django 4.0.6 on 2022-08-20 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='city',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='roll',
        ),
        migrations.AddField(
            model_name='student',
            name='email_body',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='email_id',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='email_sub',
            field=models.CharField(default='NA', max_length=50),
            preserve_default=False,
        ),
    ]