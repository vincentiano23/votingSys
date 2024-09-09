# Generated by Django 5.1.1 on 2024-09-09 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0002_vote_delete_voter_alter_candidate_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('has_voted', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
