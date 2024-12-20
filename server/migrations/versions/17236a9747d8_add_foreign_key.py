"""add foreign key

Revision ID: 17236a9747d8
Revises: 5d1939a6c406
Create Date: 2024-12-04 09:59:43.957263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17236a9747d8'
down_revision = '5d1939a6c406'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hamburgers_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('deli_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_hamburgers_table_deli_id_delis_table'), 'delis_table', ['deli_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hamburgers_table', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_hamburgers_table_deli_id_delis_table'), type_='foreignkey')
        batch_op.drop_column('deli_id')

    # ### end Alembic commands ###
