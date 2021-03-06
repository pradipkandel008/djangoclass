# Generated by Django 3.2.5 on 2022-05-08 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=3000)),
                ('image', models.ImageField(upload_to='static/uploads')),
            ],
        ),
    ]
