"""The fields in the file with models and schemas have been adjusted.

Revision ID: d8ab3febcfba
Revises: 88566986fa2a
Create Date: 2023-07-16 11:36:28.099947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d8ab3febcfba"
down_revision = "88566986fa2a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("rating", sa.Column("like_is_toggeled", sa.Boolean(), nullable=True))
    op.drop_column("rating", "like")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "rating", sa.Column("like", sa.BOOLEAN(), autoincrement=False, nullable=True)
    )  # noqa: E501
    op.drop_column("rating", "like_is_toggeled")
    # ### end Alembic commands ###
