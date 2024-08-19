"""empty message

Revision ID: 7958bca727ff
Revises: 72e332176e85
Create Date: 2024-08-17 20:41:44.252044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7958bca727ff'
down_revision = '72e332176e85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('checklists', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description_pipeline', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('checklists', schema=None) as batch_op:
        batch_op.drop_column('description_pipeline')

    # ### end Alembic commands ###
