from flask import request, url_for, redirect
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class OrganizationView(ModelView):
    column_filters = ['form_service']
    column_searchable_list = ('name', 'contacts')
    can_edit = False
    can_create = False
    can_delete = False

    column_list = ('id', 'name', 'date_registration', 'opf', 'contacts', 'name_boss',
                   'license', 'direction_of_rehabilitation', 'form_service',
                   'resources', 'total_seats',
                   'free_seats', 'result_checks', 'work_experience', 'departmental_affiliation', 'parent_organization',
                   'other_information')

    def is_accessible(self):
        return not current_user.is_authenticated


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and not current_user.role_id == 1

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))


class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role_id == 1
