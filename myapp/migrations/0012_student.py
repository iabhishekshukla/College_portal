# Generated by Django 4.2.3 on 2023-08-08 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_delete_student_remove_course_id_course_course_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=45)),
                ('phone', models.CharField(max_length=10)),
                ('student_id', models.CharField(default='', max_length=40, primary_key=True, serialize=False)),
                ('student_password', models.CharField(max_length=40)),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=6)),
                ('description', models.TextField()),
                ('address', models.TextField()),
                ('student_pic', models.FileField(default='', max_length=200, upload_to='myapp/student_pic')),
                ('course', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.course')),
            ],
        ),
    ]
