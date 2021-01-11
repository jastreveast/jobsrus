"""empty message

Revision ID: 83ce2d82a85d
Revises: 
Create Date: 2020-11-12 19:37:32.143402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83ce2d82a85d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=100), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('company', sa.String(length=255), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('requirements', sa.String(), nullable=True),
    sa.Column('qualifications', sa.String(), nullable=True),
    sa.Column('salary', sa.String(), nullable=True),
    sa.Column('application', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('job')
    # ### end Alembic commands ###
