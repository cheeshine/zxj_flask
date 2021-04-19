# coding: utf-8
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from run import app
from app import db


# 加载config
app.config.from_object('app.config')

# 初始化db
db.init_app(app)

# 创建migrate和manager对象
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()



