from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app.helpers import cached

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    return render_template('pages/index.html')
