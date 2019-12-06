# Generated by Django 2.2.3 on 2019-12-06 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20191206_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='role',
            field=models.CharField(blank=True, choices=[('Curation', 'curation'), ('Organizer', 'organizer'), ('Co Organizer', 'coorganizer'), ('Marketing', 'marketing'), ('Documentation', 'documentation'), ('Creativity', 'creativity'), ('Frontend Developer', 'frontend'), ('Backend Developer', 'backend'), ('UI Designer', 'designer')], default='others', help_text="team's way of association in team", max_length=30, null=True),
        ),
    ]
