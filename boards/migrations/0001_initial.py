# Generated by Django 4.0.1 on 2022-01-14 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('type', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'boards',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('img_url', models.CharField(max_length=2048)),
                ('type', models.CharField(max_length=64)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.board')),
            ],
            options={
                'db_table': 'images',
            },
        ),
    ]
