# Generated by Django 5.1.1 on 2024-09-23 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_classes'),
        ('students', '0002_rename_student_students'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Classes',
            new_name='Class101',
        ),
        migrations.RenameModel(
            old_name='Courses',
            new_name='Course',
        ),
    ]
