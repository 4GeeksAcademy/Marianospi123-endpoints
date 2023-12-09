"""empty message

Revision ID: a7fb854f0920
Revises: c4434ae83a89
Create Date: 2023-12-09 17:12:30.474244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7fb854f0920'
down_revision = 'c4434ae83a89'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('poblation', sa.String(length=80), nullable=False))
        batch_op.drop_column('population')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('population', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
        batch_op.drop_column('poblation')

    # ### end Alembic commands ###