from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')

@app.errorhandler(404)
def not_found(e):
    return "Page not found", 404

from app.views import main_blueprint
from app.example_module.views import module_blueprint

app.register_blueprint(main_blueprint)
app.register_blueprint(module_blueprint)
# Register more blueprints later
