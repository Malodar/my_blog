# Generated by Django 2.1 on 2019-10-31 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('programming', 'Programming'), ('life_in_usa', 'Live in USA'), ('other', 'Other')], default='other', max_length=30),
        ),
    ]
