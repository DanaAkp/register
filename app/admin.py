from flask import request, url_for, redirect
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm
from flask_babelex import Babel
from flask_login import current_user
from app.models import User, Organization, ServiceForm, TypeOfService, OrganizationServiceForm, ServiceFormTypeOfService
import re


class OrganizationView(ModelView):
    # form_base_class = SecureForm
    column_filters = ('name', 'id_form_service')
    column_searchable_list = ('name', 'contacts')
    # column_hide_backrefs = False
    # column_list = ('name', 'date_registration', 'opf', 'contacts', 'name_boss', 'license',
    #                'direction_of_rehabilitation')


class MyModelView(ModelView):
    pass
    # def is_accessible(self):
    #     return current_user.is_authenticated
    #
    # def inaccessible_callback(self, name, **kwargs):
    #     # redirect to login page if user doesn't have access
    #     return redirect(url_for('login', next=request.url))

