# Generated by Django 2.1.1 on 2018-10-06 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nota', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etiqueta',
            name='cor',
            field=models.CharField(default='6A5ACD', help_text='A cor da etiqueta pode ajudar na visualização das anotações (use com sabedoria...)', max_length=6, verbose_name='Cor'),
        ),
    ]
