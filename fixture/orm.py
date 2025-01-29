from sqlalchemy import create_engine, Column, Integer, String, DateTime, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
from model.group import Group
from model.contact import Contact

Base = declarative_base()

class ORMFixture:
    def __init__(self, host, name, user, password):
        self.engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{name}')
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    class ORMGroup(Base):
        __tablename__ = 'group_list'
        id = Column(Integer, primary_key=True, name='group_id')
        name = Column(String, name='group_name')
        header = Column(String, name='group_header')
        footer = Column(String, name='group_footer')
        contacts = relationship('ORMContact', secondary='address_in_groups', back_populates='groups')

    class ORMContact(Base):
        __tablename__ = 'addressbook'
        id = Column(Integer, primary_key=True, name='id')
        firstname = Column(String, name='firstname')
        lastname = Column(String, name='lastname')
        deprecated = Column(DateTime, name='deprecated')
        groups = relationship('ORMGroup', secondary='address_in_groups', back_populates='contacts')

    address_in_groups = Table('address_in_groups', Base.metadata,
        Column('id', Integer, ForeignKey('addressbook.id'), primary_key=True),
        Column('group_id', Integer, ForeignKey('group_list.group_id'), primary_key=True)
    )

    def convert_groups_to_model(self, groups):
        return [Group(id=str(group.id), group_name=group.name, group_header=group.header, group_footer=group.footer) for group in groups]

    def convert_contacts_to_model(self, contacts):
        return [Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname) for contact in contacts]

    def get_group_list(self):
        session = self.Session()
        groups = session.query(self.ORMGroup).all()
        session.close()
        return self.convert_groups_to_model(groups)

    def get_contact_list(self):
        session = self.Session()
        contacts = session.query(self.ORMContact).filter(self.ORMContact.deprecated == None).all()
        session.close()
        return self.convert_contacts_to_model(contacts)

    def get_contacts_in_group(self, group):
        session = self.Session()
        orm_group = session.query(self.ORMGroup).filter(self.ORMGroup.id == group.id).first()
        contacts = orm_group.contacts if orm_group else []
        session.close()
        return self.convert_contacts_to_model(contacts)

    def get_contacts_not_in_group(self, group):
        session = self.Session()
        orm_group = session.query(self.ORMGroup).filter(self.ORMGroup.id == group.id).first()
        contacts = session.query(self.ORMContact).filter(self.ORMContact.deprecated == None).filter(~self.ORMContact.groups.contains(orm_group)).all()
        session.close()
        return self.convert_contacts_to_model(contacts)

    def get_groups_in_contact(self, contact):
        session = self.Session()
        orm_contact = session.query(self.ORMContact).filter(self.ORMContact.id == contact.id).first()
        groups = orm_contact.groups if orm_contact else []
        session.close()
        return self.convert_groups_to_model(groups)