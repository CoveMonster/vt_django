# Generated by Django 2.1.2 on 2018-10-10 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=50)),
                ('source_file_path', models.CharField(max_length=100)),
                ('timestamp', models.BooleanField(default=False)),
                ('status', models.IntegerField(default=-1)),
                ('failure_reason', models.CharField(max_length=100)),
                ('json_file_path', models.CharField(max_length=100)),
                ('objectFile_Timestamp_Path', models.CharField(max_length=100)),
                ('objectFile_Contend_path', models.CharField(max_length=100)),
                ('create_time', models.DateField(auto_now_add=True)),
                ('update_time', models.DateField(blank=True, null=True)),
                ('download_num', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('loginDate', models.DateField(auto_now_add=True)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='files',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vt_App.User'),
        ),
    ]
