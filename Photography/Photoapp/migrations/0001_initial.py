# Generated by Django 4.2.6 on 2023-10-30 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Fotógrafo')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Fotógrafo',
                'verbose_name_plural': 'Fotógrafos',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Género')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Género',
                'verbose_name_plural': 'Géneros',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Fotografía')),
                ('description', models.TextField(verbose_name='Detalle')),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, 'Pricipiante'), (2, 'Intermedio'), (3, 'Avanzado'), (4, 'Experto'), (5, 'Profesional')])),
                ('image', models.ImageField(blank=True, null=True, upload_to='Photo', verbose_name='Imagen')),
                ('year', models.SmallIntegerField(blank=True, verbose_name='Año de captura')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Photoapp.author', verbose_name='Fotógrafo')),
                ('genders', models.ManyToManyField(to='Photoapp.gender', verbose_name='Géneros')),
            ],
            options={
                'verbose_name': 'Fotografía',
                'verbose_name_plural': 'Fotografías',
            },
        ),
    ]
