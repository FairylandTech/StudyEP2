import users

## 定义路由

@users.users_bp.route(rule='/index')
def home_users():
    return 'Home Users'
