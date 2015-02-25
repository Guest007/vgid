# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import core.models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=500, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('is_publish', models.BooleanField(default=False, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d\u043e?')),
                ('description', ckeditor.fields.RichTextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('text', ckeditor.fields.RichTextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442', blank=True)),
                ('geo', models.CharField(default=b'', help_text='\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b \u0434\u043b\u044f \u043f\u043e\u043a\u0430\u0437\u0430 \u043d\u0430 \u043a\u0430\u0440\u0442\u0435', max_length=50, verbose_name='\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b', blank=True)),
                ('meta_title', models.CharField(help_text='meta tag title \u043d\u0435 \u0434\u043b\u0438\u043d\u043d\u0435\u0435 80 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432', max_length=80, verbose_name='\u041c\u0435\u0442\u0430-\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True)),
                ('meta_description', models.CharField(help_text='meta tag description \u043d\u0435 \u0434\u043b\u0438\u043d\u043d\u0435\u0435 200 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432', max_length=200, verbose_name='\u041c\u0435\u0442\u0430-\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('meta_keyword', models.CharField(help_text='meta tag keyword \u043d\u0435 \u0434\u043b\u0438\u043d\u043d\u0435\u0435 250 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432', max_length=250, verbose_name='\u041a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430', blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=core.models.get_file_name, null=True, verbose_name='Image', blank=True)),
                ('is_history', models.BooleanField(default=False, help_text='\u0418\u0441\u0442\u043e\u0440\u0438\u044f - \u0434\u0430, \u041d\u043e\u0432\u043e\u0441\u0442\u0438 - \u043d\u0435\u0442', verbose_name='\u0418\u0441\u0442\u043e\u0440\u0438\u044f')),
                ('event', models.ForeignKey(to='events.Event', blank=True)),
                ('gallery', models.ManyToManyField(to='core.Gallery', null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u041d\u043e\u0432\u043e\u0441\u0442\u044c',
                'verbose_name_plural': '\u041d\u043e\u0432\u043e\u0441\u0442\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=500, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name='Modified')),
            ],
            options={
                'verbose_name': '\u0420\u0430\u0437\u0434\u0435\u043b',
                'verbose_name_plural': '\u0420\u0430\u0437\u0434\u0435\u043b\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='history',
            name='section',
            field=models.ForeignKey(to='history.Section', blank=True),
            preserve_default=True,
        ),
    ]
