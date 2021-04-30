"""empty message

Revision ID: 4ed60e84cf8f
Revises: 99a4afeebd6e
Create Date: 2021-04-21 01:08:50.628010

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4ed60e84cf8f'
down_revision = '99a4afeebd6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'heart_disease_prediction_ibfk_1', 'heart_disease_prediction', type_='foreignkey')
    op.drop_column('heart_disease_prediction', 'BloodPressure')
    op.drop_column('heart_disease_prediction', 'ExerciseInducedAngina')
    op.drop_column('heart_disease_prediction', 'Gender')
    op.drop_column('heart_disease_prediction', 'prediction')
    op.drop_column('heart_disease_prediction', 'Thalassemia')
    op.drop_column('heart_disease_prediction', 'ElectrocardiographicResults')
    op.drop_column('heart_disease_prediction', 'MajorVesselsNo')
    op.drop_column('heart_disease_prediction', 'MaxHeartRate')
    op.drop_column('heart_disease_prediction', 'STdepression')
    op.drop_column('heart_disease_prediction', 'user_id')
    op.drop_column('heart_disease_prediction', 'ChestPain')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('heart_disease_prediction', sa.Column('ChestPain', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('heart_disease_prediction', sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('heart_disease_prediction', sa.Column('STdepression', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('heart_disease_prediction', sa.Column('MaxHeartRate', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('heart_disease_prediction', sa.Column('MajorVesselsNo', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('heart_disease_prediction', sa.Column('ElectrocardiographicResults', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('heart_disease_prediction', sa.Column('Thalassemia', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('heart_disease_prediction', sa.Column('prediction', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('heart_disease_prediction', sa.Column('Gender', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('heart_disease_prediction', sa.Column('ExerciseInducedAngina', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('heart_disease_prediction', sa.Column('BloodPressure', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key(u'heart_disease_prediction_ibfk_1', 'heart_disease_prediction', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###