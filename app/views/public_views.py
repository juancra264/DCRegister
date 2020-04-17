from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from app.models.models import VisitorEntranceForm, VisitorExitForm
from app.models.user_models import Visitorlog

public_blueprint = Blueprint('public', __name__, template_folder='templates')


@public_blueprint.route('/')
def home_page():
    return render_template('pages/home_page.html')


@public_blueprint.route('/RegistroIngreso', methods=['GET', 'POST'])
def ingreso_page():
    form = VisitorEntranceForm()
    if form.validate_on_submit():
        flash('Se registra ingreso de {} para el cliente {} \
               {}'.format(form.Fullname.data,
                          form.ClienteBT.data,
                          datetime.now()))
        visitor = Visitorlog(ClienteBT=form.ClienteBT.data,
                             Fullname=form.Fullname.data,
                             NumeroID=form.NumeroID.data,
                             Actividad=form.Actividad.data,
                             IngresaMedios=form.IngresaMedios.data,
                             FechaHoraIngreso=datetime.now(),
                             EnAreaBlanca=False,
                             Operador="Pendiente"
                             )
        db.session.add(visitor)
        db.session.commit()
        return redirect(url_for('public.home_page'))
    return render_template('pages/ingreso_page.html', form=form)


@public_blueprint.route('/RegistroSalida', methods=['GET', 'POST'])
def salida_page():
    form = VisitorExitForm()
    form.Fullname.choices = [(g.id, g.Fullname) for g in Visitorlog.query.filter(
        Visitorlog.EnAreaBlanca is True).order_by('Fullname')]
    if form.validate_on_submit():
        visitor = Visitorlog.query.filter(Visitorlog.id == form.Fullname.data).first()
        visitor.EnAreaBlanca = False
        visitor.FechaHoraSalida = datetime.now()
        db.session.commit()
        flash('Salida registrada para {} a las \
              {}'.format(visitor.Fullname,
                         datetime.now().strftime("%H:%M %Y-%m-%d")))
        return redirect(url_for('public.home_page'))
    return render_template('pages/salida_page.html', form=form)
