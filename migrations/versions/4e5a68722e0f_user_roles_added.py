"""user roles added

Revision ID: 4e5a68722e0f
Revises: 3a2148c7e9c6
Create Date: 2021-05-10 18:04:59.281798

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '4e5a68722e0f'
down_revision = '3a2148c7e9c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=50), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name'),
                    sa.UniqueConstraint('name')
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
    op.drop_table('user_roles')
    op.drop_table('roles')
    # ### end Alembic commands ###