"""empty message

Revision ID: 02d4bebde76c
Revises: 1d04b91cd243
Create Date: 2021-04-05 07:42:31.861553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02d4bebde76c'
down_revision = '1d04b91cd243'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('db_day', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('db_month', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('db_year', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('first_name', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('last_name', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('phone', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('ssn', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('ssn_hash', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'ssn_hash')
    op.drop_column('user', 'ssn')
    op.drop_column('user', 'phone')
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    op.drop_column('user', 'db_year')
    op.drop_column('user', 'db_month')
    op.drop_column('user', 'db_day')
    # ### end Alembic commands ###