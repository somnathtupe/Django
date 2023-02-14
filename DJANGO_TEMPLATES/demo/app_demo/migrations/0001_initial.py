# Generated by Django 4.1.4 on 2022-12-12 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allcourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=200)),
                ('insename', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='detalis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp', models.CharField(max_length=200)),
                ('il', models.CharField(max_length=200)),
                ('couse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_demo.allcourse')),
            ],
        ),
    ]