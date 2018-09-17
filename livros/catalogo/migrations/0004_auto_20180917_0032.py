# Generated by Django 2.1 on 2018-09-17 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_auto_20180907_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fonte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text="Titulo da fonte (ex.: 'Confissões')", max_length=200, verbose_name='Título')),
                ('subtitulo', models.CharField(blank=True, default='', help_text='Algumas obras apresentam subtítulos bastante elucidativos de seu conteúdo', max_length=200, null=True, verbose_name='Subtítulo')),
                ('resumo', models.TextField(blank=True, help_text='Uma breve descrição do conteúdo da obra.', null=True, verbose_name='Resumo')),
            ],
        ),
        migrations.RemoveField(
            model_name='livro',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='id',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='subtitulo',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='sumario',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='titulo',
        ),
        migrations.AlterField(
            model_name='autor',
            name='pseudonimo',
            field=models.CharField(blank=True, default='', help_text="Pseudonimo ou nome universal do autor. (ex.: 'Santo Agostinho')", max_length=100, null=True, verbose_name='Pseudônimo'),
        ),
        migrations.AddField(
            model_name='fonte',
            name='autor',
            field=models.ManyToManyField(help_text='Indique o autor ou autores da obra', to='catalogo.Autor', verbose_name='Autoria'),
        ),
        migrations.AddField(
            model_name='livro',
            name='fonte_ptr',
            field=models.OneToOneField(auto_created=True, default=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='catalogo.Fonte'),
            preserve_default=False,
        ),
    ]
