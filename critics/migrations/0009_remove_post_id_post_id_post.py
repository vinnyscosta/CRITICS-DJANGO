# Generated by Django 5.0.1 on 2024-03-26 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('critics', '0008_alter_post_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AddField(
            model_name='post',
            name='id_post',
            field=models.CharField(default=None, max_length=20, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
