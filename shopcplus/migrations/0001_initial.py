# Generated by Django 3.1.5 on 2022-03-19 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='aj', max_length=100)),
                ('password', models.CharField(default='cm', max_length=100)),
            ],
        ),
    ]
