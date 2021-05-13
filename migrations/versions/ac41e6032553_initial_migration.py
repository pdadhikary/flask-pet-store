"""initial migration

Revision ID: ac41e6032553
Revises: 
Create Date: 2021-05-13 15:50:09.186958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac41e6032553'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('brand', sa.String(length=60), nullable=False),
    sa.Column('category', sa.String(length=30), nullable=False),
    sa.Column('product_image', sa.String(length=150), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=350), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('sex', sa.String(length=1), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('username', sa.String(length=60), nullable=False),
    sa.Column('password_hash', sa.String(length=60), nullable=False),
    sa.Column('street_name', sa.String(length=60), nullable=False),
    sa.Column('zip_code', sa.String(length=7), nullable=False),
    sa.Column('city', sa.String(length=30), nullable=False),
    sa.Column('province', sa.String(length=2), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username'),
    sa.UniqueConstraint('username')
    )
    op.create_table('product_orders',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('user_roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_roles')
    op.drop_table('product_orders')
    op.drop_table('user')
    op.drop_table('roles')
    op.drop_table('product')
    # ### end Alembic commands ###