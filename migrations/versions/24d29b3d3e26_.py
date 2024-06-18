"""empty message

Revision ID: 24d29b3d3e26
Revises: e6fe48981b7d
Create Date: 2024-03-17 19:08:15.670397

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '24d29b3d3e26'
down_revision: Union[str, None] = 'e6fe48981b7d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'username')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
