"""empty message

Revision ID: dd176628c3e8
Revises: 55a14cec9183
Create Date: 2024-07-18 12:09:16.709120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd176628c3e8'
down_revision = '55a14cec9183'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('new', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('new')

    # ### end Alembic commands ###
