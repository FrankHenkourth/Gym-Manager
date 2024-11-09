# Generated by Django 4.2.13 on 2024-06-15 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membresias', '0002_alter_cellclient_idcliente_alter_clientes_idmember_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cellclient',
            old_name='telef',
            new_name='telefono',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='nomb',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='clientplant',
            old_name='idclieplan',
            new_name='id_clie_plan',
        ),
        migrations.RenameField(
            model_name='planes',
            old_name='descriplan',
            new_name='descripcion_plan',
        ),
        migrations.RenameField(
            model_name='planes',
            old_name='nomplan',
            new_name='nombre_plan',
        ),
        migrations.RenameField(
            model_name='tipoplan',
            old_name='idtyplan',
            new_name='id_ty_plan',
        ),
        migrations.AddField(
            model_name='cellclient',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='clientes',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='clientplant',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='membresia',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='planes',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tipoplan',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]