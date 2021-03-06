# flake8: noqa
"""empty message

Revision ID: 748d5fc8c8
Revises: 5290ef12641
Create Date: 2015-08-20 09:12:32.308260

"""

# revision identifiers, used by Alembic.
revision = '748d5fc8c8'
down_revision = '5290ef12641'


from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('borrower',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('case_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('middle_names', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('mobile_no', sa.String(), nullable=False),
    sa.Column('email_address', sa.String(), nullable=False),
    sa.Column('address', postgresql.ARRAY(sa.String()), nullable=False),
    sa.ForeignKeyConstraint(['case_id'], ['case.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('borrower')
    ### end Alembic commands ###
