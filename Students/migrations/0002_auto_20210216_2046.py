# Generated by Django 3.0 on 2021-02-16 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='behaviorgrade',
            name='studentName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Students.MemberStudent'),
        ),
    ]