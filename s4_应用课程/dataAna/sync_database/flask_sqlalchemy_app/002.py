# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019-06-03 20:24
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""


def upgrade():
    op.add_column(
        'dataset',
        sa.Column(
            'meta',
            postgresql.JSONB(),
            nullable=True
        )
    )
    op.execute('''
        UPDATE "dataset" SET
            meta = jsonb_set(coalesce(meta, '{}'), '{organization_id}', to_jsonb(organization_id))
        WHERE
            organization_id IS NOT NULL
    ''')
    op.drop_column('dataset', 'organization_id')



