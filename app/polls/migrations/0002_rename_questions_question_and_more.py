# Generated by Django 4.2.7 on 2023-11-06 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='questions_text',
            new_name='question_text',
        ),
    ]