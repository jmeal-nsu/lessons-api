"""add Place and Lesson tables

Revision ID: ff0d0fded14c
Revises: 25579adec504
Create Date: 2024-04-02 01:48:09.826629

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'ff0d0fded14c'
down_revision: Union[str, None] = '25579adec504'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('place',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cabinet', sa.String(), nullable=True),
    sa.Column('pavilion', postgresql.ENUM('NEW', 'MAIN', 'LAB', 'SPORT_OLD', 'SPORT_NEW', 'STADIUM', name='pavilion'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lesson',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start', sa.DateTime(), nullable=True),
    sa.Column('subject', sa.String(), nullable=True),
    sa.Column('type', postgresql.ENUM('LECTURE', 'PRACTICE', 'LABORATORY', name='lessontype'), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.Column('place_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['place_id'], ['place.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lesson')
    op.drop_table('place')
    # ### end Alembic commands ###
