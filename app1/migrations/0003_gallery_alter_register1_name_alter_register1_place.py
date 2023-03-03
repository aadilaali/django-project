# Generated by Django 4.1.6 on 2023-02-06 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_register1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=15)),
                ('Brand', models.CharField(max_length=15)),
                ('Model', models.CharField(max_length=15)),
                ('Price', models.IntegerField()),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.AlterField(
            model_name='register1',
            name='Name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='register1',
            name='Place',
            field=models.CharField(max_length=15),
        ),
    ]
