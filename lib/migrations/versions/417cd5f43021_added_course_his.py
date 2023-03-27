"""added course his

Revision ID: 417cd5f43021
Revises: 262e6b620753
Create Date: 2023-03-27 00:04:37.537684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '417cd5f43021'
down_revision = '262e6b620753'
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