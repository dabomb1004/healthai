"""empty message

Revision ID: 18fa3a98459f
Revises: b79b6f937210
Create Date: 2021-04-24 21:28:35.905208

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18fa3a98459f'
down_revision = 'b79b6f937210'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('breast_cancer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('texture_mean', sa.Float(precision=9), nullable=True),
    sa.Column('perimeter_mean', sa.Float(precision=9), nullable=True),
    sa.Column('smoothness_mean', sa.Float(precision=9), nullable=True),
    sa.Column('compactness_mean', sa.Float(precision=9), nullable=True),
    sa.Column('concavity_mean', sa.Float(precision=9), nullable=True),
    sa.Column('concave_points_mean', sa.Float(precision=9), nullable=True),
    sa.Column('symmetry_mean', sa.Float(precision=9), nullable=True),
    sa.Column('radius_se', sa.Float(precision=9), nullable=True),
    sa.Column('compactness_se', sa.Float(precision=9), nullable=True),
    sa.Column('concavity_se', sa.Float(precision=9), nullable=True),
    sa.Column('concave_points_se', sa.Float(precision=9), nullable=True),
    sa.Column('texture_worst', sa.Float(precision=9), nullable=True),
    sa.Column('smoothness_worst', sa.Float(precision=9), nullable=True),
    sa.Column('compactness_worst', sa.Float(precision=9), nullable=True),
    sa.Column('concavity_worst', sa.Float(precision=9), nullable=True),
    sa.Column('concave_points_worst', sa.Float(precision=9), nullable=True),
    sa.Column('symmetry_worst', sa.Float(precision=9), nullable=True),
    sa.Column('fractal_dimension_worst', sa.Float(precision=9), nullable=True),
    sa.Column('prediction', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_breast_cancer_timestamp'), 'breast_cancer', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_breast_cancer_timestamp'), table_name='breast_cancer')
    op.drop_table('breast_cancer')
    # ### end Alembic commands ###
