# Generated by Django 3.1 on 2020-08-31 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pages',
            options={'ordering': ['order', 'title'], 'verbose_name': 'pagina', 'verbose_name_plural': 'Paginas'},
        ),
        migrations.AddField(
            model_name='pages',
            name='order',
            field=models.SmallIntegerField(default=0, verbose_name='orden'),
        ),
    ]
