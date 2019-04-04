# Generated by Django 2.1.3 on 2019-04-03 23:36

import content.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20181201_0026'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('name_ar', models.CharField(max_length=150)),
                ('age_rating', models.CharField(max_length=3)),
                ('difficulty', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5, 'Maximum Limit is 5')])),
            ],
        ),
        migrations.CreateModel(
            name='QuestionTmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('name_ar', models.CharField(blank=True, max_length=150, null=True)),
                ('age_rating', models.CharField(max_length=3)),
                ('Correct_answer', models.CharField(blank=True, max_length=150, null=True)),
                ('creator_id', models.CharField(max_length=150)),
                ('difficulty', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5, 'Maximum Limit is 5')])),
                ('question_image', models.ImageField(blank=True, null=True, upload_to=content.models.get_image_path)),
                ('is_approved', models.BooleanField(default=False)),
                ('disapproved', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_ar',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='name_ar',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='questiontmp',
            name='Category_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.Category'),
        ),
    ]