"""empty message

Revision ID: 34e51f44cca9
Revises: 
Create Date: 2024-07-25 16:02:53.737759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34e51f44cca9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('positions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('Updated_at', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sellers',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('Updated_at', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('checklists',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('seller_id', sa.Integer(), nullable=False),
    sa.Column('sale_date', sa.Date(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('phases', sa.Integer(), nullable=True),
    sa.Column('voltage', sa.Integer(), nullable=True),
    sa.Column('power', sa.Integer(), nullable=True),
    sa.Column('special_project', sa.Integer(), nullable=True),
    sa.Column('eletric_key', sa.Boolean(), nullable=True),
    sa.Column('eletric_panel', sa.Boolean(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('layout', sa.Boolean(), nullable=True),
    sa.Column('pipeline', sa.Boolean(), nullable=True),
    sa.Column('special_paint', sa.Boolean(), nullable=True),
    sa.Column('extra_filters', sa.Boolean(), nullable=True),
    sa.Column('assembly', sa.String(length=255), nullable=True),
    sa.Column('freight', sa.String(length=255), nullable=True),
    sa.Column('pallet', sa.Boolean(), nullable=True),
    sa.Column('adress', sa.String(length=255), nullable=True),
    sa.Column('deadline', sa.Date(), nullable=True),
    sa.Column('other', sa.String(length=255), nullable=True),
    sa.Column('filled', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('Updated_at', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['seller_id'], ['sellers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lead_sales',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('sale_date', sa.DateTime(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('seller_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('Updated_at', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['seller_id'], ['sellers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('position_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('Updated_at', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['position_id'], ['positions.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('lead_sales')
    op.drop_table('checklists')
    op.drop_table('sellers')
    op.drop_table('positions')
    # ### end Alembic commands ###
