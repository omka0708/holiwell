"""empty message

Revision ID: f24be1dbfc05
Revises: 3799d168d1b3
Create Date: 2024-03-31 22:36:07.808903

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f24be1dbfc05'
down_revision: Union[str, None] = '3799d168d1b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('link_before_lesson',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('lesson_id', sa.Integer(), nullable=True),
    sa.Column('linked_lesson_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['lesson_id'], ['lesson.id'], ),
    sa.ForeignKeyConstraint(['linked_lesson_id'], ['lesson.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('link_before_lesson')
    # ### end Alembic commands ###
