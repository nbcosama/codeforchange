# Generated by Django 5.1.3 on 2024-12-14 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sambandhanewapp', '0006_feedback_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='type',
            field=models.CharField(choices=[('issue', 'Issue'), ('reply', 'Reply'), ('comment', 'Comment'), ('reComment', 'Re-Comment'), ('mitra', 'Mitra')], max_length=100),
        ),
    ]