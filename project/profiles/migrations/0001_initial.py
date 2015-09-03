# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'stu', max_length=3, choices=[(b'css', b'Missouri S&T Computer Science Student'), (b'stu', b'Missouri S&T Student'), (b'fac', b'Missouri S&T Staff or Faculty'), (b'alm', b'Missour S&T Alumnus/Alumna')])),
                ('about_me', models.TextField(validators=[django.core.validators.MaxLengthValidator(500)])),
                ('rendered_about_me', models.TextField(editable=False)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
