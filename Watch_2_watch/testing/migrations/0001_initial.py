# Generated by Django 3.2.12 on 2022-04-12 17:09

import Watch_2_watch.testing.validator
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production_year', models.PositiveIntegerField(validators=[Watch_2_watch.testing.validator.prod_year_validator])),
            ],
        ),
    ]
