# Generated by Django 4.1 on 2022-08-22 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default=True, max_length=20)),
                ('lname', models.CharField(default=True, max_length=20)),
                ('email', models.EmailField(default=True, max_length=254)),
                ('pas', models.CharField(default=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=True, max_length=20)),
                ('details', models.CharField(default=True, max_length=200)),
                ('image', models.ImageField(default=True, upload_to='image/')),
                ('email', models.EmailField(default=True, max_length=254)),
                ('publish', models.CharField(default=True, max_length=20)),
                ('user_id', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='blog.student')),
            ],
        ),
    ]