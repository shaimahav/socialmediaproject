# Generated by Django 3.2.25 on 2024-11-20 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='posted_by',
            field=models.CharField(default='shaimah', max_length=100),
            preserve_default=False,
        ),
    ]