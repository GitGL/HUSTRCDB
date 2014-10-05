# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
            ],
            options={
                'db_table': 'Brands',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Build',
            fields=[
            ],
            options={
                'db_table': 'Builds',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
            ],
            options={
                'db_table': 'Events',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Maintenancerecord',
            fields=[
            ],
            options={
                'db_table': 'MaintenanceRecords',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
            ],
            options={
                'db_table': 'Problems',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Projector',
            fields=[
            ],
            options={
                'db_table': 'Projectors',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Projectorstate',
            fields=[
            ],
            options={
                'db_table': 'view_projector_state',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
            ],
            options={
                'db_table': 'Rooms',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
            ],
            options={
                'db_table': 'Status',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Statusrecord',
            fields=[
            ],
            options={
                'db_table': 'StatusRecords',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
