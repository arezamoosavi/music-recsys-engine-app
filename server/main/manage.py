from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from web import flask_app, db

migrate = Migrate(flask_app, db)

manager = Manager(flask_app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()