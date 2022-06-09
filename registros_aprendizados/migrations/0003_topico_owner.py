# Generated by Django 4.0.5 on 2022-06-08 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registros_aprendizados', '0002_rename_entry_assuntos'),
    ]

    operations = [
        migrations.AddField(
            model_name='topico',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
