"""empty message

Revision ID: 14589b06218c
Revises: 1f86c3289c10
Create Date: 2022-03-20 19:20:30.928324

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '14589b06218c'
down_revision = '1f86c3289c10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('title', sa.String(length=160), nullable=False),
    sa.Column('bedrooms', sa.Integer(), nullable=True),
    sa.Column('bathrooms', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(length=80), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('proptype', sa.String(length=80), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('img', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('title')
    )
    op.drop_table('Properties')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Properties',
    sa.Column('title', sa.VARCHAR(length=160), autoincrement=False, nullable=False),
    sa.Column('bedrooms', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('bathrooms', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('location', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('price', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('proptype', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('img', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('title', name='Properties_pkey')
    )
    op.drop_table('properties')
    # ### end Alembic commands ###
