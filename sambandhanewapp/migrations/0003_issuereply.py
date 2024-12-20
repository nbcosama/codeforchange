# Generated by Django 5.1.3 on 2024-12-13 08:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sambandhanewapp', '0002_userissue'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('issueID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sambandhanewapp.userissue')),
                ('repliedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sambandhanewapp.useraccount')),
            ],
        ),
    ]
