"""create tables

Revision ID: 381db56b812d
Revises: 
Create Date: 2021-02-17 16:05:25.763177

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '381db56b812d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('job_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_job_categories_category'), 'job_categories', ['category'], unique=False)
    op.create_index(op.f('ix_job_categories_id'), 'job_categories', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_job_categories_id'), table_name='job_categories')
    op.drop_index(op.f('ix_job_categories_category'), table_name='job_categories')
    op.drop_table('job_categories')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
