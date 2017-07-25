#!/usr/bin/env python
from flask_script import Manager
from hubstry.app import app


manager = Manager(app)


@manager.option('-h',
                '--host',
                dest='host',
                default='0.0.0.0',
                help='hostname')
@manager.option('-p',
                '--port',
                dest='port',
                default=8000,
                help='port number')
def runserver(host, port):
    app.run(host=host, port=int(port))


if __name__ == '__main__':
    manager.run()
