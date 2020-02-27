"""Create schools-geocoded table

Revision ID: 5108b8b89a36
Revises: 
Create Date: 2020-02-27 15:21:41.309329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5108b8b89a36'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'schools_geocoded',
        sa.Column('id', sa.Integer),
        sa.Column('ATS_CODE', sa.String(50)),
        sa.Column('BORO', sa.String(1)),
        sa.Column('BORONUM', sa.Integer),
        sa.Column('LOC_CODE', sa.String(50), primary_key=True),
        sa.Column('SCHOOLNAME', sa.String(50)),
        sa.Column('SCH_TYPE', sa.String(50)),
        sa.Column('MANAGED_BY', sa.Integer),
        sa.Column('GEO_DISTRI', sa.Integer),
        sa.Column('ADMIN_DIST', sa.Integer),
        sa.Column('ADDRESS', sa.String(50)),
        sa.Column('STATE_CODE', sa.String(2)),
        sa.Column('ZIP', sa.Text),
        sa.Column('PRINCIPAL', sa.String(50)),
        sa.Column('PRIN_PH', sa.Text),
        sa.Column('FAX', sa.Text),
        sa.Column('GRADES', sa.Text),
        sa.Column('block', sa.Integer),
        sa.Column('city', sa.Text),
        sa.Column('coordinates', sa.Text),
        sa.Column('county_fips', sa.Text),
        sa.Column('geocoded_address', sa.Text),
        sa.Column('is_exact', sa.Text),
        sa.Column('is_match', sa.Text),
        sa.Column('latitude', sa.Text),
        sa.Column('longitude', sa.Text),
        sa.Column('returned_address', sa.Text),
        sa.Column('side', sa.String(1)),
        sa.Column('state', sa.String(2)),
        sa.Column('state_fips', sa.Text),
        sa.Column('tiger_line', sa.Integer),
        sa.Column('tract', sa.Integer),
        sa.Column('zipcode', sa.Text)
    )


def downgrade():
    op.drop_table('schools_geocoded')
