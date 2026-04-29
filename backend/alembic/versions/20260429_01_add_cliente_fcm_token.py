"""Add fcm_token to cliente table

Revision ID: 20260429_01
Revises: 20260428_01_create_pago
Create Date: 2026-04-29

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20260429_01'
down_revision = '20260428_01_create_pago'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('cliente', sa.Column('fcm_token', sa.String(255), nullable=True))


def downgrade() -> None:
    op.drop_column('cliente', 'fcm_token')
