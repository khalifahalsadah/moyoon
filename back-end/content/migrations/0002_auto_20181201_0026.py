# Generated by Django 2.1.3 on 2018-11-30 21:26

import content.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionimage',
            name='Question',
        ),
        migrations.AlterField(
            model_name='question',
            name='question_image',
            field=models.ImageField(blank=True, null=True, upload_to=content.models.get_image_path),
        ),
        migrations.DeleteModel(
            name='QuestionImage',
        ),
    ]
