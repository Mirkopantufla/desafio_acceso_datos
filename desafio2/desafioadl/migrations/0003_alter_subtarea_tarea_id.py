# Generated by Django 4.2 on 2024-05-23 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('desafioadl', '0002_rename_description_subtarea_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtarea',
            name='tarea_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtareas', to='desafioadl.tarea'),
        ),
    ]
