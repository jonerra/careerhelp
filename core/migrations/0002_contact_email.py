# Generated by Django 2.1.4 on 2018-12-11 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]