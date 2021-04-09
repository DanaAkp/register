from flask import request, url_for, redirect
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class OrganizationView(ModelView):
    # def create_view(self, *args, **kwargs):
    #     if not current_user.is_authenticated:
    #         self.can_create = False
    #         self.can_edit = False
    #         self.can_delete = False
    column_filters = ['name']  # TODO добавить id_form_service
    column_searchable_list = ('name', 'contacts')

    # column_hide_backrefs = False
    # TODO вместо id_form_service писать name
    column_list = ('id', 'name', 'date_registration', 'opf', 'contacts', 'name_boss',
                   'license', 'direction_of_rehabilitation', 'id_form_service',
                   'resources', 'total_seats',
                   'free_seats', 'result_checks', 'work_experience', 'departmental_affiliation', 'parent_organization',
                   'other_information')

    # def get_query(self):
    #     query = self.session.query(self.model)


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))

