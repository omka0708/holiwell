"""empty message

Revision ID: 94fbf01eac9f
Revises: 64dca0e4cabe
Create Date: 2024-05-01 14:16:21.695118

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '94fbf01eac9f'
down_revision: Union[str, None] = '64dca0e4cabe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(), nullable=False))
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('user', 'username')
    # ### end Alembic commands ###