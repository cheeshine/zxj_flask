#!/usr/bin/env python
from flask_script import Manager , Shell, Server
from flask_assets import ManageAssets
from example import app,assets_env

manager = Manager(app)
manager.add_command("runserver" , Server())
manager.add_command("shell",Shell())
manager.add_command("assets",ManageAssets(assets_env))
manager.run()


