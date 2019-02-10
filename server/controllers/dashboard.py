from flask import render_template, redirect, session, url_for

def index():
    if 'user_id' not in session:
        return redirect(url_for('users:new'))
    return render_template('dashboard/index.html')