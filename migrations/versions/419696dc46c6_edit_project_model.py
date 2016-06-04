"""edit project model

Revision ID: 419696dc46c6
Revises: None
Create Date: 2016-05-28 12:16:43.399000

"""

# revision identifiers, used by Alembic.
revision = '419696dc46c6'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.add_column('project', sa.Column('project_description', sa.VARCHAR(length=200), nullable=True))
    op.add_column('project', sa.Column('project_id', sa.VARCHAR(length=50), nullable=True))
    op.create_index(op.f('ix_project_project_id'), 'project', ['project_id'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_project_project_id'), table_name='project')
    op.drop_column('project', 'project_id')
    op.drop_column('project', 'project_description')
    op.create_table('user',
    sa.Column('username', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('pw_hash', mysql.VARCHAR(length=80), nullable=True),
    sa.PrimaryKeyConstraint('username'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    ### end Alembic commands ###