# Generated by Django 4.2.7 on 2023-11-06 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(auto_created=True, verbose_name='date published'),
        ),
    ]
