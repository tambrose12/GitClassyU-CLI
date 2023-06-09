"""add data e>

Revision ID: c989156a671e
Revises: 1c04bdfb3235
Create Date: 2023-03-27 00:28:23.290447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c989156a671e'
down_revision = '1c04bdfb3235'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'students', 'courses', ['course_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'students', type_='foreignkey')
    # ### end Alembic commands ###
