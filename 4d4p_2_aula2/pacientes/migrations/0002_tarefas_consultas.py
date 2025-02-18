# Generated by Django 4.2.19 on 2025-02-18 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarefa', models.CharField(max_length=255)),
                ('instrucoes', models.TextField()),
                ('frequencia', models.CharField(choices=[('D', 'Diário'), ('1S', '1 vez por semana'), ('2S', '2 vezes por semana'), ('3S', '3 vezes por semana'), ('N', 'Ao necessitar')], default='D', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Consultas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humor', models.PositiveIntegerField()),
                ('registro_geral', models.TextField()),
                ('video', models.FileField(upload_to='video')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.pacientes')),
                ('tarefas', models.ManyToManyField(to='pacientes.tarefas')),
            ],
        ),
    ]
