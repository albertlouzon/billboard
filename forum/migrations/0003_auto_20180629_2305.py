# Generated by Django 2.0.6 on 2018-06-29 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20180629_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message_forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', models.CharField(max_length=800)),
                ('author', models.CharField(max_length=800)),
            ],
        ),
        migrations.DeleteModel(
            name='Messages',
        ),
    ]