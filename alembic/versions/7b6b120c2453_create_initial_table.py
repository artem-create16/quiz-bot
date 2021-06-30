"""create initial table

Revision ID: 7b6b120c2453
Revises: 
Create Date: 2021-06-30 15:39:53.030940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b6b120c2453'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('telegram_id', sa.Integer(), nullable=False),
                    sa.Column('chat_id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('first_name', sa.String()),
                    sa.Column('first_name', sa.String()),
                    sa.Column('last_name', sa.String()),
                    sa.Column('username', sa.String()),
                    sa.PrimaryKeyConstraint('telegram_id'),
                    sa.UniqueConstraint('telegram_id'),
                    sa.UniqueConstraint('username'),
                    sa.UniqueConstraint('chat_id')
                    )


def downgrade():
    pass
