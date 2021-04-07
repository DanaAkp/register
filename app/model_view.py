from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from app.models import Organization, ServiceForm


class FormServiceModelView(ModelView):
    datamodel = SQLAInterface(ServiceForm)


class OrganizationModelView(ModelView):
    datamodel = SQLAInterface(Organization)
    # related_views = [FormServiceModelView]

