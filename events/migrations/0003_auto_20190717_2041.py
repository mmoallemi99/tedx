# Generated by Django 2.2.3 on 2019-07-17 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='', help_text='link to event', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='year',
            field=models.IntegerField(blank=True, choices=[(2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], default=2019, help_text='year that event is being held', null=True),
        ),
    ]
