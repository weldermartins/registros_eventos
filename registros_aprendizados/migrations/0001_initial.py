# Generated by Django 4.0.5 on 2022-06-01 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=200)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('topico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros_aprendizados.topico')),
            ],
            options={
                'verbose_name_plural': 'assunto',
            },
        ),
    ]
