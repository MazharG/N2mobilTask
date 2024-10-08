# Generated by Django 5.1.1 on 2024-09-18 20:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('suite', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Geo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('thumbnail_url', models.URLField()),
                ('albumId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='task.albums')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('postId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='task.posts')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=17)),
                ('website', models.CharField(max_length=100)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='task.address')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='task.company')),
                ('geo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='task.geo')),
            ],
        ),
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('completed', models.BooleanField(default=False)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todos', to='task.users')),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='task.users'),
        ),
        migrations.AddField(
            model_name='albums',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='task.users'),
        ),
    ]
