# Generated by Django 5.1.1 on 2024-10-06 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
