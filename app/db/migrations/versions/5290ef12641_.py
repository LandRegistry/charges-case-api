# flake8: noqa
"""empty message

Revision ID: 5290ef12641
Revises: 2dbc8088936
Create Date: 2015-07-30 14:35:37.465838

"""

# revision identifiers, used by Alembic.
revision = '5290ef12641'
down_revision = '2dbc8088936'


from alembic import op
import sqlalchemy as sa



def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('case', sa.Column('case_ref', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('case', 'case_ref')
    ### end Alembic commands ###
