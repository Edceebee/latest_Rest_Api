# Generated by Django 3.2.5 on 2021-07-01 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_auto_20210701_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]