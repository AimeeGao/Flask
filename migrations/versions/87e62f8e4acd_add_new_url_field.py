"""add new url field

Revision ID: 87e62f8e4acd
Revises: 2beb25979ecd
Create Date: 2018-05-09 15:44:52.683065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87e62f8e4acd'
down_revision = '2beb25979ecd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('live',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('up_id', sa.Integer(), nullable=True),
    sa.Column('live_url', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['up_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_live_live_url'), 'live', ['live_url'], unique=True)
    op.create_index(op.f('ix_live_name'), 'live', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_live_name'), table_name='live')
    op.drop_index(op.f('ix_live_live_url'), table_name='live')
    op.drop_table('live')
    # ### end Alembic commands ###
