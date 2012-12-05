from flask.ext.script import Manager
from app import app

manager = Manager(app)

@manager.command
def runserver():
    app.run(host='0.0.0.0', port=5000, debug=app.config['DEBUG'])

if __name__ == '__main__':
    if app.config['ENVIRONMENT'] != 'production':
        manager.run()
    else:
        app.run()
