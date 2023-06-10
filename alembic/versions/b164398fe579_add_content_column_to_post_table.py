"""add content column to post table

Revision ID: b164398fe579
Revises: ff39731fe113
Create Date: 2023-06-09 21:54:22.434024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b164398fe579'
down_revision = 'ff39731fe113'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass