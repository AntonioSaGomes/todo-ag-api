# Generated by Django 4.1.5 on 2023-01-12 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_alter_todo_duedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='order',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='todo',
            name='section',
            field=models.CharField(default='In Progress', max_length=100),
        ),
    ]
