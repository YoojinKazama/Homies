# Import Packages
from database import Base
from sqlalchemy import text
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, DateTime, Float, Text, Boolean, Date, Time, Numeric
from sqlalchemy.orm import relationship


# * PUBLIC USER
class PublicUser(Base):
    __tablename__ = 'public_users'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))
    is_blacklist = Column(Boolean, default=text('0'))

    profile = relationship('PublicProfile', back_populates='public_user', uselist=False)


class PublicProfile(Base):
    __tablename__ = 'public_profiles'

    id = Column(String(36), primary_key=True, nullable=False, default=text('UUID()'))
    user_id = Column(String(36), ForeignKey('public_users.id'), nullable=True)
    first_name = Column(String(255), nullable=False)
    middle_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=False)
    suffix_name = Column(String(255), nullable=True)
    birth_date = Column(Date, nullable=False)
    gender = Column(String(255), nullable=False)
    house_street = Column(String(255), nullable=False)
    barangay = Column(String(255), nullable=False)
    municipality = Column(String(255), nullable=False)
    province = Column(String(255), nullable=False)
    region = Column(String(255), nullable=False)
    contact_number = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    full_address = Column(String(255), nullable=False)

    public_user = relationship('PublicUser', back_populates='profile')


# * INTERNAL USER
class InternalUser(Base):
    __tablename__ = 'internal_users'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))

    roles = relationship('UserRole', back_populates='user')
    employee_info = relationship('Employee', back_populates = 'user_credentials', uselist=False)


class Role(Base):
    __tablename__ = 'roles'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    subsystem = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    redirect_url = Column(String(255), nullable=False)

    users = relationship('UserRole', back_populates='role')


class UserRole(Base):
    __tablename__ = 'user_roles'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    user_id = Column(String(36), ForeignKey('internal_users.id'), default=text('UUID()'))
    role_id = Column(String(36), ForeignKey('roles.id'), default=text('UUID()'))

    user = relationship('InternalUser', back_populates='roles')
    role = relationship('Role', back_populates='users')

# Department Model
# Hiram namin sa core human capital
class Department(Base):
    __tablename__ = "departments"

    # ==================================================================================
    # Columns
    # ==================================================================================

    department_id = Column(
        String(36),
        primary_key = True,
        default = text('UUID()')
    )
    name = Column(
        String(255),
        nullable = False
    )
    description = Column(
        String(255),
        nullable = False
    )
    created_at = Column(
        DateTime,
        default = text('NOW()'),
        nullable = False
    )
    updated_at = Column(
        DateTime,
        default = text('NOW()'),
        onupdate = text('NOW()')
    )
    
class Employee(Base):
    __tablename__ = "employees"

    # ==================================================================================
    # Columns
    # ==================================================================================

    employee_id = Column(
        String(36),
        primary_key = True,
        default = text('UUID()')
    )
    user_id = Column(
        String(36), 
        ForeignKey('internal_users.id'), 
        nullable=False
    )
    first_name = Column(
        String(255),
        nullable = False
    )
    middle_name = Column(
        String(255),
        nullable =  True
    )
    last_name = Column(
        String(255),
        nullable = False
    )
    extension_name = Column(
        String(255),
        nullable = True
    )
    contact_number = Column(
        String(255),
        nullable = False
    )
    status = Column(
        String(255),
        nullable = True
    )
    created_at = Column(
        DateTime,
        default = text('NOW()'),
        nullable = False
    )
    updated_at = Column(
        DateTime,
        default = text('NOW()'),
        onupdate = text('NOW()')
    )

class Asset(Base):
    __tablename__ = 'assets'

    asset_id = Column(String(60), primary_key=True, default=text('UUID()'))
    asset_provider_id = Column(String(60), ForeignKey('asset_providers.asset_provider_id'), nullable=True)
    asset_type_id = Column(String(60), ForeignKey('asset_types.asset_type_id'), nullable=True)
    asset_number = Column(Integer, nullable=True)
    asset_cost = Column(Numeric, nullable=True)
    asset_title = Column(String(255), nullable=True)
    asset_description = Column(Text, nullable=True)
    asset_brand = Column(String(255), nullable=True)
    asset_model = Column(String(255), nullable=True)
    asset_serial = Column(String(255), nullable=True)
    asset_acquisition = Column(String(255), nullable=True)
    acquisition_date = Column(DateTime, nullable=True)
    asset_status = Column(String(255), nullable=True, default=('Available'))
    asset_remarks = Column(String(255), nullable=True)
    active_status = Column(String(255), nullable=True, default=('Active'))
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))
    created_by = Column(String(60), ForeignKey('internal_users.id'))

    asset_provider = relationship('Asset_provider', back_populates='asset', lazy='joined')
    asset_type = relationship('Asset_Type', back_populates='asset', lazy='joined')
    created_by_details = relationship('InternalUser', foreign_keys=[created_by], lazy='joined')

