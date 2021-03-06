# Generated by Django 3.1.3 on 2020-12-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('KFUPMCollection', '0002_dep'),
    ]

    operations = [
        migrations.CreateModel(
            name='answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AID', models.CharField(max_length=250)),
                ('Rate', models.CharField(max_length=250)),
                ('QID', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'answer',
            },
        ),
        migrations.CreateModel(
            name='contains',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QID', models.CharField(max_length=250)),
                ('EID', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'contains',
            },
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('CID', models.CharField(max_length=250)),
                ('prerequisites', models.CharField(max_length=250)),
                ('DID', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='dep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('icon', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('icon', models.CharField(max_length=250)),
                ('DID', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EID', models.CharField(max_length=250)),
                ('comments', models.CharField(max_length=250)),
                ('E_Date', models.CharField(max_length=250)),
                ('SID', models.CharField(max_length=250)),
                ('IID', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'evaluation',
            },
        ),
        migrations.CreateModel(
            name='instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('IID', models.CharField(max_length=250)),
                ('Office_Phone_number', models.CharField(max_length=250)),
                ('Email', models.CharField(max_length=250)),
                ('Office_location', models.CharField(max_length=250)),
                ('website', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'instructor',
            },
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QID', models.CharField(max_length=250)),
                ('Qname', models.CharField(max_length=250)),
                ('Weight', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'question',
            },
        ),
    ]
