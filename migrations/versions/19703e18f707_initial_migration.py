"""Initial migration.

Revision ID: 19703e18f707
Revises: 
Create Date: 2020-03-29 10:04:22.523925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19703e18f707'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('layout',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('structure', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sheet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('sheet_data', sa.JSON(), nullable=True),
    sa.Column('layout_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['layout_id'], ['layout.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sheet')
    op.drop_table('layout')
    # ### end Alembic commands ###
