"""empty message

Revision ID: 97c2a4a60481
Revises: 18fa3a98459f
Create Date: 2021-04-25 18:39:07.003965

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '97c2a4a60481'
down_revision = '18fa3a98459f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('breast_cancer', 'concavity_worst')
    op.drop_column('breast_cancer', 'radius_se')
    op.drop_column('breast_cancer', 'perimeter_mean')
    op.drop_column('breast_cancer', 'concave_points_worst')
    op.drop_column('breast_cancer', 'compactness_se')
    op.drop_column('breast_cancer', 'concave_points_se')
    op.drop_column('breast_cancer', 'concavity_mean')
    op.drop_column('breast_cancer', 'symmetry_mean')
    op.drop_column('breast_cancer', 'concave_points_mean')
    op.drop_column('breast_cancer', 'smoothness_worst')
    op.drop_column('breast_cancer', 'symmetry_worst')
    op.drop_column('breast_cancer', 'fractal_dimension_worst')
    op.drop_column('breast_cancer', 'smoothness_mean')
    op.drop_column('breast_cancer', 'concavity_se')
    op.drop_column('breast_cancer', 'compactness_mean')
    op.drop_column('breast_cancer', 'texture_worst')
    op.drop_column('breast_cancer', 'compactness_worst')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('breast_cancer', sa.Column('compactness_worst', mysql.FLOAT(), nullable=True))
    op.add_column('breast_cancer', sa.Column('texture_worst', mysql.FLOAT(), nullable=True))
    op.add_column('breast_cancer', sa.Column('compactness_mean', mysql.FLOAT(), nullable=True))
    op.add_column('breast_cancer', sa.Column('concavity_se', mysql.FLOAT(), nullable=True))
    op.add_column('breast_cancer', sa.Column('smoothness_mean', mysql.FLOAT(), nullable=True))
    op.add_column('breast_cancer', sa.Column('fractal_dimension_worst', mysql.FLOAT(), nullable=True))
    op.add_column('breast_cancer', sa.Column('symmetry_worst', mysql.FLOAT(), nullable=True))
    op.add_column('breast_cancer', sa.Column('smoothness_worst', mysql.FLOAT(), nullable=True))
    op.add_column('breast_cancer', sa.Column('concave_points_mean', mysql.FLOAT(), nullable=True))
    op.add_column('breast_cancer', sa.Column('symmetry_mean', mysql.FLOAT(), nullable=True))
    op.add_column('breast_cancer', sa.Column('concavity_mean', mysql.FLOAT(), nullable=True))
    op.add_column('breast_cancer', sa.Column('concave_points_se', mysql.FLOAT(), nullable=True))
    op.add_column('breast_cancer', sa.Column('compactness_se', mysql.FLOAT(), nullable=True))
    op.add_column('breast_cancer', sa.Column('concave_points_worst', mysql.FLOAT(), nullable=True))
    op.add_column('breast_cancer', sa.Column('perimeter_mean', mysql.FLOAT(), nullable=True))
    op.add_column('breast_cancer', sa.Column('radius_se', mysql.FLOAT(), nullable=True))
    op.add_column('breast_cancer', sa.Column('concavity_worst', mysql.FLOAT(), nullable=True))
    # ### end Alembic commands ###
