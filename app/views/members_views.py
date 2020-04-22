from datetime import datetime, timedelta
from flask import Blueprint, redirect, render_template, request, url_for
from flask_user import current_user, login_required
from app import db, babel
from app.models.models import EditVisitorEntranceForm, QueryByIdForm, QueryByCustomerForm
from app.models.user_models import UserProfileForm, Visitorlog
from flask import current_app as app
import gettext

members_blueprint = Blueprint('members', __name__, template_folder='templates')


@babel.localeselector
def get_locale():
    translations = [str(translation) for translation in
                    babel.list_translations()]
    return request.accept_languages.best_match(translations)


def set_lang(lang):
    i18n_dir = app.config['BABEL_TRANSLATION_DIRECTORIES']
    gettext.install('lang', i18n_dir)
    trans_file = i18n_dir + lang + '/LC_MESSAGES/flask_user'
    tr = gettext.translation(trans_file, 'locale', languages=[lang])
    tr.install(True)
    app.jinja_env.install_gettext_translations(tr)


@members_blueprint.before_app_request
def before_request():
    lang = get_locale()
    lang = lang if lang else app.config['BABEL_DEFAULT_LOCALE']
    set_lang(lang)

    if request.path.startswith('/admin'):
        if current_user.is_authenticated:
            if not current_user.has_role("admin"):
                return redirect(url_for('user.logout'))
        else:
            return redirect(url_for('user.login'))


@members_blueprint.route('/members/')
@login_required
def member_page():
    visitors = Visitorlog.query.filter(Visitorlog.Operador == 'Pendiente')
    return render_template('pages/user_page.html', visitors=visitors)


@members_blueprint.route('/members/validar/<string:id_data>', methods=['POST', 'GET'])
@login_required
def validate_page(id_data):
    visitor = Visitorlog.query.filter_by(id=int(id_data)).first()
    visitor.Operador = current_user.email
    visitor.EnAreaBlanca = True
    db.session.commit()
    return redirect(url_for('members.member_page'))


@members_blueprint.route('/members/editar/<string:id_data>', methods=['POST', 'GET'])
@login_required
def edit_page(id_data):
    visitor = Visitorlog.query.filter_by(id=int(id_data)).first()
    form = EditVisitorEntranceForm(ClienteBT=visitor.ClienteBT,
                                   Fullname=visitor.Fullname,
                                   NumeroID=visitor.NumeroID,
                                   Actividad=visitor.Actividad,
                                   IngresaMedios=visitor.IngresaMedios)
    if request.method == 'POST' and form.validate():
        visitor.ClienteBT = form.ClienteBT.data
        visitor.Fullname = form.Fullname.data
        visitor.NumeroID = form.NumeroID.data
        visitor.Actividad = form.Actividad.data
        visitor.IngresaMedios = form.IngresaMedios.data
        db.session.commit()
        return redirect(url_for('members.member_page'))
    return render_template('pages/edit_ingreso_page.html', form=form)


@members_blueprint.route('/members/cancelar/<string:id_data>', methods=['POST', 'GET'])
@login_required
def cancel_page(id_data):
    visitor = Visitorlog.query.filter_by(id=int(id_data)).first()
    db.session.delete(visitor)
    db.session.commit()
    return redirect(url_for('members.member_page'))


@members_blueprint.route('/members/reports')
@login_required
def reports_page():
    return render_template('pages/reports_page.html')


@members_blueprint.route('/members/reports/alldata')
@login_required
def reports_all_page():
    visitors = Visitorlog.query.all()
    return render_template('pages/reports_alldata.html', visitors=visitors)


@members_blueprint.route('/members/reports/byID', methods=['POST', 'GET'])
@login_required
def reports_byid_page():
    form = QueryByIdForm()
    if request.method == 'POST' and form.validate():
        hoy = datetime.strptime(str(form.FechaFin.data), "%Y-%m-%d")
        hoy = hoy + timedelta(hours=23, minutes=55, seconds=59, microseconds=999999)
        visitors = Visitorlog.query.filter(Visitorlog.NumeroID == form.NumeroID.data). \
            filter(Visitorlog.FechaHoraIngreso < hoy,
                   Visitorlog.FechaHoraIngreso >= form.FechaInicio.data). \
            order_by(Visitorlog.FechaHoraIngreso.desc()).all()
        return render_template('pages/results.html', visitors=visitors,
                               consulta="por Identificación")
    return render_template('pages/reports_byID.html', form=form)


@members_blueprint.route('/members/reports/byCustomer', methods=['POST', 'GET'])
@login_required
def reports_bycustomer_page():
    i = 0
    form = QueryByCustomerForm()
    clientes = list(set([g.ClienteBT for g in Visitorlog.query.all()]))
    choices = []
    for x in clientes:
        choices.append((i, x))
    form.ClienteBT.choices = choices
    if request.method == 'POST' and form.validate():
        hoy = datetime.strptime(str(form.FechaFin.data), "%Y-%m-%d")
        hoy = hoy + timedelta(hours=23, minutes=55, seconds=59, microseconds=999999)
        visitors = Visitorlog.query.filter(Visitorlog.ClienteBT == clientes[form.ClienteBT.data]). \
            filter(Visitorlog.FechaHoraIngreso < hoy,
                   Visitorlog.FechaHoraIngreso >= form.FechaInicio.data). \
            order_by(Visitorlog.FechaHoraIngreso.desc()).all()
        return render_template('pages/results.html', visitors=visitors,
                               consulta="por Cliente")
    return render_template('pages/reports_byCustomer.html', form=form)


@members_blueprint.route('/members/profile/', methods=['GET', 'POST'])
@login_required
def user_profile_page():
    # Initialize form
    # form = UserProfileForm(request.form, current_user)
    form = UserProfileForm()

    # Process valid POST
    if request.method == 'POST' and form.validate():
        # Copy form fields to user_profile fields
        form.populate_obj(current_user)

        # Save user_profile
        db.session.commit()

        # Redirect to home page
        return redirect(url_for('public.home_page'))

    # Process GET or invalid POST
    return render_template('pages/user_profile_page.html',
                           form=form)
