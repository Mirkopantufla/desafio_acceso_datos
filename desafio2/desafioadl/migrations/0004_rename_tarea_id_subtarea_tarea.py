# Generated by Django 4.2 on 2024-05-23 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desafioadl', '0003_alter_subtarea_tarea_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtarea',
            old_name='tarea_id',
            new_name='tarea',
        ),
    ]
