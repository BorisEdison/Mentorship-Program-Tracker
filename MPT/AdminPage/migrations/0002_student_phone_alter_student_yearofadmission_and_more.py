# Generated by Django 4.0.4 on 2022-06-03 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='YearOfAdmission',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='current_RollNo',
            field=models.IntegerField(null=True),
        ),
    ]