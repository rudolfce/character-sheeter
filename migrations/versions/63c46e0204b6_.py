"""empty message

Revision ID: 63c46e0204b6
Revises: 19703e18f707
Create Date: 2021-01-22 15:33:44.978429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63c46e0204b6'
down_revision = '19703e18f707'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('layout', sa.Column('field_mapping', sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('layout', 'field_mapping')
    # ### end Alembic commands ###
