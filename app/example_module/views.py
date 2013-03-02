from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app.example_module.decorators import example_wrapper

module_blueprint = Blueprint('module', __name__, url_prefix="/module")

@module_blueprint.route('/')
def index():
    return "Index"
