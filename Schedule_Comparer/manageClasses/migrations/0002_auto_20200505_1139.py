# Generated by Django 3.0.5 on 2020-05-05 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageClasses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='afterSchool',
        ),
        migrations.CreateModel(
            name='AfterSchoolActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('students', models.ManyToManyField(to='manageClasses.Student')),
                ('teachers', models.ManyToManyField(to='manageClasses.Teacher')),
            ],
        ),
    ]
