"""merging heads maybe

Revision ID: 1b7c528476f5
Revises: 7b6c70371daf, 993148d9b081
Create Date: 2023-03-30 15:48:59.796211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b7c528476f5'
down_revision = ('7b6c70371daf', '993148d9b081')
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
