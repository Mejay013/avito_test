# Generated by Django 3.1.1 on 2020-09-26 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_link', models.CharField(max_length=200)),
                ('new_link', models.CharField(max_length=200)),
            ],
        ),
    ]