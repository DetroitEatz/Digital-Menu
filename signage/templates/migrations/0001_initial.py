# Generated by Django 2.0.13 on 2019-05-07 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('archived', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, null=True)),
                ('template', models.FileField(blank=True, null=True, upload_to='templates/')),
            ],
            options={
                'db_table': 'templates',
            },
        ),
    ]
