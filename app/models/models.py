from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, SubmitField, SelectField, HiddenField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField, TimeField
db = SQLAlchemy()


class AdmUsers(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.Unicode(255), nullable=False,
                      server_default=u'', unique=True)
    confirmed_at = db.Column(db.DateTime())
    password = db.Column(db.String(255), nullable=False, server_default='')
    active = db.Column(db.Boolean(), nullable=False, server_default='0')

    active = db.Column('is_active', db.Boolean(),
                       nullable=False, server_default='0')


class AdmUsersRoles(db.Model):
    __tablename__ = 'users_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer())
    role_id = db.Column(db.Integer())


class AdmRoles(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False,
                     server_default=u'', unique=True)
    # for display purposes
    label = db.Column(db.Unicode(255), server_default=u'')


class VisitorEntranceForm(FlaskForm):
    ClienteBT = StringField('Cliente BT', validators=[DataRequired()])
    Fullname = StringField('Nombre Completo', validators=[DataRequired()])
    NumeroID = StringField('Numero Identificacion', validators=[DataRequired()])
    Actividad = TextAreaField(u'Descripcion Actividad')
    IngresaMedios = BooleanField('Ingresa Medios')
    image = HiddenField('image')
    submit = SubmitField('Registrar Ingreso')


class EditVisitorEntranceForm(FlaskForm):
    ClienteBT = StringField('Cliente BT', validators=[DataRequired()])
    Fullname = StringField('Nombre Completo', validators=[DataRequired()])
    NumeroID = StringField('Numero Identificacion', validators=[DataRequired()])
    Actividad = TextAreaField(u'Descripcion Actividad')
    IngresaMedios = BooleanField('Ingresa Medios')
    submit = SubmitField('Guardar Cambios')


class VisitorExitForm(FlaskForm):
    Fullname = SelectField(u'Fullname', coerce=int)
    submit = SubmitField('Registrar Salida')


class QueryByIdForm(FlaskForm):
    today_date = datetime.today().date()
    first_day_of_month = today_date.replace(day=1)
    NumeroID = StringField('Numero Identificacion', validators=[DataRequired()])
    FechaFin = DateField('Fecha Fin', id='datepick',
                            default=today_date)
    FechaInicio = DateField('Fecha Inicio', id='datepick',
                            default=first_day_of_month)
    submit = SubmitField('Consultar')


class QueryByCustomerForm(FlaskForm):
    today_date = datetime.today().date()
    first_day_of_month = today_date.replace(day=1)
    #ClienteBT = StringField('Cliente BT', validators=[DataRequired()])
    ClienteBT = SelectField(u'Cliente BT', coerce=int)
    FechaFin = DateField('Fecha Fin', id='datepick',
                            default=today_date)
    FechaInicio = DateField('Fecha Inicio', id='datepick',
                            default=first_day_of_month)
    submit = SubmitField('Consultar')
