from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from app.models import User, Organization, ServiceForm, TypeOfService, OrganizationServiceForm, ServiceFormTypeOfService
import re


class OrganizationView(ModelView):
    column_hide_backrefs = False
    # column_list = ('name', 'date_registration', 'opf', 'contacts', 'name_boss', 'license',
    #                'direction_of_rehabilitation')


class MyModelView(ModelView):
    pass

