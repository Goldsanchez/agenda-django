# Generated by Django 3.2.9 on 2021-11-25 17:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agenda',
            options={'ordering': ('nombre',), 'verbose_name': 'Contacto', 'verbose_name_plural': 'Contactos'},
        ),
        migrations.RenameField(
            model_name='agenda',
            old_name='name',
            new_name='creador',
        ),
        migrations.RenameField(
            model_name='agenda',
            old_name='phone',
            new_name='telefono',
        ),
        migrations.AddField(
            model_name='agenda',
            name='nombre',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]