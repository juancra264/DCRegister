from __future__ import print_function  # Use print() instead of print
from flask import url_for


def test_page_urls(client):
    # Visit home page
    response = client.get("/", follow_redirects=True)
    assert response.status_code == 200

    # Visit admin page   should redirect to sign-in, so we will get 302
    response = client.get(url_for('admin.index'), follow_redirects=False)
    assert response.status_code == 302

    # Visit members page   should redirect to sign-in, so we will get 302
    response = client.get("/members/", follow_redirects=False)
    assert response.status_code == 302

    # Visit members page   should redirect to sign-in, so we will get 302
    response = client.get("/members/profile/", follow_redirects=False)
    assert response.status_code == 302

    # Visit Regitro Ingreso
    response = client.get(url_for('public.ingreso_page'), follow_redirects=True)
    assert response.status_code == 200

    # Visit Regitro Salida
    response = client.get("/RegistroSalida", follow_redirects=True)
    assert response.status_code == 200


def test_admin_login(client):
    # Login as admin
    response = client.post(url_for('user.login'), follow_redirects=True,
                           data=dict(email='admin@example.com',
                                     password='admin123'))
    assert response.status_code == 200
    # Visit Admin page
    response = client.get(url_for('admin.index'), follow_redirects=False)
    assert response.status_code == 200

    # Logout
    response = client.get("/user/sign-out", follow_redirects=True)
    assert response.status_code == 200
