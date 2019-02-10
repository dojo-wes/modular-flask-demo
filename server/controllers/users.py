from flask import render_template, request, redirect, session, url_for, flash
from server.models.user import User

def new():
    return render_template('users/new.html')

def create():
    errors = User.helpers.validate(request.form)
    if errors:
        for error in errors:
            flash(error)
        return redirect(url_for('users:new'))

    User.helpers.create(request.form)
    return redirect(url_for('dashboard:index'))