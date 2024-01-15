"""Create initial tables

Revision ID: 2fb70b6bb94f
Revises: 
Create Date: 2024-01-14 09:02:03.594277

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2fb70b6bb94f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('enquiry_id', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('quote_details', sa.String(), nullable=True),
    sa.Column('quote_title', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_quote_amount'), 'quote', ['amount'], unique=False)
    op.create_index(op.f('ix_quote_category_id'), 'quote', ['category_id'], unique=False)
    op.create_index(op.f('ix_quote_enquiry_id'), 'quote', ['enquiry_id'], unique=False)
    op.create_index(op.f('ix_quote_id'), 'quote', ['id'], unique=False)
    op.create_index(op.f('ix_quote_quote_details'), 'quote', ['quote_details'], unique=False)
    op.create_index(op.f('ix_quote_quote_title'), 'quote', ['quote_title'], unique=False)
    op.create_index(op.f('ix_quote_status'), 'quote', ['status'], unique=False)
    op.create_table('calendar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quote_id', sa.Integer(), nullable=False),
    sa.Column('scheduled_date', sa.DateTime(), nullable=False),
    sa.Column('event_type', sa.String(), nullable=False),
    sa.Column('event_status', sa.String(), nullable=True),
    sa.Column('notes', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['quote_id'], ['quote.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_calendar_event_status'), 'calendar', ['event_status'], unique=False)
    op.create_index(op.f('ix_calendar_id'), 'calendar', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_calendar_id'), table_name='calendar')
    op.drop_index(op.f('ix_calendar_event_status'), table_name='calendar')
    op.drop_table('calendar')
    op.drop_index(op.f('ix_quote_status'), table_name='quote')
    op.drop_index(op.f('ix_quote_quote_title'), table_name='quote')
    op.drop_index(op.f('ix_quote_quote_details'), table_name='quote')
    op.drop_index(op.f('ix_quote_id'), table_name='quote')
    op.drop_index(op.f('ix_quote_enquiry_id'), table_name='quote')
    op.drop_index(op.f('ix_quote_category_id'), table_name='quote')
    op.drop_index(op.f('ix_quote_amount'), table_name='quote')
    op.drop_table('quote')
    # ### end Alembic commands ###
