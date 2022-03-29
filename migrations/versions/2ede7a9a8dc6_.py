"""empty message

Revision ID: 2ede7a9a8dc6
Revises: 4851c5079c5b
Create Date: 2021-07-12 16:34:15.112872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ede7a9a8dc6'
down_revision = '4851c5079c5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('date_sent', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_messages_date_sent'), 'messages', ['date_sent'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_messages_date_sent'), table_name='messages')
    op.drop_column('messages', 'date_sent')
    # ### end Alembic commands ###