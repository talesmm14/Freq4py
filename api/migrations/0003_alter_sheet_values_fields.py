# Generated by Django 3.2.8 on 2021-10-25 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_sheet_not_working_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='values_fields',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.sheet_value'),
        ),
    ]