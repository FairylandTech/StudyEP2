from flask import Blueprint

test_api = Blueprint(name='test_api', import_name=__name__, url_prefix='/test')
"""
构建蓝图
name: 蓝图名称
import_name: 模块名称
url_prefix: url前缀
"""

