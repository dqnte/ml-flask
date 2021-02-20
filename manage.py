import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from server.main import create_server, db

server = create_server('dev')
server.app_context().push()

manager = Manager(server)

migrate = Migrate(server, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    server.run()


if __name__ == '__main__':
    manager.run()
