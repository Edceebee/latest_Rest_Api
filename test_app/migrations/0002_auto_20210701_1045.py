# Generated by Django 3.2.5 on 2021-07-01 09:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='name',
            field=models.CharField(error_messages={'blank': 'this field cannot be blank', 'null': 'this field cannot be null'}, max_length=255, null=True, unique=True),
        ),
    ]