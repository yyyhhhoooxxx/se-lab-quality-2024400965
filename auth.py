def authenticate_user(username: str, password: str) -> bool:
    """用户登录验证
    :param username: 用户名
    :param password: 密码
    :return: 验证成功返回True，失败返回False
    """
    return username == "admin" and password == "123456"