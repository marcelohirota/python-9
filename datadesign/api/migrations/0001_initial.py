# Generated by Django 3.0.6 on 2020-06-17 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('status', models.BooleanField(verbose_name='Status')),
                ('env', models.CharField(max_length=20, verbose_name='Env')),
                ('version', models.CharField(max_length=5, verbose_name='Version')),
                ('address', models.GenericIPAddressField(verbose_name='IP Address')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='Último login')),
                ('email', models.CharField(max_length=254, verbose_name='E-mail')),
                ('password', models.CharField(max_length=50, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='GroupUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Group')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=20, verbose_name='Level')),
                ('data', models.TextField(verbose_name='Data')),
                ('arquivado', models.BooleanField(verbose_name='Arquivado')),
                ('date', models.DateField(auto_now=True, verbose_name='Date')),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Agent')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
        ),
    ]
