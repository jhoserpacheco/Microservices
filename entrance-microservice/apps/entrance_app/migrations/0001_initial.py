# Generated by Django 4.0.4 on 2022-05-16 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('group_id', models.IntegerField()),
                ('entrance_time', models.DateTimeField(auto_now_add=True)),
                ('exit_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LogDateHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrance_time_range', models.DateTimeField(auto_now_add=True)),
                ('exit_time_range', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('group_id', models.IntegerField()),
                ('key', models.CharField(max_length=255)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('log_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entrance_app.log')),
            ],
        ),
        migrations.CreateModel(
            name='LogHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('group_id', models.IntegerField()),
                ('entrance_time', models.DateTimeField(auto_now_add=True)),
                ('exit_time', models.DateTimeField(null=True)),
                ('logs_date_history_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrance_app.logdatehistory')),
            ],
        ),
    ]