class Asset_provider(Base):
    __tablename__ = 'asset_providers'
    
    asset_provider_id = Column(String(36), primary_key=True, default=text('UUID()'))
    asset_provider_name = Column(String(255), nullable=True)
    asset_provider_contact = Column(String(255), nullable=True)
    asset_provider_email = Column(String(255), nullable=True)
    active_status = Column(String(255), nullable=True, default=('Active'))
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))

    asset = relationship('Asset')
    
class Asset_Type(Base):
    __tablename__ = 'asset_types'

    asset_type_id = Column(String(36), primary_key=True, default=text('UUID()'))
    asset_type_title = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    active_status = Column(String(255), nullable=True, default=('Active'))
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))

    asset = relationship('Asset')

class Asset_Warranty(Base):
    __tablename__ = 'asset_warranty'

    warranty_id = Column(String(36), primary_key=True, default=text('UUID()'))
    asset_id = Column(String(36), ForeignKey('assets.asset_id'), nullable=True)
    warranty_length = Column(Numeric, nullable=True)
    expiration_date = Column(DateTime, nullable=True)
    warranty_contact = Column(String(255), nullable=True)
    warranty_email = Column(String(255), nullable=True)
    warranty_note = Column(String(255), nullable=True)
    active_status = Column(Text, nullable=True, default=('Active'))

    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))
    created_by = Column(String(36), ForeignKey('internal_users.id'), nullable=True)

    asset_type = relationship('Asset', foreign_keys=[asset_id], lazy='joined')
    created_by_details = relationship('InternalUser', foreign_keys=[created_by], lazy='joined')
    
class Broken_Asset(Base):
    __tablename__ = 'broken_assets'

    broken_id = Column(String(36), primary_key=True, default=text('UUID()'))
    asset_id = Column(String(36), ForeignKey('assets.asset_id'), nullable=True)
    remarks = Column(Text, nullable=True)
    broken_date = Column(DateTime, nullable=True)
    active_status = Column(String(255), nullable=True, default=('Active'))
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))

    created_by = Column(String(60), ForeignKey('internal_users.id'))


    created_by_details = relationship('InternalUser', foreign_keys=[created_by], lazy='joined')
    
class Asset_check_out(Base):
    __tablename__ = 'asset_check_out'

    check_out_id = Column(String(36), primary_key=True, default=text('UUID()'))
    asset_id = Column(String(60), ForeignKey('assets.asset_id'), nullable=True)
    user_id = Column(String(60), ForeignKey('internal_users.id'), nullable=True)
    department_id = Column(String(60), ForeignKey('departments.department_id'), nullable=True)
    location = Column(String(255), nullable=True)
    check_out_date = Column(DateTime, nullable=True)
    check_out_due = Column(DateTime, nullable=True)
    remarks = Column(Text, nullable=True)
    active_status = Column(String(255), nullable=True, default=('Active'))
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))
   
    on_department = relationship('Department', foreign_keys=[department_id], lazy='joined')
    on_user = relationship('InternalUser', foreign_keys=[user_id], lazy='joined')
    the_asset = relationship('Asset', foreign_keys=[asset_id], lazy='joined')
    
    
class Dispose_Asset(Base):
    __tablename__ = 'dispose_assets'

    dispose_id = Column(String(36), primary_key=True, default=text('UUID()'))
    asset_id = Column(String(36), ForeignKey('assets.asset_id'), nullable=True)
    remarks = Column(Text, nullable=True)
    dispose_to = Column(String(255), nullable=True)
    dispose_date = Column(DateTime, nullable=True)
    active_status = Column(String(255), nullable=True, default=('Active'))
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))

    created_by = Column(String(60), ForeignKey('internal_users.id'))


    created_by_details = relationship('InternalUser', foreign_keys=[created_by], lazy='joined')
    
class Events(Base):
    __tablename__ = 'events'

    event_id = Column(String(36), primary_key=True, default=text('UUID()'))
    asset_id = Column(String(36), ForeignKey('assets.asset_id'), nullable=True)
    event_title = Column(String(255), nullable=True)
    event_message = Column(String(255), nullable=True)
    active_status = Column(String(255), nullable=True, default=('Active'))
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))
    
