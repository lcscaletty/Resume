# Generated by Django 5.2 on 2025-04-18 18:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leoscaletty', '0002_bullet'),
    ]

    operations = [
        migrations.CreateModel(
            name='moreInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leoscaletty.bullet')),
            ],
        ),
    ]
