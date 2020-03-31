from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, SubmitField
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
    Operador = StringField('Operador que Acompaña', validators=[DataRequired()])
    FechaIngreso = DateField('Fecha Ingreso', format='%Y-%m-%d',
                              default=datetime.now())
    HoraIngreso = TimeField('Hora Ingreso', default=datetime.now())
    submit = SubmitField('Registrar Ingreso')


class VisitorExitForm(FlaskForm):
    Fullname = StringField('Nombre Completo', validators=[DataRequired()])
    FechaSalida = DateField('Fecha Salida', format='%Y-%m-%d',
                              default=datetime.now())
    HoraSalida = TimeField('Hora Salida', default=datetime.now())
    submit = SubmitField('Registrar Salida')