class Maintenance(Base):
    __tablename__ = 'maintenances'

    maintenance_id = Column(String(36), primary_key=True, default=text('UUID()'))
    maintenance_provider_id = Column(String(36), ForeignKey('maintenance_providers.maintenance_provider_id'), nullable=False)
    asset_id = Column(String(36), ForeignKey('assets.asset_id'), nullable=False)
    maintenance_name = Column(String(255), nullable=True)
    maintenance_details = Column(String(255), nullable=True)
    maintenance_cost = Column(Numeric, nullable=True)
    maintenance_day = Column(Integer, nullable=True)
    maintenance_due = Column(DateTime, nullable=True)
    maintenance_completed = Column(DateTime, nullable=True)
    maintenance_repeatable = Column(String(255), nullable=True)
    maintenance_status = Column(String(255), nullable=True)
    remarks = Column(String(255), nullable=True)
    active_status = Column(String(255), nullable=True, default=('Active'))
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))

    Maintenance_provider = relationship('Maintenance_provider', back_populates='maintenance', lazy='joined')
    
class Maintenance_provider(Base):
    __tablename__ = 'maintenance_providers'

    maintenance_provider_id = Column(String(36), primary_key=True, default=text('UUID()'))
    maintenance_provider_name = Column(String(255), nullable=True)
    maintenance_provider_contact = Column(String(255), nullable=True)
    maintenance_provider_email = Column(String(255), nullable=True) 
    active_status = Column(String(255), nullable=True, default=('Active'))
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))

    maintenance = relationship('Maintenance')

class Maintenance_Report(Base):
    __tablename__ = 'maintenance_reports'

    maintenance_report_id = Column(String(36), primary_key=True, default=text('UUID()'))
    maintenance_id = Column(String(36), ForeignKey('maintenances.maintenance_id'), nullable=False)
    maintenance_cost = Column(Numeric, nullable=True)
    completed_date = Column(DateTime, nullable=True)
    remarks = Column(Text, nullable=True)
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))

    maintenance_details = relationship('Maintenance', foreign_keys=[maintenance_id], lazy='joined')

class Missing_Asset(Base):
    __tablename__ = 'missing_assets'

    missing_id = Column(String(36), primary_key=True, default=text('UUID()'))
    asset_id = Column(String(36), ForeignKey('assets.asset_id'), nullable=True)
    remarks = Column(Text, nullable=True)
    missing_date = Column(DateTime, nullable=True)
    active_status = Column(String(255), nullable=True, default=('Active'))
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))

    created_by = Column(String(60), ForeignKey('internal_users.id'))


    created_by_details = relationship('InternalUser', foreign_keys=[created_by], lazy='joined')

class Request_Asset(Base):
    __tablename__ = 'request_assets'

    request_id = Column(String(36), primary_key=True, default=text('UUID()'))
    asset_type_id = Column(String(36), ForeignKey('asset_types.asset_type_id'), nullable=True)
    request_brand = Column(String(255), nullable=True)
    request_model = Column(DateTime, nullable=True)
    request_description = Column(Text, nullable=True)
    request_status = Column(String(255), nullable=True)
    request_remark = Column(Text, nullable=True)
    active_status = Column(Text, nullable=True, default=('Active'))

    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))
    created_by = Column(String(36), ForeignKey('users.user_id'), nullable=True)
    updated_by = Column(String(36), ForeignKey('users.user_id'), nullable=True)

    asset_type = relationship('Asset_Type', lazy='joined')
    created_by_details = relationship('User', foreign_keys=[created_by], lazy='joined')
    updated_by_details = relationship('User', foreign_keys=[updated_by], lazy='joined')   

class Sell_Asset(Base):
    __tablename__ = 'sell_assets'

    sell_id = Column(String(36), primary_key=True, default=text('UUID()'))
    asset_id = Column(String(36), ForeignKey('assets.asset_id'), nullable=True)
    sell_to = Column(String(255), nullable=True)
    sell_to_contact = Column(String(255), nullable=True)
    sell_to_email = Column(String(255), nullable=True)
    sell_date = Column(DateTime, nullable=True)
    sell_price = Column(Numeric, nullable=True)
    remarks = Column(Text, nullable=True)
    active_status = Column(String(255), nullable=True, default=('Active'))
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))

    created_by = Column(String(60), ForeignKey('internal_users.id'))


    created_by_details = relationship('InternalUser', foreign_keys=[created_by], lazy='joined')       