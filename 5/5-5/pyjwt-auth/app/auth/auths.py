# coding: utf-8
import jwt
import datetime
import time
from flask import jsonify
from app.users.model import Users
from .. import config
from .. import common


class Auth:
    @staticmethod
    def encode_auth_token(user_id, login_time):
        """
        生成认证token
        :param user_id: int
        :param login_time: int(timestamp)
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=60),
                'iat': datetime.datetime.utcnow(),
                'iss': 'ken',
                'data': {
                    'id': user_id,
                    'login_time': login_time
                }
            }
            return jwt.encode(
                payload,
                config.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        验证token
        :param auth_token:
        :return: int|str
        """
        try:
            payload = jwt.decode(auth_token,  config.SECRET_KEY, options={'verify_exp': False})
            if 'data' in payload and 'id' in payload['data']:
                return payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return 'Token过期'
        except jwt.InvalidTokenError:
            return '无效Token'

    def authenticate(self, username, password):
        """
        用户登录，登录成功返回token,将登录时间写入数据库；登录失败返回失败原因
        :param username:
        :param password:
        :return: json
        """
        user_info = Users.query.filter_by(username=username).first()
        if user_info is None:
            return jsonify(common.false_return('', '用户不存在'))
        else:
            if Users.check_password(Users, user_info.password, password):
                login_time = int(time.time())
                user_info.login_time = login_time
                Users.update(Users)
                token = self.encode_auth_token(user_info.id, login_time)
                print(token)
                return jsonify(common.true_return(token.decode(), '登录成功'))
            else:
                return jsonify(common.false_return('', '密码不正确'))

    def identify(self, request):
        """
        用户鉴权
        :param request:
        :return:
        """
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token_arr = auth_header.split(' ')
            if not auth_token_arr or auth_token_arr[0] != 'JWT' or len(auth_token_arr) != 2:
                result = common.false_return('', '验证错误')
            else:
                auth_toke = auth_token_arr[1]
                payload = self.decode_auth_token(auth_toke)
                if not isinstance(payload, str):
                    user = Users.get(Users, payload['data']['id'])
                    if user is None:
                        result = common.false_return('', '用户不存在')
                    else:
                        if user.login_time == payload['data']['login_time']:
                            result = common.true_return(user.id, '请求成功')
                        else:
                            result = common.false_return('', 'token已更改，请重新登录')
                else:
                    result = common.false_return('', payload)
        else:
            result = common.false_return('', '无认证token')
        return result



