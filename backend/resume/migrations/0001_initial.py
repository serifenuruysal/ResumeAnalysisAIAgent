# Generated by Django 5.1.2 on 2024-10-16 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_file', models.FileField(upload_to='resumes/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
