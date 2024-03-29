"""added category id to calendar

Revision ID: 45c4718722d0
Revises: b32d590cee65
Create Date: 2024-01-31 07:29:16.691672

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45c4718722d0'
down_revision: Union[str, None] = 'b32d590cee65'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('calendar', sa.Column('category_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_calendar_category_id'), 'calendar', ['category_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_calendar_category_id'), table_name='calendar')
    op.drop_column('calendar', 'category_id')
    # ### end Alembic commands ###
