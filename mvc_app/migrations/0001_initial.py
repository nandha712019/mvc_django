# Generated by Django 3.2.5 on 2021-07-21 06:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('Media_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Media_link', models.FileField(default='', unique=True, upload_to='uploads/')),
                ('Media_type', models.CharField(choices=[('Audio', 'Audio'), ('Video', 'Video')], default='Audio', max_length=20, verbose_name='Media_type')),
                ('Title', models.TextField(default='', max_length=50)),
                ('Description', models.TextField(default='', max_length=300)),
                ('Thumbnail', models.ImageField(default='', upload_to='uploads/')),
                ('created_on', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Media_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mvc_app.media')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'Media_id')},
            },
        ),
    ]
