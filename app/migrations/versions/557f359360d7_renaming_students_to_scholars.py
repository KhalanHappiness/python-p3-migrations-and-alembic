"""Renaming students to scholars

Revision ID: 557f359360d7
Revises: 2966e19e6460
Create Date: 2025-05-27 15:23:18.940235

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '557f359360d7'
down_revision: Union[str, None] = '2966e19e6460'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    pass


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    pass
