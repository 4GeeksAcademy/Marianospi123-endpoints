"""empty message

Revision ID: c4434ae83a89
Revises: ad82b7b51a5f
Create Date: 2023-12-08 16:05:48.375820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4434ae83a89'
down_revision = 'ad82b7b51a5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('population', sa.String(length=80), nullable=False))
        batch_op.drop_column('poblation')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('poblation', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
        batch_op.drop_column('population')

    # ### end Alembic commands ###