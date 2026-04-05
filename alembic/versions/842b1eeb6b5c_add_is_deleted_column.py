"""add is_deleted column

Revision ID: 842b1eeb6b5c
Revises: 
Create Date: 2026-04-06 00:24:58.268528

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '842b1eeb6b5c'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column(
        'transactions',
        sa.Column('is_deleted', sa.Boolean(), nullable=True)
    )

def downgrade():
    op.drop_column('transactions', 'is_deleted')