#!/usr/bin/env python
from flask_script import Manager, Shell, Server
from flask_script.commands import ShowUrls, Clean

from pynashapi import create_app, DB
from commands.db_init import DbInit, DbProp

app = create_app()

manager = Manager(app)


def make_shell_config():
    return dict(app=app, DB=DB)


manager.add_command('runserver', Server())
manager.add_command('shell', Shell(make_context=make_shell_config))
manager.add_command('shows-url', ShowUrls())
manager.add_command('clean', Clean())
manager.add_command('db-init', DbInit(DB))
manager.add_command('db-prop', DbProp(DB))

if __name__ == '__main__':
    manager.run()
