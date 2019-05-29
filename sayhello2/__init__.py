from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# 程序实例化
app = Flask(__name__)
# 导入配置。（疑问：必须要在数据库对象实例化之前导入配置吗）
app.config.from_pyfile(r'settings.py')
# 两个不知名参数
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# 数据库对象实例化
db = SQLAlchemy(app)


# 导入视图函数、错误处理、自定义命令（疑问：为什么要在最后导入而不是在开始）
from sayhello2 import views, errors, commands
