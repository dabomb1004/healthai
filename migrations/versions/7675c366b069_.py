"""empty message

Revision ID: 7675c366b069
Revises: da61f4ab70c3
Create Date: 2021-04-18 21:56:55.847157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7675c366b069'
down_revision = 'da61f4ab70c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('heart_disease_prediction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Age', sa.Integer(), nullable=True),
    sa.Column('Gender', sa.Integer(), nullable=True),
    sa.Column('ChestPain', sa.Integer(), nullable=True),
    sa.Column('BloodPressure', sa.Integer(), nullable=True),
    sa.Column('ElectrocardiographicResults', sa.Integer(), nullable=True),
    sa.Column('MaxHeartRate', sa.Integer(), nullable=True),
    sa.Column('ExerciseInducedAngina', sa.Integer(), nullable=True),
    sa.Column('STdepression', sa.Integer(), nullable=True),
    sa.Column('ExercisePeakSlope', sa.Integer(), nullable=True),
    sa.Column('MajorVesselsNo', sa.Integer(), nullable=True),
    sa.Column('Thalassemia', sa.Integer(), nullable=True),
    sa.Column('prediction', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('heart_disease_prediction')
    # ### end Alembic commands ###
