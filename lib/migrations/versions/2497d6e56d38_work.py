"""work

Revision ID: 2497d6e56d38
Revises: 65f30c57973a
Create Date: 2023-03-28 11:08:58.472842

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2497d6e56d38'
down_revision = '65f30c57973a'
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
