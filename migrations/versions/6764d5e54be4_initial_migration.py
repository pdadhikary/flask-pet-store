"""Initial Migration

Revision ID: 6764d5e54be4
Revises: 
Create Date: 2021-05-05 11:36:35.378015

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6764d5e54be4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=60), nullable=False),
                    sa.Column('brand', sa.String(length=60), nullable=False),
                    sa.Column('category', sa.String(length=30), nullable=False),
                    sa.Column('product_image', sa.String(length=150), nullable=True),
                    sa.Column('quantity', sa.Integer(), nullable=False),
                    sa.Column('description', sa.String(length=350), nullable=False),
                    sa.PrimaryKeyConstraint('id')
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
                    sa.ForeignKeyConstraint(['product_id'], ['admin.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
                    )
    op.drop_table('user_roles')
    op.drop_table('customer')
    op.drop_table('role')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('name', sa.VARCHAR(length=50), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    op.create_table('customer',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('first_name', sa.VARCHAR(length=30), nullable=False),
                    sa.Column('last_name', sa.VARCHAR(length=30), nullable=False),
                    sa.Column('sex', sa.VARCHAR(length=1), nullable=False),
                    sa.Column('email', sa.VARCHAR(length=80), nullable=False),
                    sa.Column('username', sa.VARCHAR(length=60), nullable=False),
                    sa.Column('password_hash', sa.VARCHAR(length=60), nullable=False),
                    sa.Column('street_name', sa.VARCHAR(length=60), nullable=False),
                    sa.Column('zip_code', sa.VARCHAR(length=7), nullable=False),
                    sa.Column('city', sa.VARCHAR(length=30), nullable=False),
                    sa.Column('province', sa.VARCHAR(length=2), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('username')
                    )
    op.create_table('user_roles',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('customer_id', sa.INTEGER(), nullable=True),
                    sa.Column('role_id', sa.INTEGER(), nullable=True),
                    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.drop_table('product_orders')
    op.drop_table('user')
    op.drop_table('admin')
    # ### end Alembic commands ###
