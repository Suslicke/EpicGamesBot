"""Create DB

Revision ID: d3f3082479c7
Revises: 
Create Date: 2023-03-26 18:57:42.937830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3f3082479c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('game_url', sa.String(), nullable=True),
    sa.Column('time_end', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subscriptions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('game_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_fk', sa.Integer(), nullable=False),
    sa.Column('shor_desc', sa.String(), nullable=True),
    sa.Column('genres', sa.String(), nullable=True),
    sa.Column('features', sa.String(), nullable=True),
    sa.Column('time_end', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['game_fk'], ['games.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('telegram_user_id', sa.BigInteger(), nullable=False),
    sa.Column('telegram_chat_id', sa.BigInteger(), nullable=False),
    sa.Column('telegram_username', sa.String(length=255), nullable=True),
    sa.Column('subscriptions_id', sa.Integer(), nullable=True),
    sa.Column('sub_start_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('sub_end_date', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['subscriptions_id'], ['subscriptions.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('telegram_chat_id'),
    sa.UniqueConstraint('telegram_user_id')
    )
    op.create_table('game_detail_specifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_detail', sa.Integer(), nullable=False),
    sa.Column('os', sa.String(), nullable=True),
    sa.Column('cpu', sa.String(), nullable=True),
    sa.Column('gpu', sa.String(), nullable=True),
    sa.Column('memory', sa.String(), nullable=True),
    sa.Column('space', sa.String(), nullable=True),
    sa.Column('time_end', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['game_detail'], ['game_details.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('total', sa.Integer(), nullable=False),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('subscription_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['subscription_id'], ['subscriptions.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_table('game_detail_specifications')
    op.drop_table('users')
    op.drop_table('game_details')
    op.drop_table('subscriptions')
    op.drop_table('games')
    # ### end Alembic commands ###
