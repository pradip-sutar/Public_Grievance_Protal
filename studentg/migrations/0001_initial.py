# Generated by Django 5.0.7 on 2024-07-22 16:49

import django.db.models.deletion
import studentg.constants
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('redressal', '0004_alter_department_id_alter_institute_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DayToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(default=0)),
                ('last_update', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Dept_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentg.department')),
            ],
        ),
        migrations.CreateModel(
            name='Grievance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('daytoken', models.IntegerField()),
                ('last_update', models.DateField(auto_now=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Draft'), (2, 'In Review'), (3, 'Pending'), (4, 'Resolved'), (5, 'Rejected')], default=2)),
                ('message', models.TextField(max_length=1000)),
                ('subject', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('state', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('block', models.CharField(max_length=255)),
                ('village', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentg.department')),
                ('redressal_body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grievances', to='redressal.redressalbody')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentg.dept_category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grievances', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-last_update'],
                'unique_together': {('date', 'daytoken')},
            },
            bases=(studentg.constants.StatusConstants, models.Model),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('grievance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='studentg.grievance')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(choices=[(5, '5 Stars'), (4, '4 Stars'), (3, '3 Stars'), (2, '2 Stars'), (1, '1 Star')])),
                ('grievance', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='studentg.grievance')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('pin', models.CharField(blank=True, max_length=10, null=True)),
                ('aadhaar', models.CharField(blank=True, max_length=12, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(max_length=1000)),
                ('grievance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='studentg.grievance')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Replies',
                'ordering': ['date_time'],
            },
        ),
    ]
