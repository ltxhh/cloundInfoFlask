# 创建Token与校验Token


import jwt
from flask import current_app


def generate_jwt(payload, expiry, secret=None):
    """"
    生成jwt
    :param payload: dict 载荷
    :param expiry: datetime 有效期
    :param secret: 盐
    :return: token
    """
    _payload = {
        'exp': expiry
    }
    _payload.update(payload)

    if not secret:
        secret = current_app.config['JWT_SECRET']

    token = jwt.encode(_payload, secret, algorithm='HS256')

    return token


def verify_jwt(token, secret=None):
    """
    校验jwt
    :param token: token值
    :param secret: 盐
    :return: payload 载荷
    """
    if not secret:
        secret = current_app.config['JWT_SECRET']

    try:
        payload = jwt.decode(token, secret, algorithms='HS256')
    except:
        payload = None
    return payload
