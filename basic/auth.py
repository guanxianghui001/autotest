import functools

from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

from basic.db import get_db,close_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

# @bp.before_app_request
# def load_logged_in_user():
#     user_id = session.get('user_id')
#
#     if user_id is None:
#         g.user = None
#     else:
#         g.user = get_db().execute(
#             'SELECT * FROM user WHERE id = ?', (user_id,)
#         ).fetchone()

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        realname = request.form['realname']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not realname:
            error = 'realname is required'
        elif db.execute(
            'SELECT id FROM user WHERE user = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO yl_user (user,name, password) VALUES (?, ?, ?)',
                (username, realname,generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))
            close_db()
        flash(error)

    return render_template('auth/register.html')