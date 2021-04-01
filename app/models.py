from app.app import db


class Organization(db.Model):
    __tablename__ = 'organizations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    date_registration = db.Column(db.Date, nullable=False)
    opf = db.Column(db.Text, nullable=False)
    address = db.Column(db.Text, nullable=False)
    name_boss = db.Column(db.Text, nullable=False)
    license = db.Column(db.Text, nullable=False)

    form_service = ''

    direction_of_rehabilitation_or_habilitation = db.Column(db.Text, nullable=False)


class OPF(db.Model):
    pass


class Address(db.Model):
    pass


class ServiceForms(db.Model):
    pass


class TypesOfService(db.Model):
    pass
