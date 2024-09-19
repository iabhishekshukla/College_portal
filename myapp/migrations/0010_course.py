# Generated by Django 4.2.3 on 2023-08-08 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_fees', models.IntegerField()),
                ('course_duration', models.CharField(max_length=40)),
                ('course_contents', models.TextField(blank=True)),
                ('course_pic', models.FileField(default='', max_length=200, upload_to='myapp/course_pic')),
            ],
        ),
    ]
