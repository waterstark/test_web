"""empty message

Revision ID: f70eac98d788
Revises: 25f7b7f4bd03
Create Date: 2023-07-10 12:33:04.825347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f70eac98d788'
down_revision = '25f7b7f4bd03'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('title', sa.String(), nullable=False))
    op.add_column('post', sa.Column('number_of_likes', sa.Integer(), nullable=False))
    op.add_column('post', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'post', 'user', ['owner_id'], ['id'], ondelete='CASCADE')
    op.drop_column('post', 'author_of_post')
    op.drop_index('ix_user_email', table_name='user')
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.create_index('ix_user_email', 'user', ['email'], unique=False)
    op.add_column('post', sa.Column('author_of_post', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_column('post', 'owner_id')
    op.drop_column('post', 'number_of_likes')
    op.drop_column('post', 'title')
    # ### end Alembic commands ###
