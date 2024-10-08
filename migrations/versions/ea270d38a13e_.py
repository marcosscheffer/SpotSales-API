"""empty message

Revision ID: ea270d38a13e
Revises: a19afd7a14f8
Create Date: 2024-08-20 13:47:52.964106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea270d38a13e'
down_revision = 'a19afd7a14f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.String(length=20), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('filter_op',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('seller_id', sa.Integer(), nullable=False),
    sa.Column('sale_date', sa.Date(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('ts', sa.String(length=20), nullable=False),
    sa.Column('deadline', sa.Date(), nullable=True),
    sa.Column('carrier', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['seller_id'], ['sellers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products_solds',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('filter_op_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['filter_op_id'], ['filter_op.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products_solds')
    op.drop_table('filter_op')
    op.drop_table('product')
    # ### end Alembic commands ###
