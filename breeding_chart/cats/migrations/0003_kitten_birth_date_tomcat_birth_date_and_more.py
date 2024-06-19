# Generated by Django 5.0.6 on 2024-06-18 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0002_remove_tomcat_parents_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitten',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tomcat',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='drawing_code',
            field=models.CharField(choices=[('11', 'shaded - 11'), ('12', 'shell - 12'), ('21', 'unspecified drawing - 21'), ('22', 'marble drawing (blotched - 22)'), ('23', 'tiger drawing (mackerel - 23)'), ('24', 'dot drawing (spotted - 24)'), ('25', 'ticked drawing (ticked - 25)'), ('None', 'None')], default='None', max_length=4),
        ),
        migrations.AlterField(
            model_name='color',
            name='white_mottle_code',
            field=models.CharField(choices=[('01', 'from - 01'), ('02', 'harlequin - 02'), ('03', 'bicolor - 03'), ('09', 'with unspecified white spots - 09'), ('None', 'None')], default='None', max_length=4),
        ),
    ]