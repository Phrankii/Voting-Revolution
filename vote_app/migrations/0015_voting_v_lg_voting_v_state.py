# Generated by Django 4.1.3 on 2023-04-20 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote_app', '0014_voting_candidate_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='v_lg',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='voting',
            name='v_state',
            field=models.CharField(default=False, max_length=100),
        ),
    ]
