from flask import render_template, redirect, session, request, flash

def index():
    print('INDEX RUNNING')
    return render_template('index.html')

def other():
    return "Other!"