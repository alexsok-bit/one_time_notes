# Generated by Django 3.1.1 on 2020-09-03 09:04

import dropnote.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SnippetItem',
            fields=[
                ('id', dropnote.models.TokenField(default=dropnote.models.TokenField.make_new, editable=False, max_length=6, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]