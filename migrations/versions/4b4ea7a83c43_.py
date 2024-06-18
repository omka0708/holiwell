"""empty message

Revision ID: 4b4ea7a83c43
Revises: 4f7be532dcbe
Create Date: 2024-04-13 19:06:25.921832

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4b4ea7a83c43'
down_revision: Union[str, None] = '4f7be532dcbe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course_type',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('slug', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('course',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('path_to_cover', sa.String(), nullable=True),
    sa.Column('course_type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_type_id'], ['course_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('lesson', sa.Column('course_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'lesson', 'course', ['course_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'lesson', type_='foreignkey')
    op.drop_column('lesson', 'course_id')
    op.drop_table('course')
    op.drop_table('course_type')
    # ### end Alembic commands ###
