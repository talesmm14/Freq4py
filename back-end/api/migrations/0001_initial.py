# Generated by Django 4.0 on 2021-12-15 16:28

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('afternoon_entry_time', models.TimeField(blank=True, null=True)),
                ('afternoon_departure_time', models.TimeField(blank=True, null=True)),
                ('morning_entry_time', models.TimeField(blank=True, null=True)),
                ('morning_departure_time', models.TimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='SheetValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_value_1', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('field_value_2', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('field_value_3', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('field_value_4', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('field_value_5', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('field_value_6', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('field_value_7', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('field_value_8', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='SheetTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('field_title_1', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('field_title_2', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('field_title_3', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('field_title_4', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('field_title_5', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('field_title_6', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('field_title_7', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('field_title_8', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('img_path', models.ImageField(blank=True, height_field=2.67, null=True, upload_to='img_sheet', width_field=6.94)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customuser')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.schedule')),
                ('titles_fields', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sheettitle')),
                ('values_fields', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.sheetvalue')),
            ],
        ),
        migrations.CreateModel(
            name='NotWorkType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=40, verbose_name='Nome')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='NotWorkingDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customuser')),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.notworktype')),
                ('sheet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.sheet')),
            ],
        ),
    ]
