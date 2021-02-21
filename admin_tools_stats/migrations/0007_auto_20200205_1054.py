# Generated by Django 2.2.10 on 2020-02-05 09:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_tools_stats', '0006_auto_20200205_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboardstats',
            name='criteria',
        ),
        migrations.AlterField(
            model_name='criteriatostatsm2m',
            name='criteria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_tools_stats.DashboardStatsCriteria'),
        ),
        migrations.AlterField(
            model_name='criteriatostatsm2m',
            name='stats',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_tools_stats.DashboardStats'),
        ),
        migrations.AlterField(
            model_name='dashboardstats',
            name='criteria_new',
            field=models.ManyToManyField(blank=True, through='admin_tools_stats.CriteriaToStatsM2M', to='admin_tools_stats.DashboardStatsCriteria'),
        ),
        migrations.RenameField(
            model_name='dashboardstats',
            old_name='criteria_new',
            new_name='criteria',
        ),
        migrations.RemoveField(
            model_name='dashboardstatscriteria',
            name='use_as',
        ),
        migrations.AlterField(
            model_name='criteriatostatsm2m',
            name='prefix',
            field=models.CharField(blank=True, default='', help_text='prefix, that will be added befor all lookup paths of criteria', max_length=255, verbose_name='criteria field prefix'),
        ),
    ]
