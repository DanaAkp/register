from app.app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


organization_service_form = db.Table('organization_service_form',
                                     db.Column('organizations_id', db.Integer, db.ForeignKey('organizations.id')),
                                     db.Column('service_forms_id', db.Integer, db.ForeignKey('service_forms.id')))


type_service_form = db.Table('type_service_form',
                             db.Column('types_of_service_id', db.Integer, db.ForeignKey('types_of_service.id')),
                             db.Column('service_forms_id', db.Integer, db.ForeignKey('service_forms.id')))


class Organization(db.Model):
    __tablename__ = 'organizations'
    # 1 регистрационный номер учетной записи
    id = db.Column(db.Integer(), primary_key=True)
    # 2 название организации
    name = db.Column(db.Text(), nullable=False)
    # 3 дата гос. регистрации юр. лица
    date_registration = db.Column(db.DateTime(), nullable=False)
    # 4 организационно-правовая форма
    opf = db.Column(db.Text(), nullable=False)
    # 5 адреса, телефон, эл. почта
    contacts = db.Column(db.Text(), nullable=False)
    # 6 ФИО руководителя
    name_boss = db.Column(db.Text(), nullable=False)
    # 7 информация о лицензии организации
    license = db.Column(db.Text(), nullable=False)

    # 8 формы обслуживания
    form_service = db.relationship('ServiceForm', secondary='organization_service_form',
                                      backref=db.backref('organizations', lazy='dynamic'))

    # 9 направления реабилитации или абилитации
    direction_of_rehabilitation = db.Column(db.Text(), nullable=False)
    # 10 перечень оказываемых услуг, наличие специалистов, наличие технических средств, реабилитационные программы
    resources = db.Column(db.Text(), nullable=False)
    # 11 общее количество мест для реабил. услуг
    total_seats = db.Column(db.Integer(), nullable=False)
    # 11 количество свободных мест для реабил. услуг TODO по формам обслуживания
    free_seats = db.Column(db.Integer(), nullable=False)
    # 12 информация о результатх, проведенных проверок
    result_checks = db.Column(db.Text(), nullable=False)
    # 13 информация об опыте работы за последние 5 лет
    work_experience = db.Column(db.Text(), nullable=False)
    # 14 ведомственная принадлежность
    departmental_affiliation = db.Column(db.Text(), nullable=False)
    # 15 вышестоящая организация
    parent_organization = db.Column(db.Text(), nullable=False)
    # 16 другая информация, определнная региональными нормативными актами
    other_information = db.Column(db.Text(), nullable=False)

    def __str__(self):
        return self.name


class ServiceForm(db.Model):
    __tablename__ = 'service_forms'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __str__(self):
        return self.name


class TypeOfService(db.Model):
    __tablename__ = 'types_of_service'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    id_service_form = db.relationship('ServiceForm',secondary='type_service_form',
                                      backref=db.backref('types_of_service', lazy='dynamic'))

    def __str__(self):
        return self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __str__(self):
        return self.name
