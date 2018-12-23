# Generated by Django 2.1 on 2018-12-22 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0007_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='status.Department'),
        ),
        migrations.AlterField(
            model_name='department',
            name='deaprtmentname',
            field=models.CharField(max_length=100),
        ),
    ]
