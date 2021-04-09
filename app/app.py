from flask import request

from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_bootstrap3 import Bootstrap
from flask_migrate import Migrate
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from flask_wtf import CSRFProtect
from app.forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.url_map.strict_slashes = False
FLASK_ENV = os.environ.get("FLASK_ENV") or 'development'
app.config.from_object('app.config.%s%sConfig' % (FLASK_ENV[0].upper(), FLASK_ENV[1:]))
app.static_folder = app.config['STATIC_FOLDER']
bootstrap = Bootstrap(app)
CSRFProtect(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)


from app.models import User, Organization, TypeOfService, ServiceForm, Role


db.create_all()


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


admin = Admin(app=app, name='Реестр реабилитационных организаций', template_mode='bootstrap3')


from app.admin import MyModelView, OrganizationView, AdminModelView


admin.add_view(OrganizationView(Organization, db.session, endpoint='model_view_organization'))

admin.add_view(MyModelView(Organization, db.session))
admin.add_view(MyModelView(TypeOfService, db.session))
admin.add_view(MyModelView(ServiceForm, db.session))

admin.add_view(AdminModelView(User, db.session))
admin.add_view(AdminModelView(Role, db.session))


# region View
@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect('/admin')
    return redirect(url_for('model_view_organization.index_view'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        if user.is_block:
            flash('your account is blocked by the administrator')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == "POST":
        username = form.username.data
        password = form.password.data
        if User.query.filter_by(name=username).first() is None:
            new_user = User()
            new_user.name = username
            new_user.set_password(password)
            new_user.is_block = False
            db.session.add(new_user)
            db.session.commit()
        else:
            flash('Username is exist')
            return render_template('register.html', form=form)
    return render_template('register.html', title='Register', form=form)


