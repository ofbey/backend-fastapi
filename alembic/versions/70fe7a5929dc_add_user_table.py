"""add user table

Revision ID: 70fe7a5929dc
Revises: b164398fe579
Create Date: 2023-06-09 21:59:32.014037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70fe7a5929dc'
down_revision = 'b164398fe579'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass