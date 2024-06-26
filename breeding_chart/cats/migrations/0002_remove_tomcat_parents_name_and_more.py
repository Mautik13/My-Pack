# Generated by Django 5.0.6 on 2024-06-18 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tomcat',
            name='parents_name',
        ),
        migrations.RemoveField(
            model_name='kitten',
            name='parents_name',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='parents_name',
        ),
        migrations.AddField(
            model_name='cat',
            name='fathers_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='mothers_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='kitten',
            name='fathers_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='kitten',
            name='mothers_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tomcat',
            name='fathers_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tomcat',
            name='mothers_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='white_mottle_code',
            field=models.CharField(choices=[('01', 'from - 01'), ('02', 'harlequin - 02'), ('03', 'bicolor - 03'), ('09', 'with unspecified white spots - 09'), ('None', 'None')], default=None, max_length=4),
        ),
        migrations.DeleteModel(
            name='Parent',
        ),
    ]
