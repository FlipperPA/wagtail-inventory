# -*- coding: utf-8 -*-
from django.db import migrations

from wagtail.core import blocks as core_blocks
from wagtail.core import fields as core_fields  # pragma: no cover


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_nested_stream_block_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singlestreamfieldpage',
            name='content',
            field=core_fields.StreamField([('atom', core_blocks.StructBlock([('title', core_blocks.CharBlock())])), ('molecule', core_blocks.StructBlock([('title', core_blocks.CharBlock()), ('atoms', core_blocks.ListBlock(core_blocks.StructBlock([('title', core_blocks.CharBlock())])))])), ('organism', core_blocks.StructBlock([('molecules', core_blocks.ListBlock(core_blocks.StructBlock([('title', core_blocks.CharBlock()), ('atoms', core_blocks.ListBlock(core_blocks.StructBlock([('title', core_blocks.CharBlock())])))])))]))], blank=True),
        ),
    ]
