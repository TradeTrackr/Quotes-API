"""added start and end date

Revision ID: b1bcec5e52c2
Revises: 327dc447ebdd
Create Date: 2024-01-28 14:26:42.632599

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b1bcec5e52c2'
down_revision: Union[str, None] = '327dc447ebdd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('calendar', sa.Column('scheduled_start_date_and_time', sa.DateTime(), nullable=False))
    op.add_column('calendar', sa.Column('scheduled_end_date_and_time', sa.DateTime(), nullable=False))
    op.drop_column('calendar', 'scheduled_date')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('calendar', sa.Column('scheduled_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.drop_column('calendar', 'scheduled_end_date_and_time')
    op.drop_column('calendar', 'scheduled_start_date_and_time')
    # ### end Alembic commands ###
