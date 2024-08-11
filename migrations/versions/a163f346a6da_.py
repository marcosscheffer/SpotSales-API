"""empty message

Revision ID: a163f346a6da
Revises: 8a6ad7f2cffc
Create Date: 2024-08-11 11:44:07.270129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a163f346a6da'
down_revision = '8a6ad7f2cffc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lead_sales', schema=None) as batch_op:
        batch_op.add_column(sa.Column('company', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('ts', sa.String(length=20), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lead_sales', schema=None) as batch_op:
        batch_op.drop_column('ts')
        batch_op.drop_column('company')

    # ### end Alembic commands ###
