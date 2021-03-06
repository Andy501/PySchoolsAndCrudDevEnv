# Generated by Django 3.0 on 2021-02-11 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Doe', max_length=50)),
                ('age', models.IntegerField(default=99)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teacher.Teachers')),
            ],
        ),
        migrations.CreateModel(
            name='BehaviorGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventGrade', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('F', 'F')], max_length=1)),
                ('eventSeverity', models.CharField(choices=[('Bad', 'Bad Behavior'), ('Good', 'Good Behavior'), ('Danger', 'Dangerous')], max_length=15)),
                ('eventTitle', models.CharField(max_length=15)),
                ('eventDescription', models.TextField()),
                ('studentName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Students.MemberStudent')),
            ],
        ),
    ]
