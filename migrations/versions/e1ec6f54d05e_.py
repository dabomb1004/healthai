"""empty message

Revision ID: e1ec6f54d05e
Revises: 97c2a4a60481
Create Date: 2021-04-25 18:42:19.285538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1ec6f54d05e'
down_revision = '97c2a4a60481'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('breast_cancer', sa.Column('compactness_mean', sa.Float(precision=9), nullable=True))
    op.add_column('breast_cancer', sa.Column('compactness_se', sa.Float(precision=9), nullable=True))
    op.add_column('breast_cancer', sa.Column('compactness_worst', sa.Float(precision=9), nullable=True))
    op.add_column('breast_cancer', sa.Column('concave_points_mean', sa.Float(precision=9), nullable=True))
    op.add_column('breast_cancer', sa.Column('concave_points_se', sa.Float(precision=9), nullable=True))
    op.add_column('breast_cancer', sa.Column('concave_points_worst', sa.Float(precision=9), nullable=True))
    op.add_column('breast_cancer', sa.Column('concavity_mean', sa.Float(precision=9), nullable=True))
    op.add_column('breast_cancer', sa.Column('concavity_se', sa.Float(precision=9), nullable=True))
    op.add_column('breast_cancer', sa.Column('concavity_worst', sa.Float(precision=9), nullable=True))
    op.add_column('breast_cancer', sa.Column('fractal_dimension_worst', sa.Float(precision=9), nullable=True))
    op.add_column('breast_cancer', sa.Column('perimeter_mean', sa.Float(precision=9), nullable=True))
    op.add_column('breast_cancer', sa.Column('radius_se', sa.Float(precision=9), nullable=True))
    op.add_column('breast_cancer', sa.Column('smoothness_mean', sa.Float(precision=9), nullable=True))
    op.add_column('breast_cancer', sa.Column('smoothness_worst', sa.Float(precision=9), nullable=True))
    op.add_column('breast_cancer', sa.Column('symmetry_mean', sa.Float(precision=9), nullable=True))
    op.add_column('breast_cancer', sa.Column('symmetry_worst', sa.Float(precision=9), nullable=True))
    op.add_column('breast_cancer', sa.Column('texture_worst', sa.Float(precision=9), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('breast_cancer', 'texture_worst')
    op.drop_column('breast_cancer', 'symmetry_worst')
    op.drop_column('breast_cancer', 'symmetry_mean')
    op.drop_column('breast_cancer', 'smoothness_worst')
    op.drop_column('breast_cancer', 'smoothness_mean')
    op.drop_column('breast_cancer', 'radius_se')
    op.drop_column('breast_cancer', 'perimeter_mean')
    op.drop_column('breast_cancer', 'fractal_dimension_worst')
    op.drop_column('breast_cancer', 'concavity_worst')
    op.drop_column('breast_cancer', 'concavity_se')
    op.drop_column('breast_cancer', 'concavity_mean')
    op.drop_column('breast_cancer', 'concave_points_worst')
    op.drop_column('breast_cancer', 'concave_points_se')
    op.drop_column('breast_cancer', 'concave_points_mean')
    op.drop_column('breast_cancer', 'compactness_worst')
    op.drop_column('breast_cancer', 'compactness_se')
    op.drop_column('breast_cancer', 'compactness_mean')
    # ### end Alembic commands ###
