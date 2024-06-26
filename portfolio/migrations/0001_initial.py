# Generated by Django 5.0.6 on 2024-06-10 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('phone1', models.CharField(max_length=250)),
                ('phone2', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=250)),
                ('degree', models.CharField(max_length=250)),
                ('field_of_study', models.CharField(max_length=250)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('middle_name', models.CharField(blank=True, max_length=250, null=True)),
                ('last_name', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('about_me', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(max_length=250)),
                ('profile_photo', models.ImageField(upload_to='profile/')),
                ('cv', models.FileField(upload_to='cv/')),
                ('years_of_experience', models.CharField(max_length=250)),
                ('happy_clients', models.CharField(max_length=250)),
                ('github', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('google', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True)),
                ('project_info', models.TextField()),
                ('client', models.CharField(max_length=250)),
                ('industry', models.CharField(max_length=250)),
                ('technology', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('url', models.URLField()),
                ('image1', models.ImageField(upload_to='project/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='project/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='project/')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=250)),
                ('icon_class', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('level_of_expertise', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('company_name', models.CharField(max_length=250)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('current_job', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
