# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('about_menu', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'aboutmenu',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticleSecondAbout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('articleSecondAbout_body', models.TextField()),
                ('articleSecondAbout_author', models.TextField()),
            ],
            options={
                'db_table': 'articlesecondabout',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticleSecondHome',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('articleSecodHome_title', models.CharField(max_length=200)),
                ('articleSecondHome_body', models.TextField()),
            ],
            options={
                'db_table': 'mainarticlesecondhome',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BanerHome',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('banerhome_title', models.CharField(max_length=50)),
                ('banerHome_body', models.CharField(max_length=100)),
                ('banerHome_images', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'banerhome',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_map_title', models.CharField(max_length=150)),
                ('contact_article', models.TextField()),
                ('contact_adress_index', models.CharField(max_length=150)),
                ('contact_adress_city', models.CharField(max_length=150)),
                ('contact_adress_street', models.CharField(max_length=150)),
                ('contact_adress_office', models.CharField(max_length=150)),
                ('contact_adress_telephone', models.CharField(max_length=150)),
                ('contact_adress_mob', models.CharField(max_length=150)),
                ('contact_adress_email', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'contact',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feedback_name', models.CharField(max_length=200)),
                ('feedback_email', models.CharField(max_length=200)),
                ('feedback_phone', models.CharField(max_length=200)),
                ('feedback_text', models.TextField()),
            ],
            options={
                'db_table': 'feedback',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FooterBar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('footer_bar', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'footer',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LinkAbout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('linkabout', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'linkabout',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MainArticleAbout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mainArticleAbout_title', models.CharField(max_length=200)),
                ('mainArticleAbout_body', models.TextField()),
            ],
            options={
                'db_table': 'mainarticleabout',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MainArticleHome',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mainArticleHome_title', models.CharField(max_length=200)),
                ('mainArticleHome_body', models.TextField()),
            ],
            options={
                'db_table': 'mainarticlehome',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NavbarMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('navbar_menu', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'navbarmenu',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('poduct_slogan', models.CharField(max_length=100)),
                ('poductNameImages', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'product',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_slogan', models.CharField(max_length=100)),
                ('projectArticle_title', models.CharField(max_length=100)),
                ('projectArticle_preview', models.CharField(max_length=200)),
                ('projectArticle_body', models.TextField()),
            ],
            options={
                'db_table': 'project',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SloganHome',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sloganHome_title', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'sloganhome',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TitleArticleHome',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titleArticleHome_title', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'titlearticlehome',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TitleTeamAbout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titleTeamAbout', models.CharField(max_length=30)),
                ('titlePeople', models.CharField(max_length=50)),
                ('titlePeople_body', models.TextField()),
            ],
            options={
                'db_table': 'titleteamabout',
            },
            bases=(models.Model,),
        ),
    ]
