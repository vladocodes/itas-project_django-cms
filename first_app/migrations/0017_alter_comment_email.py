# Generated by Django 3.2 on 2021-05-31 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0016_alter_comment_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
